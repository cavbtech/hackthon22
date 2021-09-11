#!/usr/bin/python3                                                                                                      
                                                                                                                        
from confluent_kafka import Producer
import socket


                                                                                       
from random import randint                                                                                              
from time import sleep                                                                                                  
import sys                                                                                                              

##localhost:29092                                                                                                                       
BROKER = 'kafka:9092'                                                                                               
TOPIC  = 'housing'                                                                                                      
                                                                                                                        
house_data = 'test.csv'                                                                                
house_data_records = open(house_data).read().splitlines()                                                                             
                                                                                                                        
try:
    conf = {'bootstrap.servers': BROKER,'client.id': socket.gethostname()}   
    p = Producer(conf)                                                                                                                 
    #p = KafkaProducer(bootstrap_servers=BROKER)                                                                         
except Exception as e:                                                                                                  
    print(f"ERROR --> {e}")                                                                                             
    sys.exit(1)                                                                                                        
counter =0                                                                                                                      
while True:                                                                                                
    for message in house_data_records:                                                                                      
        print(f"message to be produced={message}")                                                                          
        p.produce(TOPIC, key=str(counter),value=message)    
        p.flush() 
        counter = counter + 1                                                                 
        sleep(randint(1,4))