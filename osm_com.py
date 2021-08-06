import matplotlib.pyplot as plt  # Collect coords into list
import requests
from PIL import Image
import json
# node["name"~".*"] 56.206010,47.229596,56.210534,47.245893
import pandas as pd
import numpy as np

overpass_url = "http://overpass-api.de/api/interpreter"

overpass_query = """
[out:json];
way["building"~".*"](55.609696,47.410604,55.614289,47.426901);
(._;>;);
out;

"""

# overpass_query = """
# [out:json];
# (node["amenity"="building"](55.808945,49.086185,55.814660,49.106655);
#  way["amenity"="building"](55.808945,49.086185,55.814660,49.106655);
#  rel["amenity"="building"](55.808945,49.086185,55.814660,49.106655);
# );
# out;
# """


response = requests.get(overpass_url,
                        params={'data': overpass_query})
data = response.json()

coords = []
for element in data['elements']:
  if element['type'] == 'node':
    lon = element['lon']
    lat = element['lat']
    coords.append((lon, lat))
  elif 'center' in element:
    lon = element['center']['lon']
    lat = element['center']['lat']
    coords.append((lon, lat))

# plt.imshow(img, extent=[56.018145,48.383038,56.020987,48.393273])

