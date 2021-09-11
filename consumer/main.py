import os
import uvicorn
import requests
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from confluent_kafka import Consumer
import sys
import json
from utils import Record
from time import sleep 

# class which is expected in the payload

BROKER = 'kafka:9092'                                                                                               
TOPIC  = 'housing' 
encoding = 'utf-8'

PREDICTOR_ENDPOINT = os.getenv("PREDICTOR_ENDPOINT")

conf = {'bootstrap.servers': BROKER,
        'group.id': "foo",
        'auto.offset.reset': 'smallest'}

consumer = Consumer(conf)

running = True
topics  = [TOPIC]

def basic_consume_loop(consumer, topics):
    try:
        consumer.subscribe(topics)

        while running:
            msg = consumer.poll(timeout=1.0)
            if msg is None: 
                print("no messages yet")
                continue

            if msg.error():
                if msg.error().code():
                    # End of partition event
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise Exception(msg.error())
            else:
                msg_process(msg)
    finally:
        # Close down consumer to commit final offsets.
        consumer.close()

def shutdown():
    running = False
    
def msg_process(msg):
    try:
        record_key = msg.key()
        record_value = msg.value().decode(encoding)
        print(f"record_value={record_value}")
        inputObj     = Record(record_value.split(",")).getJsonObject()
        print(f"input record_key={record_key} and inputObj={inputObj}")
        endpoint = f"{PREDICTOR_ENDPOINT}/predict"
        print(f"predictor end point = {endpoint}")
        response =requests.post(endpoint, json=inputObj)
        print(f"predicted value for input record_key={record_key} and inputObj={inputObj} and prediction={response.json()}")
    except Exception as e:
        print(f"there are are errors {e}")

def testMessage():
    while True :
        try:
            inputObj = {"Id": 1485.0, "MSSubClass": 80.0, "MSZoning": "RL", "LotArea": 13300.0, "Street": "Pave", "LotShape": "IR1", "LandContour": "Lvl", "Utilities": "AllPub", "LotConfig": "Inside", "LandSlope": "Gtl", "Neighborhood": "Gilbert", "Condition1": "Norm", "Condition2": "Norm", "BldgType": "1Fam", "HouseStyle": "SLvl", "OverallQual": 7.0, "OverallCond": 5.0, "YearBuilt": 2004.0, "YearRemodAdd": 2004.0, "RoofStyle": "Gable", "RoofMatl": "CompShg", "Exterior1st": "VinylSd", "Exterior2nd": "VinylSd", "MasVnrType": "None", "MasVnrArea": 0.0, "ExterQual": "Gd", "ExterCond": "TA", "Foundation": "PConc", "BsmtQual": "Gd", "BsmtCond": "TA", "BsmtExposure": "No", "BsmtFinType1": "GLQ", "BsmtFinSF1": 326.0, "BsmtFinType2": "Unf", "BsmtFinSF2": 0.0, "BsmtUnfSF": 58.0, "TotalBsmtSF": 384.0, "Heating": "GasA", "HeatingQC": "Ex", "CentralAir": "Y", "Electrical": "SBrkr", "fstFlrSF": 744.0, "sndFlrSF": 630.0, "LowQualFinSF": 0.0, "GrLivArea": 1374.0, "BsmtFullBath": 1.0, "BsmtHalfBath": 0.0, "FullBath": 2.0, "HalfBath": 1.0, "BedroomAbvGr": 3.0, "KitchenAbvGr": 1.0, "KitchenQual": "Gd", "TotRmsAbvGrd": 7.0, "Functional": "Typ", "Fireplaces": 1.0, "GarageType": "BuiltIn", "GarageYrBlt": 2004.0, "GarageFinish": "Fin", "GarageCars": 2.0, "GarageArea": 400.0, "GarageQual": "TA", "GarageCond": "TA", "PavedDrive": "Y", "WoodDeckSF": 100.0, "OpenPorchSF": 0.0, "EnclosedPorch": 0.0, "SsnPorch": 0.0, "ScreenPorch": 0.0, "PoolArea": 0.0, "MiscVal": 0.0, "MoSold": 6.0, "YrSold": 2010.0, "SaleType": "WD", "SaleCondition": "Normal"}
            response = requests.post(f"{PREDICTOR_ENDPOINT}/predict", json=inputObj)
            print(f"predicted value for inputObj={inputObj} and prediction={response.json()}")
            sleep(2)
        except:
            sleep(5)

basic_consume_loop(consumer,topics)
#testMessage()
    
    