#!venv/bin/python
import importlib
import os
import time

from flask import Flask, jsonify, request

from backend import ImageData, PATH_TO_IMAGES

if not os.path.exists(PATH_TO_IMAGES):
    os.makedirs(PATH_TO_IMAGES)
    print("Starting loading images")
    importlib.import_module('load-images')
    print("Images loaded")
else:
    print("Images already downloaded to the disk")

image_data = ImageData()

app = Flask(__name__)

@app.route('/api/v1.0/get-points/<userId>', methods=['GET'])
def get_points(userId):
    return jsonify({'points': 178})


@app.route('/api/v1.0/check-location/<lng>/<lat>', methods=['GET'])
def check_location(lng, lat):
    challenge_id, encoded_img = image_data.get_image_for_location(lng, lat)
    if encoded_img is not None:
        return jsonify({"found": 1, "image": encoded_img, "challengeId": challenge_id})
    else:
        return jsonify({"found": 0})

@app.route('/api/v1.0/submit-challenge-photo', methods=['POST'])
def submit_challenge_photo():
    time.sleep(7)
    encoded_image = request.json["img"]
    challenge_id = request.json["challengeId"]
    result = image_data.compare_images(image_data.challenges[challenge_id], encoded_image)
    return jsonify({"challengeId": challenge_id, "points": result})


if __name__ == '__main__':
    app.run(debug=True)
