import requests

#primary key a1b5423635a44927b351380e297efd37

headers = {
    # Request headers
    'api_key': 'a1b5423635a44927b351380e297efd37',
}

this_url = 'https://api.wmata.com/Rail.svc/json/jLines'

def getAllStations(api_url):
    url = api_url
    response = requests.get(url, headers = headers)
    return(response.json())

print(getAllStations(this_url))