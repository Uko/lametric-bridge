from flask import Flask, jsonify
from flaskr.instagram import follower_count

app = Flask(__name__)


@app.route('/instagram/followerCount/<username>')
def instaFollowerCount(username):
    return jsonify({'instagramFollowerCount': follower_count(username)})

