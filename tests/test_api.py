import os
import requests
from flask import json
from shorty.api import create_shortlink

class TestApi:
    headers: dict = {
        'Content-type': 'application/json'
    }
        
    def test_create_shortlink_valid_input(self):
        payload: dict = {
            'url':self.dataProvider()['valid_input']['url'],
            'provider': self.dataProvider()['valid_input']['provider']
        }

        response = requests.post(os.getenv("APP_URL")+'/shortlinks', headers=self.headers, json=payload)
        assert json.loads(response.text) == self.dataProvider()['valid_input']['expected']

    def test_create_shortlink_invalid_input_empty_url(self):
        payload: dict = {
            'url':self.dataProvider()['invalid_input_empty_url']['url'],
            'provider': self.dataProvider()['invalid_input_empty_url']['provider']
        }

        response = requests.post(os.getenv("APP_URL")+'/shortlinks', headers=self.headers, json=payload)
        assert json.loads(response.text) == self.dataProvider()['invalid_input_empty_url']['expected']

    def test_create_shortlink_invalid_input_int_url(self):
        payload: dict = {
            'url':self.dataProvider()['invalid_input_int_url']['url'],
            'provider': self.dataProvider()['invalid_input_int_url']['provider']
        }

        response = requests.post(os.getenv("APP_URL")+'/shortlinks', headers=self.headers, json=payload)
        assert json.loads(response.text) == self.dataProvider()['invalid_input_int_url']['expected']

    def test_create_shortlink_invalid_input_int_provider(self):
        payload: dict = {
            'url':self.dataProvider()['invalid_input_int_provider']['url'],
            'provider': self.dataProvider()['invalid_input_int_provider']['provider']
        }

        response = requests.post(os.getenv("APP_URL")+'/shortlinks', headers=self.headers, json=payload)
        assert json.loads(response.text) == self.dataProvider()['invalid_input_int_provider']['expected']    

    def test_create_shortlink_invalid_input_invalid_provider(self):
        payload: dict = {
            'url':self.dataProvider()['invalid_input_invalid_provider']['url'],
            'provider': self.dataProvider()['invalid_input_invalid_provider']['provider']
        }

        response = requests.post(os.getenv("APP_URL")+'/shortlinks', headers=self.headers, json=payload)
        assert json.loads(response.text) == self.dataProvider()['invalid_input_invalid_provider']['expected']        

    @staticmethod
    def dataProvider():
        return {
            'valid_input' : {
                'expected': {
                    'link': "https://bit.ly/3tWLUSJ",
                    'url': "https://google.com",
                },
                'url':'https://google.com',
                'provider': 'Bitly'
            },
            'invalid_input_empty_url' : {
                'expected': {
                    'message': 'You must provide a url!',
                    'success': False
                },
                'url':'',
                'provider': 'Bitly'
            },
            'invalid_input_int_url' : {
                'expected': {
                    'message': 'Url field and provider field must be strings!',
                    'success': False
                },
                'url':1,
                'provider': 'Bitly'
            },
            'invalid_input_int_provider' : {
                'expected': {
                    'message': 'Url field and provider field must be strings!',
                    'success': False
                },
                'url':'https://google.com',
                'provider': 1
            },
            'invalid_input_invalid_provider' : {
                'expected': {
                    "link": "https://bit.ly/3tWLUSJ",
                    "url": "https://google.com"
                },
                'url':'https://google.com',
                'provider': 'test'
            }
        }   
