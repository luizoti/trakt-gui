#!/usr/bin/env python3

import json
import API.apibase as api


class SearchTrakt():
    def __init__(self):
        self.TYPES = {
            'all'        : '/search/all?query=',
            'movie_show' : '/search/movie,show?query=',
            'movie'      : '/search/movie?query=',
            'show'       : '/search/show?query=',
            'episode'    : '/search/episode?query=',
            'person'     : '/search/person?query=',
            'list'       : '/search/list?query=',
        }

        self.headers = {
            'Content-Type': 'application/json',
            'trakt-api-version': '2',
            'trakt-api-key': api.keys['client_id'],
        }


    def Search(self, _type, movie):
        try: # .content
            response = api.ApiBase.get(self, ''.join([self.TYPES[_type], movie]), self.headers)
            if response.status_code == 200 and len(json.loads(response.content)) == 0:
                result = 0
            elif response.status_code == 200 and len(json.loads(response.content)) > 0:
                result = json.loads(response.content)
                pass
            print(response.status_code)
        except Exception as e:
            raise e
        return result
