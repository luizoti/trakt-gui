#!/usr/bin/env python3

import json

try:
    from API.apibase import get
    from API.apikeys import tmdb
    from API.cache import Cache
except Exception as e:
    from apibase import get
    from apikeys import tmdb
    from cache import Cache
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
    'show_ep'    : ['/tv/', '', 'season/', '', '/episode/', '', '/images']
}


headers = {
    'Content-Type': 'application/json;charset=utf-8',
}


def config(img_type, file): # Future update a persistent mecanism with timer count to rerun in X space of days
    _dict = {
        'backdrop_path': ['backdrop_sizes', 'w780'],
        'poster_path': ['poster_sizes', 'w500'],
        'logo_path': ['logo_sizes', 'w185'],
    }

    try:
        cfg = json.loads(get(tmdb['APIURL'], ''.join([TYPES['config'], tmdb['apikey']]), headers).content)
    except Exception as e:
        raise e

    _type = cfg['images'][_dict[img_type][0]]
    size = _dict[img_type][1]

    if size in _type:
        return ''.join([cfg['images']['secure_base_url'], size, file])
        pass


def GetData(_type, _id, season_number=None, episode_number=None, lang='en-US'):
    ch = Cache(_id)
    method_list = TYPES[_type]
    method = method_list[1] = _id

    if _type == 'show_season' or 'show_ep':
        if season_number != None:
            method = method_list[3] = season_number
            pass
    elif _type == 'show_ep':
        if episode_number != None:
            method = method_list[5] = episode_number
            pass
        pass

    try:
        if ch.isOnCache() is True:
            return ch.returnCache()
        else:
            return ch.doCache(json.loads(get(tmdb['APIURL'], ''.join([''.join(method_list), '?api_key=', tmdb['apikey'], '&language=', lang]), headers=headers).content))
            pass
    except Exception as e:
        raise e