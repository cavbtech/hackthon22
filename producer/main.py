#!/usr/bin/python3                                                                                                      
                                                                                                                        
from kafka import KafkaProducer                                                                                         
from random import randint                                                                                              
from time import sleep                                                                                                  
import sys                                                                                                              
                                                                                                                        
BROKER = 'localhost:29092'                                                                                               
TOPIC = 'housedata'                                                                                                      
                                                                                                                        
house_data = 'test.csv'                                                                                
house_data_records = open(house_data).read().splitlines()                                                                             
                                                                                                                        
try:                                                                                                                    
    p = KafkaProducer(bootstrap_servers=BROKER)                                                                         
except Exception as e:                                                                                                  
    print(f"ERROR --> {e}")                                                                                             
    sys.exit(1)                                                                                                        
                                                                                                                        
while True:                                                                                                             
    message = ''                                                                                                        
    for _ in range(randint(2, 7)):                                                                                      
        message += house_data_records[randint(0, len(house_data_records)-1)] + ' '                                                                
    print(f">>> '{message}'")                                                                                           
    p.send(TOPIC, bytes(message, encoding="utf8"))                                                                      
    sleep(randint(1,4))