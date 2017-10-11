import requests
import django

#primary key a1b5423635a44927b351380e297efd37

headers = {
    # Request headers
    'api_key': 'a1b5423635a44927b351380e297efd37',
}

this_url = 'https://api.wmata.com/Rail.svc/json/jStations?'

def getAllStations(line):
    url = 'https://api.wmata.com/Rail.svc/json/jStations?LineCode=' + str(line)
    response = requests.get(url, headers = headers)
    return(response.json())

#print(getAllStations('RD')['Stations'])

def populateStations(line):
    url = 'https://api.wmata.com/Rail.svc/json/jStations?LineCode=' + str(line)
    response = requests.get(url, headers = headers)
    list_of_stations = response.json()['Stations']
    for i in range(len(list_of_stations)):
        print(list_of_stations[i])
    return list_of_stations

    #Stations

print(populateStations('RD'))