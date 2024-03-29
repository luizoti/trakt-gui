import json

try:
    from API.apibase import get
    from API.apikeys import trakt
except Exception as e:
    from apibase import get
    from apikeys import trakt


TYPES = {
    'all'        : '/search/all?query=',
    'movie_show' : '/search/movie,show?query=',
    'movie'      : '/search/movie?query=',
    'show'       : '/search/show?query=',
    'episode'    : '/search/episode?query=',
    'person'     : '/search/person?query=',
    'list'       : '/search/list?query=',
}

headers = {
    'Content-Type': 'application/json',
    'trakt-api-version': '2',
    'trakt-api-key': trakt['client_id'],
}


def Search(_type, movie):
    try:
        response = get(trakt['APIURL'], ''.join([TYPES[_type], movie]), headers)

        if response.status_code == 200 and len(json.loads(response.content)) == 0:
            return result
        elif response.status_code == 200 and len(json.loads(response.content)) > 0:
            search = json.loads(response.content)
    except Exception as e:
        raise e
    return search