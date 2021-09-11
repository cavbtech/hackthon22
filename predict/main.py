# Import all needed modules
from numpy import number
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from fastapi import FastAPI
import uvicorn
import pandas as pd
from pydantic import BaseModel
import numpy as geek

# defining the main app
app = FastAPI(title="predictor", docs_url="/")



#load the data from my drive 
df_train = pd.read_csv('train.csv')

#delete columns with many missing data
df_train.drop(['PoolQC','MiscFeature','Alley','Fence','FireplaceQu','LotFrontage'], axis = 1,inplace=True)

#Drop rows with missing data 
df_train.dropna(inplace=True) 
X, y = df_train.loc[:, df_train.columns != 'SalePrice'], df_train['SalePrice']
# select categorical features
categorical_features = list(X.select_dtypes(include=['object']).columns)

numeric_features = list(X.select_dtypes(include=['int64', 'float64']).columns)
numeric_transformer = Pipeline(steps=[('poly',PolynomialFeatures(degree =2)),('scaler', StandardScaler())])

categorical_transformer = Pipeline(steps=[('onehot', OneHotEncoder(handle_unknown='ignore'))])
preprocessor = ColumnTransformer(transformers=[('num', numeric_transformer, numeric_features),('cat', categorical_transformer, categorical_features)])

clf = Pipeline(steps=[('preprocessor', preprocessor),('classifier', LinearRegression())])
X_train, X_test, y_train, y_test = train_test_split(df_train.loc[:, df_train.columns != 'SalePrice'], df_train['SalePrice'], test_size=0.25, random_state=42)

clf.fit(X_train, y_train)

                                                                                                 
# class which is expected in the payload
class QueryIn(BaseModel):
    Id:float
    MSSubClass:float
    MSZoning:str
    LotArea:float
    Street:str
    LotShape:str
    LandContour:str
    Utilities:str
    LotConfig:str
    LandSlope:str
    Neighborhood:str
    Condition1:str
    Condition2:str
    BldgType:str
    HouseStyle:str
    OverallQual:float
    OverallCond:float
    YearBuilt:float
    YearRemodAdd:float
    RoofStyle:str
    RoofMatl:str
    Exterior1st:str
    Exterior2nd:str
    MasVnrType:str
    MasVnrArea:float
    ExterQual:str
    ExterCond:str
    Foundation:str
    BsmtQual:str
    BsmtCond:str
    BsmtExposure:str
    BsmtFinType1:str
    BsmtFinSF1:float
    BsmtFinType2:str
    BsmtFinSF2:float
    BsmtUnfSF:float
    TotalBsmtSF:float
    Heating:str
    HeatingQC:str
    CentralAir:str
    Electrical:str
    fstFlrSF:float
    sndFlrSF:float
    LowQualFinSF:float
    GrLivArea:float
    BsmtFullBath:float
    BsmtHalfBath:float
    FullBath:float
    HalfBath:float
    BedroomAbvGr:float
    KitchenAbvGr:float
    KitchenQual:str
    TotRmsAbvGrd:float
    Functional:str
    Fireplaces:float
    GarageType:str
    GarageYrBlt:float
    GarageFinish:str
    GarageCars:float
    GarageArea:float
    GarageQual:str
    GarageCond:str
    PavedDrive:str
    WoodDeckSF:float
    OpenPorchSF:float
    EnclosedPorch:float
    SsnPorch:float
    ScreenPorch:float
    PoolArea:float
    MiscVal:float
    MoSold:float
    YrSold:float
    SaleType:str
    SaleCondition:str

# class which is returned in the response
class QueryOut(BaseModel):
    SalePrice: float                                                                                                 


# Route definitions
@app.get("/ping")
# Healthcheck route to ensure that the API is up and running
def ping():
    return {"ping": "pong"}

@app.post("/predict", response_model=QueryOut, status_code=200)
def predict(query:QueryIn):
    # x = list(query.dict().values())
    # pred = clf.predict([x])[0]
    x = query.dict()
    ##pred = clf.predict(geek.reshape(x,(1,-1)))
    actdata = pd.DataFrame([x])
    pred = clf.predict(actdata)
    output = {"SalePrice": pred}
    return output


# Main function to start the app when main.py is called
if __name__ == "__main__":
    # Uvicorn is used to run the server and listen for incoming API requests on 0.0.0.0:9990
    uvicorn.run("main:app", host="0.0.0.0", port=9990, reload=True)
