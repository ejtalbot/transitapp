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
        new_station = Station(name =current_station['Name'],
                              code=current_station['Code'],
                              latitude=current_station['Lat'],
                              longitude=current_station['Lon'],
                              street=current_station['Address']['Street'],
                              zip=current_station['Address']['Zip'],
                              city=current_station['Address']['City'],
                              line=Line.objects.get(name=main_line),
                              state=current_station['Address']['State'],
                              #line2=Line.objects.get(name=current_station['LineCode2']).first(),
                              #line3=Line.objects.get(name=current_station['LineCode3']).first(),
                              )
        print(new_station.line2)
        print(new_station.street)
        print(new_station)
        print(new_station.code)
        try:
            new_station.save()
        except:
            pass

#print(populateStations('RD'))