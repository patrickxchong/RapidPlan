import requests
import json
import csv
import os
from pprint import pprint


def WriteDictToCSV(csv_file, csv_columns, dict_data):
    """Write python dictionary to csv."""
    """From https://www.idiotinside.com/2015/04/14/export-dict-to-csv-list-to-csv-in-python/."""
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError as err:
        print("I/O error: {0}".format(err))
    return


stations = ["KJ17", "KJ35", "S71", "S01", "KJ9", "KJ26", "KJ21", "S69", "S77", "S64", "MRT26", "S63", "MRT8", "S13", "KJ16", "MRT27", "MR6", "MRT16", "MRT28", "S67", "MR8", "S02", "S03", "KJ27", "S08", "S61", "MR10", "MRT18", "KJ8", "KJ12", "KJ7", "KJ1", "S10", "MR4", "MR5", "S74", "KJ6", "MRT31", "KJ11", "MRT2", "KJ24", "KJ18", "S72", "KJ19", "KJ15", "MR1", "KJ10", "MRT5", "MRT3", "MRT4", "KJ25", "MR3", "S06", "MRT19", "S12", "MR9", "BRT2", "MRT15", "S07", "S70",
            "MRT7", "MRT13", "S04", "S05", "KJ14", "MRT14", "MRT10", "S11", "S78", "S79", "S09", "MRT11", "S75", "S81", "S15", "MR7", "S62", "MRT12", "S17", "S18", "KJ5", "BRT6", "S68", "KJ4", "MRT25", "KJ29", "KJ30", "MRT30", "KJ36", "KJ28", "S14", "S65", "MRT1", "MRT29", "BRT4", "BRT5", "BRT3", "BRT1", "MRT6", "KJ32", "KJ23", "MRT23", "KJ20", "KJ2", "MRT21", "MRT22", "KJ22", "S76", "MRT20", "MRT24", "S16", "MR11", "MRT9", "MRT17", "MR2", "KJ34", "KJ31", "BRT7", "KJ3", "KJ33"]
# stations = ["KJ17", "KJ35", "S71"]

result = {}

for src in stations:
    for dest in stations:
        if src < dest:
            url = f"https://www.myrapid.com.my/clients/Myrapid_Prasarana_37CB56E7-2301-4302-9B98-DFC127DD17E9/api/prasarana_rail.ashx?action=list_fare&from={src}&to={dest}"
            print(url)
            # Chrome user agent string
            head = {"Content-Type": "application/json",
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
            response = requests.get(url, headers=head)
            response_json = response.json()
            if src not in result:
                result[src] = {}
            result[src][dest] = response_json

with open('result.json', 'w') as fp:
    json.dump(result, fp)
    
# dir_path = os.path.dirname(os.path.realpath(__file__))
# WriteDictToCSV(dir_path + '/lkm.csv', response_json[0].keys(), response_json)
