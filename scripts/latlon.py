# [1]b.routes["0"].legs["0"].duration, ["0"].a["0"].t_duration

# results["].geometry.coordinates
import json
from collections import OrderedDict

with open('js/data.json') as json_data:
    data = json.load(json_data)

result = OrderedDict()
for i in sorted(data.keys(), reverse=True):
    result[i] = data[i]

with open('result.json', 'w') as fp:
    json.dump(result, fp, indent=4)
