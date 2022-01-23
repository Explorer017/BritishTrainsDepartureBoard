from unittest import expectedFailure
import requests
import datetime

# import auth from auth.py
from auth import auth


class trains:
    def __init__(self, time,extime,destination,operator,stops, bus = False):
        self.time = time
        self.expectedTime = extime
        self.destination = destination
        self.operator = operator
        self.callingAt = stops
        self.bus = bus
    
    def getExpectedInfo(self):
        if self.expectedTime == self.time:
            return "On time"
        else:
            return f"Expt {self.expectedTime}"

# create a class for the services from the station code input
class station:
    def __init__(self, stationCode):
        current_time = datetime.datetime.now()
        r = requests.get(f'https://api.rtt.io/api/v1/json/search/{stationCode}', auth=auth)
        json = r.json()
        self.inputStaion = json['location']['name']
        self.trains = []
        for i in json['services']:
            s = requests.get(f'https://api.rtt.io/api/v1/json/service/{i["serviceUid"]}/{current_time.strftime("%Y")}/{current_time.strftime("%m")}/{current_time.strftime("%d")}', auth=auth)
            serviceJson = s.json()
            stopstart = 0
            stops = []
            for j in range(len(serviceJson['locations'])):
                if serviceJson['locations'][j]['crs'] == stationCode.upper():
                    stopstart = j
            for k in range(stopstart+1, len(serviceJson['locations'])):
                stops.append(serviceJson['locations'][k]['description'])
            if i["serviceType"] == "bus":
                self.trains.append(trains(i['locationDetail']['gbttBookedDeparture'],None,i['locationDetail']['destination'][0]['description'],i['atocName'],stops,True))
            else:
                self.trains.append(trains(i['locationDetail']['gbttBookedDeparture'],i['locationDetail']['realtimeDeparture'],i['locationDetail']['destination'][0]['description'],i['atocName'],stops))

