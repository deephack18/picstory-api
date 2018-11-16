import json
import threading

import geopy

import imageproc

PATH_TO_DATA = "data.json"
PATH_TO_IMAGES = "images"

DISTANCE_IN_KM_TO_CONSIDER_CLOSE = 1

import base64

class ImageData(object):
    def __init__(self):
        self.counter = 0
        with open(PATH_TO_DATA, 'r') as f:
            self.image_data = json.load(f)
        self.challenges = {}
        print(self.image_data['docs'][0])
        with open('points', 'r') as f:
            self.points = int(f.readline())


    def __get_next_counter(self):
        with threading.Lock():
            self.counter += 1
            return self.counter

    def get_image_for_location(self, lng, lat):
        for img_data in self.image_data['docs']:
            if geopy.distance.distance(*img_data['CP_geo'], (lng, lat)).km < DISTANCE_IN_KM_TO_CONSIDER_CLOSE:
                with open(f'{PATH_TO_IMAGES}/{img_data["B1p"]}', "rb") as image_file:
                    encoded_img = base64.b64encode(image_file.read())
                    challenge_id = self.__get_next_counter()
                    self.challenges[challenge_id] = {encoded_img}
                    return challenge_id, encoded_img
        return None

    def __save_points(self):
        with open('points', 'w') as f:
            f.write(self.points)

    def compare_images(self, img1, img2):
        result = imageproc.compare_images(img1, img2)
        self.points += result
        self.__save_points()