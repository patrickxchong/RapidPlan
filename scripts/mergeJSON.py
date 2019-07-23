from collections import defaultdict
import json

with open('js/data.json') as json_data:
    priceList = json.load(json_data)
with open('js/stations.json') as json_data:
    stations = json.load(json_data)


for key, value in stations.items():
    if key not in priceList:
        priceList[key] = {}
    priceList[key]["name"] = value[0]
    priceList[key]["line"] = value[1][1:-1]

with open('result.json', 'w') as fp:
    json.dump(priceList, fp)
