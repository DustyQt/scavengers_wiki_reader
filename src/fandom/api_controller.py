import requests
import os

BOT_USER = os.environ['BOT_USER']
BOT_PASS = os.environ['BOT_PASS']
URL = os.environ['URL']


class ApiController():
    def __init__(self):
        self.session = requests.Session()
        self.login_token = self.get_login_token()
        self.login()
        self.csfr_token = self.get_csrf_token()

    def get_login_token(self):
        data = {
            "action": "query",
            "meta": "tokens",
            "type": "login",
            "format": "json"
        }
        print('getting login token')
        return self.session.post(URL, data).json()['query']['tokens']['logintoken']

    def login(self):
        data = {
            "action": "login",
            "lgname": BOT_USER,
            "lgpassword": BOT_PASS,
            "lgtoken": self.login_token,
            "format": "json"
        }
        print('logging')
        response = self.session.post(URL, data)
        print(response.content)

    def get_csrf_token(self):
        data = {
            "action": "query",
            "meta": "tokens",
            "format": "json"
        }
        response = self.session.post(URL, data=data)
        token = response.json()['query']['tokens']['csrftoken']
        print(token)
        return token

    def create_page(self, title, content):
        data = {
            'action': 'edit',
            'format': 'json',
            'title': title,
            'text': content,
            'summary': 'test summary',
            'bot': True,
            'token': self.csfr_token,
        }
        print(data)
        return self.session.post(URL, data=data)
