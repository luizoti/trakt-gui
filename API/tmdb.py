#!/usr/bin/env python3

import json

try:
    from API.apibase import get
    from API.apikeys import tmdb
except Exception as e:
    from apibase import get
    from apikeys import tmdb
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


def config(): # Future update a persistent mecanism with timer count to rerun in X space of days
    try:
       return json.loads(get(tmdb['APIURL'], ''.join([TYPES['config'], tmdb['apikey']]), headers).content)
    except Exception as e:
        raise e


def GetData(_type, _id, season_number=None, episode_number=None, lang='en-US'):
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
        return json.loads(get(tmdb['APIURL'], ''.join([''.join(method_list), '?api_key=', tmdb['apikey'], '&language=', lang]), headers=headers).content)
    except Exception as e:
        raise e