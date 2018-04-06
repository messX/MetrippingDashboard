import pygeohash as pgh
import json
with open('cluster-plots.json', 'r') as f:
    full_data=json.load(f)['json']

for pt in full_data:
    pt['geohash'] = pgh.encode(float(pt['lng']), float(pt['lat']), 2)

with open('cluster-plots-new.json', 'w') as fw:
    full_data=json.dump(full_data, fw)

