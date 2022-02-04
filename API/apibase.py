import requests
import json


def get(url, method, headers):
    try:
        return requests.get(''.join([url, method]), headers=headers)
    except Exception as e:
        raise e
    pass


def post(url, method, headers, data):
    try:
        return requests.post(''.join([url, method]), headers=headers, data=json.dumps(data))
    except Exception as e:
        raise e
    pass
