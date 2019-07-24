# [1]b.routes["0"].legs["0"].duration, ["0"].a["0"].t_duration

# results["].geometry.coordinates
import json
import requests
from collections import OrderedDict

with open('js/data.json') as json_data:
    data = json.load(json_data, object_pairs_hook=OrderedDict)

result = {}

for station, value in data.items():
    url = f"https://www.myrapid.com.my/clients/Myrapid_Prasarana_37CB56E7-2301-4302-9B98-DFC127DD17E9/api/prasarana_planner.ashx?action=list_street&search={value['name']}"
    print(url)
    head = {"Content-Type": "application/json",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    response = requests.get(url, headers=head)
    response_json = response.json()
    result[station] = {}
    result[station]["name"] = response_json["results"][0]["poiname"]
    result[station]["lon"] = response_json["results"][0]["geometry"]["coordinates"][0]
    result[station]["lat"] = response_json["results"][0]["geometry"]["coordinates"][1]

# result = OrderedDict()
# for i in sorted(data.keys(), reverse=True):
#     result[i] = data[i]


with open('result.json', 'w') as fp:
    json.dump(result, fp, indent=4)
