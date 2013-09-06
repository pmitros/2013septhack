import csv
import json
import sys
import logging
from logging.handlers import HTTPHandler

with open("../cleaned.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    first_row = reader.next()
    logger=logging.getLogger('sendevent')
    logger.addHandler(HTTPHandler(sys.argv[1], sys.argv[2]))

    i=0

    for row in reader:
        event = {'username':row[0], 
                 "time":row[1],
                 '''event_type''':"sakai."+row[2], 
                 """course""":row[3], 
                 'event':{}, 
                 "event_source": "playback"}
    
        logger.error(json.dumps(event))
        
        i += 1
        if i % 100 == 0:
            print i
