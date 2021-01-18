from flask import Flask, jsonify, request
from flaskr.instagram import follower_count
from flaskr.ukr_passport import latest_passport_status
from flaskr.tiktok import tiktok_followers

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/instagram/followerCount/')
@app.route('/instagram/followerCount/<username>')
def insta_follower_count(username=None):
    print(request.args.get('username'))
    print(username)
    print(username or request.args.get('username'))

    return jsonify(
        {
            'frames': [
                {
                    # https://developer.lametric.com/icons
                    'icon': 'i8649',
                    'text': str(follower_count(username or request.args.get('username')))
                }
            ]
        })


@app.route('/ua-passport/last-status/<code>')
def last_passport_status(code):
    response = latest_passport_status(code)

    if response['days'] == 1:
        days_word = 'день'
    elif 1 < response['days'] < 5:
        days_word = 'дні'
    else:
        days_word = 'днів'

    return jsonify(
        {
            'frames': [
                {
                    'icon': 'i39634',
                    'text': response['status']
                },
                {
                    'icon': 'a8702',
                    'text': str(response['days']) + ' ' + days_word
                }
            ]
        })


@app.route('/tiktok/followers/')
@app.route('/tiktok/followers/<username>')
def get_tiktok_followers(username=None):
    response = tiktok_followers(username or request.args.get('username'))

    return jsonify(
        {
            'frames': [
                {
                    'icon': 'i35685',
                    'text': str(response)
                }
            ]
        })