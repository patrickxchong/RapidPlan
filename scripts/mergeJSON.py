from collections import defaultdict
import json

with open('js/data.json') as json_data:
    data = json.load(json_data)
with open('points.json') as json_data:
    points = json.load(json_data)


for key in data.keys():
    data[key]["lat"] = points[key]["lat"]
    data[key]["lon"] = points[key]["lon"]

with open('result.json', 'w') as fp:
    json.dump(data, fp, indent=4)
