import requests
import json


def latest_passport_status(code):
    response = requests.get('http://passport.mfa.gov.ua/Home/CurrentSessionStatus?sessionId=' + str(code))
    data = json.loads(response.text)
    return sorted(data['StatusInfo'], key=lambda item: item['StatusDateUF'])[-1]['StatusName']
