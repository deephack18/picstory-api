import json
import threading
from random import random

import geopy
from geopy import distance

import imageproc
from config import TEST_MODE

PATH_TO_DATA = "data.json"
PATH_TO_TEST_DATA = "data-test.json"
PATH_TO_IMAGES = "images"

DISTANCE_IN_KM_TO_CONSIDER_CLOSE = 1

import base64


class ImageData(object):
    def __init__(self):
        print('Initializing ImageData')
        self.counter = 0
        self.image_data = self.__get_image_data_list(PATH_TO_DATA)
        if TEST_MODE:
            self.image_data.extend(self.__get_image_data_list(PATH_TO_TEST_DATA))
        self.challenges = {}
        with open('points', 'r') as f:
            self.points = int(f.readline())

    def __get_image_data_list(self, file):
        with open(file, 'r') as f:
            self.image_data = json.load(f)
            return self.image_data['docs']

    def __get_next_counter(self):
        with threading.Lock():
            self.counter += 1
            return self.counter

    def get_image_for_location(self, lng, lat):
        print(f'Looking for photo for location: {lng}, {lat}')
        for img_data in self.image_data:
            if 'CP_geo' not in img_data:
                continue
            if distance.distance(*(img_data['CP_geo']), (lng, lat)).km < DISTANCE_IN_KM_TO_CONSIDER_CLOSE:
                with open(f'{PATH_TO_IMAGES}/{img_data["B1p"][0]}', "rb") as image_file:
                    encoded_img = base64.b64encode(image_file.read()).decode()
                    challenge_id = self.__get_next_counter()
                    self.challenges[challenge_id] = encoded_img
                    return challenge_id, encoded_img
        return None, None

    def __save_points(self):
        with open('points', 'w') as f:
            f.write(str(self.points))

    def compare_images(self, img1, img2):
        result = imageproc.compare_images(img1, img2)
        self.points += result
        self.__save_points()
        return result