import json
from re import search
from os.path import join, basename, isfile

try:
    from API.apibase import get
    from API.apikeys import tmdb
    from API.cache import Cache, cache_path
except Exception as e:
    from apibase import get
    from apikeys import tmdb
    from cache import Cache, cache_path
    pass


TYPES = {
    'config'     : '/configuration?api_key=',
    'collection' : ['/collection/', '', 'images'],
    'company'    : ['/company/', '', 'images'],
    'movie'      : ['/movie/', '', 'images'],
    'network'    : ['/network/', '', 'images'],
    'person'     : ['/person/', '', 'images'],
    'person_tag' : ['/person/', '', 'tagged_images'],
    'show'       : ['/tv/', '','images'],
    'show_season': ['/tv/', '', 'season/', '', '/images'],
    'episode'    : ['/tv/', '', 'season/', '', '/episode/', '', '/images']
}


headers = {
    'Content-Type': 'application/json;charset=utf-8',
}

def config(_type):
    _dict = {
        'poster':       ['poster_path', 'poster_sizes', 'w500'],
        'background':   ['backdrop_path', 'backdrop_sizes', 'w780'],
        'logo':         ['logo_path', 'logo_sizes', 'w185']
    }

    try:
        return get(tmdb['APIURL'], ''.join([TYPES['config'], tmdb['apikey']]), headers)
    except Exception as e:
        raise e

{'type': 'movie', 'score': 1000, 'movie': {'title': 'Powder', 'year': 1995, 'ids': {'trakt': 7425, 'slug': 'powder-1995', 'imdb': 'tt0114168', 'tmdb': 12665}}}

def GetData(_type, tmdbid, season_number=None, episode_number=None, lang='en-US'):
    return get(tmdb['APIURL'], ''.join([''.join(TYPES[_type]), '?api_key=', tmdb['apikey'], '&language=', lang]), headers=headers)



print(GetData('movie', 666))