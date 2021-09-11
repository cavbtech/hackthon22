import os
import uvicorn
import requests
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

PREDICTOR_ENDPOINT = os.getenv("PREDICTR_ENDPOINT")


    
def process():
    ks = KafkaUtils.createDirectStream(ssc, ['housedata'], {'metadata.broker.list': 'localhost:29092'})
    line = ks.map(lambda x: x[1])  
    response = requests.post(f"{PREDICTR_ENDPOINT}/predict", json=line)
    
    print("before predicting the input")
    houseInputDF.show() 
    ## now predict
    
    print(f" predicted house value is= {response}")

process()