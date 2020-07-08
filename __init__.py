from flask import Flask, jsonify
from .instagram import follower_count

app = Flask(__name__)


@app.route('/instagram/followerCount/terpuhlabs_ua')
def hello_world():
    return jsonify({'instagramFollowerCount': follower_count()})

