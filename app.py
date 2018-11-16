#!venv/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/get-points/<user_id>', methods=['GET'])
def get_points(user_id):
    return jsonify({'points': 178})

if __name__ == '__main__':
    app.run(debug=True)
