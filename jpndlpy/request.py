#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' jpndlpy.JapanNdlRequest
handling JapanNdlClient request
created by @shimakaze-git
'''
import requests
from requests import RequestException


class JapanNdlRequest():
    ''' Wrap requests.Request
    '''

    def __init__(
        self,
        url: str,
        params: str
    ):
        ''' initialize with requests.Request
        '''
        self.__url = url
        self.__params = params

        self.__response = None

    def execute(self):
        method = "GET"
        self.__response = requests.request(
            method=method,
            url=self.__url,
            params=self.__params
        )

    @property
    def response(self):
        if self.status:
            return self.__response
        else:
            exception_mes = "The request failed. You can not return a response."
            raise RequestException(exception_mes)

    @property
    def status(self):
        if self.__response is None:
            return False

        if self.__response.ok:
            return True

        return False
