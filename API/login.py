#!/usr/bin/env python3

from __future__ import absolute_import

import sys
import re
import json
import API.apibase as api
from time import sleep
# from os.path import dirname, realpath, join


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
        return api.ApiBase.post(self, METHOD, self.headers, {'client_id': api.keys['client_id']})


    def CheckAuth(self, code):
        METHOD = ''.join([self.TYPES['checkauth']])

        data = {
          "code": code,
          "client_id": api.keys['client_id'],
          "client_secret": api.keys['client_secret']
        }
        return api.ApiBase.post(self, METHOD, self.headers, data=data).status_code

# import sqlite3
# from sqlite3 import Error

# class DataBase():
#     def __init__(self):
#         self.db_file = join(dirname(dirname(realpath(sys.argv[0]))), 'database.db')

#     def create_connection(self):
#         try:
#             _db = sqlite3.connect(self.db_file)
#             print(sqlite3.version)
#         except Error as e:
#             print(e)

#         _db.close()
#         pass

        
# db = DataBase()
# db.create_connection()
# # /home/luiz/trakt-gui-project/trakt-gui/API/database.db            