import requests
import json

keys = {
    'client_id': '1d7cdcd61fb21cc496f115a2918183f1071d3a7f4587fa2348c2610438141bf6',
    'client_secret': 'dd1a0195c253a7db1472ea7b2883711d86792bb27fada694673aeec670d98553',
}

APIURL = 'https://api.trakt.tv'


class ApiBase():
    def get(self, method, headers):
        try:
            return requests.get(''.join([APIURL, method]), headers=headers)
        except Exception as e:
            raise e
        pass


    def post(self, method, headers, data):
        try:                        
            return requests.post(''.join([APIURL, method]), headers=headers, data=json.dumps(data))
        except Exception as e:
            raise e
        pass