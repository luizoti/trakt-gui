import requests
import json

# https://trakt.tv/oauth/applications/74257


class TraktApi():
    def __init__(self):
        self.client_id = '1d7cdcd61fb21cc496f115a2918183f1071d3a7f4587fa2348c2610438141bf6'
        self.APIURL = 'https://api.trakt.tv'
        self.METHODS = {
            'getcode': '/oauth/device/code',
            'wat_movies': '/sync/watched/movies' # create a method
        }


    def get(self, method):
        try:
            return requests.get(self.APIURL + method, headers={'Content-Type': 'application/json',
                                                                'trakt-api-version': '2',
                                                                 'trakt-api-key': self.client_id})
        except Exception as e:
            raise e
        pass


    def post(self, method, data):
        try:
            return requests.post(self.APIURL + method, headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        except Exception as e:
            raise e
        pass
        


if __name__ == '__main__':
    api = TraktApi()
    # autcode = json.loads(api.post(api.METHODS['getcode'], {'client_id': api.client_id}).content)
    print(api.get(api.METHODS['wat_movies']))
    pass