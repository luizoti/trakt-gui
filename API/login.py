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
    