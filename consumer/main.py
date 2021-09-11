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

# class which is expected in the payload



PREDICTOR_ENDPOINT = os.getenv("PREDICTOR_ENDPOINT")

BROKER = 'kafka:9092'                                                                                               
TOPIC  = 'housing' 


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
    record_key = msg.key()
    record_value = str(msg.value())
    inputObj     = Record(record_value.split(",")).getJsonObject()
    print(f"record_key={record_key} and inputObj={inputObj}")
    #data = json.loads(record_value)
    
basic_consume_loop(consumer,topics)
    
    