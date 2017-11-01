import requests
import django
from django.db import models
from .models import Line, Station

headers = {
    # Request headers
    'api_key': 'a1b5423635a44927b351380e297efd37',
}

def populateAllStations(main_line):
    url = 'https://api.wmata.com/Rail.svc/json/jStations?LineCode=' + str(main_line)
    response = requests.get(url, headers = headers)
    list_of_stations = response.json()['Stations']
    for i in range(len(list_of_stations)):
        current_station = list_of_stations[i]
        current_station_db = Station.objects.filter(code=current_station['Code']).first()
        current_station_db.code2 = Station.objects.filter(code=current_station['StationTogether1']).first()
        current_station_db.line2 = Line.objects.filter(name=current_station['LineCode2']).first()
        current_station_db.line3 = Line.objects.filter(name=current_station['LineCode3']).first()
        print(current_station_db)
        print(current_station_db.line2)
        print(current_station_db.line3)
        print("Code:" +str(current_station_db.code2))
        try:
            current_station_db.save()
        except:
            pass

#print(populateAllStations('RD'))