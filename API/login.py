from apibase import post
from apikeys import trakt


TYPES = {
        'getcode'  : '/oauth/device/code',
        'checkauth': '/oauth/device/token',
        }

headers = {
    'Content-Type': 'application/json',
}


def GetCode(username):
    METHOD = ''.join([TYPES['getcode']])
    return post(trakt['APIURL'], METHOD, headers, {'client_id': trakt['client_id']})


def CheckAuth(code):
    METHOD = ''.join([TYPES['checkauth']])

    data = {
      "code": code,
      "client_id": trakt['client_id'],
      "client_secret": trakt['client_secret']
    }
    return post(trakt['APIURL'], METHOD, headers, data=data).status_code