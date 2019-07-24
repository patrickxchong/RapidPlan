import requests
import json
import csv
import os
from pprint import pprint
from collections import OrderedDict

with open('js/data.json') as json_data:
    data = json.load(json_data, object_pairs_hook=OrderedDict)

result = {}

for src in data.keys():
    for dest in data.keys():
        if src < dest and "duration" not in data[src][dest]:
            url = f"https://www.myrapid.com.my/clients/Myrapid_Prasarana_37CB56E7-2301-4302-9B98-DFC127DD17E9/api/prasarana_planner.ashx?action=list_planner&flng={data[src]['lon']}&flat={data[src]['lat']}&tlng={data[dest]['lon']}&tlat={data[dest]['lat']}"
            print(url)
            # Chrome user agent string
            head = {"Content-Type": "application/json",
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
            response = requests.get(url, headers=head)
            response_json = response.json()
            try:
                data[src][dest]["duration"] = int(
                    int(response_json[0]["a"][0]["t_duration"])/60)
            except:
                print(src + " : " + dest)
                print(data[src]["name"] + " : " + data[dest]["name"])
                print(url)
                pass

with open('result.json', 'w') as fp:
    json.dump(data, fp, indent=4)
