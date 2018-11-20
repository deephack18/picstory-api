import json
import urllib.request

from backend import PATH_TO_DATA, PATH_TO_TEST_DATA, PATH_TO_IMAGES
from config import TEST_MODE


def load_images(file):
    with open(file, 'r') as f:
        data = json.load(f)
        for doc in data['docs']:
            filename = doc["B1p"][0]
            urllib.request.urlretrieve(doc['B1p_url'][0], f'{PATH_TO_IMAGES}/{filename}')

load_images(PATH_TO_DATA)
if TEST_MODE:
    load_images(PATH_TO_TEST_DATA)