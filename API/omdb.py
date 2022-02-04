import json

try:
    from API.apibase import get
except Exception as e:
    from apibase import get
    pass

omdb = {
    'APIURL': 'http://www.omdbapi.com/?i=',
    'apikey': '',
}

headers = {
    'Content-Type': 'application/json;charset=utf-8',
}


def omdbData(_id):
    try:
        return get(omdb['APIURL'], ''.join([_id, "&apikey=", omdb['apikey'], "&plot=full"]), headers)
    except Exception as e:
        raise e

# print(omdbData('tt0114168'))