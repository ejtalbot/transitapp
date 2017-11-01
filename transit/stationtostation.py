import requests

#primary key a1b5423635a44927b351380e297efd37

headers = {
    # Request headers
    'api_key': 'a1b5423635a44927b351380e297efd37',
}

# exam[ple this_url = 'https://api.wmata.com/Rail.svc/json/jSrcStationToDstStationInfo?FromStationCode=E10&ToStationCode=J03'

#this_url = 'https://api.wmata.com/Rail.svc/json/jSrcStationToDstStationInfo?FromStationCode=' + fromStation + '&ToStationCode=' + toStation

def getStationToStation(fromStation, toStation):
    url = 'https://api.wmata.com/Rail.svc/json/jSrcStationToDstStationInfo?FromStationCode=' + fromStation + '&ToStationCode=' + toStation
    response = requests.get(url, headers = headers)
    return(response.json())

#print(getStationToStation('E10', 'J03'))