import requests
import json
from datetime import datetime


def latest_passport_status(code):
    response = requests.get('http://passport.mfa.gov.ua/Home/CurrentSessionStatus?sessionId=' + str(code))
    data = json.loads(response.text)
    latest = sorted(data['StatusInfo'], key=lambda item: item['StatusDateUF'])[-1]

    difference = datetime.utcfromtimestamp(latest['StatusDateUF'] / 1000) - datetime.now()

    return {
        'days': abs(difference.days),
        'status': latest['StatusName']
    }
