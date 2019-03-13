#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' JapanNdlClientBase
Python wrapper for Japan National Dict Library API
Details: http://iss.ndl.go.jp/information/api/
created by @shimakaze-git
'''

from .request import JapanNdlRequest
from .exceptions import JapanNdlException
from .response import JapanNdlResponse


class JapanNdlClientBase:

    HOST = 'iss.ndl.go.jp/api/opensearch'
    ACCEPT = 'application/json'

    @property
    def api_url(self):
        return 'https://{}?'.format(self.HOST)

    def _request(self, url, params=None):
        ''' requests process
        '''
        request_object = JapanNdlRequest(
            url=url,
            params=params
        )
        request_object.execute()

        response = request_object.response
        if request_object.status:
            return JapanNdlResponse(response)

    def request(self, params=None):
        url = self.api_url
        return self._request(url, params)

    def get(self, params=None):
        ''' get request
        >>> client.get('/users/petitviolet').status
        200
        '''
        return self.request(params)
