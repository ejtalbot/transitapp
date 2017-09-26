import requests

#primary key a1b5423635a44927b351380e297efd37

headers = {
    # Request headers
    'api_key': 'a1b5423635a44927b351380e297efd37',
}

this_url = 'https://api.wmata.com/StationPrediction.svc/json/GetPrediction/'

def getNextTrain(station_code, api_url):
    url = api_url + station_code
    response = requests.get(url, headers = headers)
    return(response.json())

#print(getNextTrain('All',this_url))