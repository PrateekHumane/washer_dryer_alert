import requests
import json

class pushbullet:
    def __init__(self,api_key):
        self.api_key = api_key

    def send_alert(self, message):
        payload = {'type':'note','title':'washing machine alert','body':message}
        header = {'Access-Token': self.api_key}
        requests.post('https://api.pushbullet.com/v2/pushes',data=payload,headers=header)

