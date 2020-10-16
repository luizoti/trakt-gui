#!/usr/bin/env python3

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
    'show_ep'    : ['/tv/', '', 'season/', '', '/episode/', '', '/images']
}


headers = {
    'Content-Type': 'application/json;charset=utf-8',
}




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


class Images():
    def __init__(self):
        self.nocov = '/home/luiz/trakt-gui-project/trakt-gui/images/no-cover.jpg'


    def parser(self, img_type, jsdt):
        try:
            return jsdt[img_type]
        except Exception as e:
            return None
            pass


    def config(self, file, img_type):
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


    def returnImg(self, img_type, tmdbid, jsdt):

        try:
            import urllib.request
        except Exception as e:
            raise e

        try:
            file = self.parser(img_type, jsdt)
        except Exception as e:
            raise e

        if file is None:
            if isfile(self.nocov):
                return self.nocov
                pass
            pass
        elif 'no-cover' in file:
            return file
            pass
        else:
            try:
                path = join(cache_path, str(tmdbid), ''.join([img_type, '.', basename(file).split('.')[1]]))
            except Exception as e:
                raise e
            else:
                pass

            if isfile(path):
                return path
            else:
                try:
                    urllib.request.urlretrieve(self.config(file, img_type), path)
                except Exception as e:
                    pass

                if isfile(path):
                    return path
                else:
                    return self.nocov
                    pass
                pass
            pass
        pass