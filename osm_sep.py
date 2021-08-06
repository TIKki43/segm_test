import matplotlib.pyplot as plt
import numpy as np
import math
import requests
from io import BytesIO
# import Image
from PIL import Image


def deg2num(lat_deg, lon_deg, zoom):
    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
    return xtile, ytile


def num2deg(xtile, ytile, zoom):
    n = 2.0 ** zoom
    lon_deg = xtile / n * 360.0 - 180.0
    lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
    lat_deg = math.degrees(lat_rad)
    return lat_deg, lon_deg


def getImageCluster(lon_deg, lat_deg, delta_long, delta_lat, zoom):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    smurl = r"http://a.tile.openstreetmap.org/{0}/{1}/{2}.png"
    xmin, ymax = deg2num(lat_deg, lon_deg, zoom)
    xmax, ymin = deg2num(delta_lat, delta_long, zoom)

    Cluster = Image.new('RGB', ((xmax - xmin + 1) * 256 - 1, (ymax - ymin + 1) * 256 - 1))  # x6
    for xtile in range(xmin, xmax + 1):
        for ytile in range(ymin, ymax + 1):
            try:
                imgurl = smurl.format(zoom, xtile, ytile)
                imgstr = requests.get(imgurl, headers=headers)  # head=None
                tile = Image.open(BytesIO(imgstr.content))
                Cluster.paste(tile, box=((xtile - xmin) * 256, (ytile - ymin) * 255))
            except:
                print("Couldn't download image")
                tile = None
    return Cluster


a = getImageCluster(47.229596,56.206010,47.245893,56.210534, 17) # 03/05
common_shape = (np.asarray(a)).shape
h, w, rbg = common_shape
# print(common_shape)
# # print(np.asarray(a))
# print(np.asarray(a).shape)
fig = plt.figure()
fig.patch.set_facecolor('white')
# plt.imshow(np.asarray(a))
# plt.show()
plt.imsave(r'C:\projects\kai_prj\dataset\osm\var.jpg', np.asarray(a))
