import json

with open('menu.json') as f:
    data = json.load(f)

print(data[0])