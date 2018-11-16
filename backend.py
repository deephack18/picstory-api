import json

import geopy

PATH_TO_DATA = "data.json"
PATH_TO_IMAGES = "images"

DISTANCE_IN_KM_TO_CONSIDER_CLOSE = 1

import base64

class ImageData(object):
    def __init__(self):
        with open(PATH_TO_DATA, 'r') as f:
            self.image_data = json.load(f)
        print(self.image_data['docs'][0])

    def get_image_for_location(self, lng, lat):
        for img_data in self.image_data['docs']:
            if geopy.distance.distance(*img_data['CP_geo'], (lng, lat)).km < DISTANCE_IN_KM_TO_CONSIDER_CLOSE:
                with open(f'{PATH_TO_IMAGES}/{img_data["B1p"]}', "rb") as image_file:
                    return base64.b64encode(image_file.read())
        return None