from API.apibase import post
from API.apikeys import trakt


class LoginTrakt():
    def __init__(self):
        self.TYPES = {
                'getcode'  : '/oauth/device/code',
                'checkauth': '/oauth/device/token',
                }

        self.headers = {
            'Content-Type': 'application/json',
        }


    def GetCode(self, username):
        METHOD = ''.join([self.TYPES['getcode']])
        return post(trakt['APIURL'], METHOD, self.headers, {'client_id': trakt['client_id']})


    def CheckAuth(self, code):
        METHOD = ''.join([self.TYPES['checkauth']])

        data = {
          "code": code,
          "client_id": trakt['client_id'],
          "client_secret": trakt['client_secret']
        }
        return post(trakt['APIURL'], METHOD, self.headers, data=data).status_code