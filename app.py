#!venv/bin/python
from flask import Flask, jsonify

from backend import ImageData

app = Flask(__name__)

image_data = None

@app.route('/api/v1.0/get-points/<user_id>', methods=['GET'])
def get_points(user_id):
    return jsonify({'points': 178})


@app.route('/api/v1.0/check-location/<lng>/<lat>', methods=['GET'])
def cehck_location(lng, lat):
    return image_data.get_image_for_location(lng, lat)


if __name__ == '__main__':
    image_data = ImageData()
    app.run(debug=True)
