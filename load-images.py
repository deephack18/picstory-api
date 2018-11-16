import json
import urllib.request

from backend import PATH_TO_DATA, PATH_TO_IMAGES

with open(PATH_TO_DATA, 'r') as f:
    data = json.load(f)
    for doc in data['docs']:
        filename = doc["B1p"][0]
        urllib.request.urlretrieve(doc['B1p_url'][0], f'{PATH_TO_IMAGES}/{filename}')