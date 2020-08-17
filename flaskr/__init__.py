from flask import Flask, jsonify
from flaskr.instagram import follower_count

app = Flask(__name__)


@app.route('/instagram/followerCount/<username>')
def instaFollowerCount(username):
    return jsonify(
        {
            'frames': [
                {
                    'icon': 'i28441',
                    'text': str(follower_count(username))}
            ]
        })
