import requests
import re
from datetime import datetime


def tiktok_followers(username):
    response = requests.get('https://www.tiktok.com/@' + str(username))

    data = re.search('<strong title=\\"Followers\\">(\\d+)</strong>', response.text).group(1)

    print(data)

    return data
