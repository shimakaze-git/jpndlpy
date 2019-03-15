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
        params: dict
    ):
        """ initialize with requests.Request

        Args:
            url (str): 文字列型のURL
            params (dict): 辞書型のGETパラメーター
        """
        self.__url = url
        self.__params = params

        self.__response = None

    def execute(self):
        """ リクエストを開始する
        """
        method = "GET"
        print(self.__params)
        self.__response = requests.request(
            method=method,
            url=self.__url,
            params=self.__params
        )

    @property
    def response(self)->object:
        """ レスポンスを返す

        Raises:
            RequestException: statusがFalseだった際に起こる例外

        Returns:
            object: 'requests.models.Response'のオブジェクト
        """
        if self.status:
            return self.__response
        else:
            exception_mes = "The request failed. You can not return a response."
            raise RequestException(exception_mes)

    @property
    def status(self)->bool:
        """ requestが成功したかどうかの状態を返す

        Returns:
            bool: True or False
        """
        if self.__response is None:
            return False

        if self.__response.ok:
            return True

        return False
