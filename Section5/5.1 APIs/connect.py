# https://www.ncdc.noaa.gov/cdo-web/webservices/v2
import requests
import json

my_token = 'BGbaBUBaAHEzVDwWytxUWFKmQUSDcbIM'
creds = dict(token=my_token)
dtype = 'data'

req = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?'
                   'datasetid=GHCND&locationid=ZIP:28801&'
                   'startdate=2010-05-01&enddate=2010-05-01',
                   dtype, headers=creds)
print(req.text)


jsonify = req.json()
with open('weather.json', 'w') as f:
    data = json.dump(jsonify, f)

