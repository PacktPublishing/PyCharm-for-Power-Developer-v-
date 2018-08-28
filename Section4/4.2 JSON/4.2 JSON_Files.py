import json

with open('USD.json') as f:
    data = json.load(f)

print('Base Dollars: ' + data['base'])

print('to Canadian Dollars: ' + str(data['rates']['CAD']))