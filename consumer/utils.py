import json

def convertToFloat(instr):
        if instr.isnumeric():
            return float(instr)
        else :
            return 0.0

class Record:

    def __init__(self,input_record):
        self.Id=convertToFloat(input_record[0])
        self.MSSubClass=convertToFloat(input_record[1])
        self.MSZoning=str(input_record[2])
        self.LotArea=convertToFloat(input_record[3])
        self.Street=str(input_record[4])
        self.LotShape=str(input_record[5])
        self.LandContour=str(input_record[6])
        self.Utilities=str(input_record[7])
        self.LotConfig=str(input_record[8])
        self.LandSlope=str(input_record[9])
        self.Neighborhood=str(input_record[10])
        self.Condition1=str(input_record[11])
        self.Condition2=str(input_record[12])
        self.BldgType=str(input_record[13])
        self.HouseStyle=str(input_record[14])
        self.OverallQual=convertToFloat(input_record[15])
        self.OverallCond=convertToFloat(input_record[16])
        self.YearBuilt=convertToFloat(input_record[17])
        self.YearRemodAdd=convertToFloat(input_record[18])
        self.RoofStyle=str(input_record[19])
        self.RoofMatl=str(input_record[20])
        self.Exterior1st=str(input_record[21])
        self.Exterior2nd=str(input_record[22])
        self.MasVnrType=str(input_record[23])
        self.MasVnrArea=convertToFloat(input_record[24])
        self.ExterQual=str(input_record[25])
        self.ExterCond=str(input_record[26])
        self.Foundation=str(input_record[27])
        self.BsmtQual=str(input_record[28])
        self.BsmtCond=str(input_record[29])
        self.BsmtExposure=str(input_record[30])
        self.BsmtFinType1=str(input_record[31])
        self.BsmtFinSF1=convertToFloat(input_record[32])
        self.BsmtFinType2=str(input_record[33])
        self.BsmtFinSF2=convertToFloat(input_record[34])
        self.BsmtUnfSF=convertToFloat(input_record[35])
        self.TotalBsmtSF=convertToFloat(input_record[36])
        self.Heating=str(input_record[37])
        self.HeatingQC=str(input_record[38])
        self.CentralAir=str(input_record[39])
        self.Electrical=str(input_record[40])
        self.fstFlrSF=convertToFloat(input_record[41])
        self.sndFlrSF=convertToFloat(input_record[42])
        self.LowQualFinSF=convertToFloat(input_record[43])
        self.GrLivArea=convertToFloat(input_record[44])
        self.BsmtFullBath=convertToFloat(input_record[45])
        self.BsmtHalfBath=convertToFloat(input_record[46])
        self.FullBath=convertToFloat(input_record[47])
        self.HalfBath=convertToFloat(input_record[48])
        self.BedroomAbvGr=convertToFloat(input_record[49])
        self.KitchenAbvGr=convertToFloat(input_record[50])
        self.KitchenQual=str(input_record[51])
        self.TotRmsAbvGrd=convertToFloat(input_record[52])
        self.Functional=str(input_record[53])
        self.Fireplaces=convertToFloat(input_record[54])
        self.GarageType=str(input_record[55])
        self.GarageYrBlt=convertToFloat(input_record[56])
        self.GarageFinish=str(input_record[57])
        self.GarageCars=convertToFloat(input_record[58])
        self.GarageArea=convertToFloat(input_record[59])
        self.GarageQual=str(input_record[60])
        self.GarageCond=str(input_record[61])
        self.PavedDrive=str(input_record[62])
        self.WoodDeckSF=convertToFloat(input_record[63])
        self.OpenPorchSF=convertToFloat(input_record[64])
        self.EnclosedPorch=convertToFloat(input_record[65])
        self.SsnPorch=convertToFloat(input_record[66])
        self.ScreenPorch=convertToFloat(input_record[67])
        self.PoolArea=convertToFloat(input_record[68])
        self.MiscVal=convertToFloat(input_record[69])
        self.MoSold=convertToFloat(input_record[70])
        self.YrSold=convertToFloat(input_record[71])
        self.SaleType=str(input_record[72])
        self.SaleCondition=str(input_record[73])
    
    def getJsonObject(self):
        #return json.dumps(self.__dict__)
        
        processed = {   "Id":self.Id,
                        "MSSubClass":self.MSSubClass,
                        "MSZoning":self.MSZoning,
                        "LotArea":self.LotArea,
                        "Street":self.Street,
                        "LotShape":self.LotShape,
                        "LandContour":self.LandContour,
                        "Utilities":self.Utilities,
                        "LotConfig":self.LotConfig,
                        "LandSlope":self.LandSlope,
                        "Neighborhood":self.Neighborhood,
                        "Condition1":self.Condition1,
                        "Condition2":self.Condition2,
                        "BldgType":self.BldgType,
                        "HouseStyle":self.HouseStyle,
                        "OverallQual":self.OverallQual,
                        "OverallCond":self.OverallCond,
                        "YearBuilt":self.YearBuilt,
                        "YearRemodAdd":self.YearRemodAdd,
                        "RoofStyle":self.RoofStyle,
                        "RoofMatl":self.RoofMatl,
                        "Exterior1st":self.Exterior1st,
                        "Exterior2nd":self.Exterior2nd,
                        "MasVnrType":self.MasVnrType,
                        "MasVnrArea":self.MasVnrArea,
                        "ExterQual":self.ExterQual,
                        "ExterCond":self.ExterCond,
                        "Foundation":self.Foundation,
                        "BsmtQual":self.BsmtQual,
                        "BsmtCond":self.BsmtCond,
                        "BsmtExposure":self.BsmtExposure,
                        "BsmtFinType1":self.BsmtFinType1,
                        "BsmtFinSF1":self.BsmtFinSF1,
                        "BsmtFinType2":self.BsmtFinType2,
                        "BsmtFinSF2":self.BsmtFinSF2,
                        "BsmtUnfSF":self.BsmtUnfSF,
                        "TotalBsmtSF":self.TotalBsmtSF,
                        "Heating":self.Heating,
                        "HeatingQC":self.HeatingQC,
                        "CentralAir":self.CentralAir,
                        "Electrical":self.Electrical,
                        "fstFlrSF":self.fstFlrSF,
                        "sndFlrSF":self.sndFlrSF,
                        "LowQualFinSF":self.LowQualFinSF,
                        "GrLivArea":self.GrLivArea,
                        "BsmtFullBath":self.BsmtFullBath,
                        "BsmtHalfBath":self.BsmtHalfBath,
                        "FullBath":self.FullBath,
                        "HalfBath":self.HalfBath,
                        "BedroomAbvGr":self.BedroomAbvGr,
                        "KitchenAbvGr":self.KitchenAbvGr,
                        "KitchenQual":self.KitchenQual,
                        "TotRmsAbvGrd":self.TotRmsAbvGrd,
                        "Functional":self.Functional,
                        "Fireplaces":self.Fireplaces,
                        "GarageType":self.GarageType,
                        "GarageYrBlt":self.GarageYrBlt,
                        "GarageFinish":self.GarageFinish,
                        "GarageCars":self.GarageCars,
                        "GarageArea":self.GarageArea,
                        "GarageQual":self.GarageQual,
                        "GarageCond":self.GarageCond,
                        "PavedDrive":self.PavedDrive,
                        "WoodDeckSF":self.WoodDeckSF,
                        "OpenPorchSF":self.OpenPorchSF,
                        "EnclosedPorch":self.EnclosedPorch,
                        "SsnPorch":self.SsnPorch,
                        "ScreenPorch":self.ScreenPorch,
                        "PoolArea":self.PoolArea,
                        "MiscVal":self.MiscVal,
                        "MoSold":self.MoSold,
                        "YrSold":self.YrSold,
                        "SaleType":self.SaleType,
                        "SaleCondition":self.SaleCondition
                }

        return processed
