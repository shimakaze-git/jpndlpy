#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' jpndlpy.JapanNdlRequest
handling JapanNdlClient request
created by @shimakaze-git
'''
import requests
from requests import RequestException
from xml.etree import ElementTree as et


from concurrent.futures import ThreadPoolExecutor


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

        """ httpのGETパラメーターを整形 """
        params_list, request_range = self.params_serialize()

        results = []
        with ThreadPoolExecutor(
            max_workers=2, thread_name_prefix="thread"
        ) as executor:
            for i in request_range:
                results.append(
                    executor.submit(
                        self.request_process,
                        method,
                        params_list[i]
                    )
                )

        self.__response = [r.result() for r in results]

        # self.__response = self.request_process(
        #     method, self.__params
        # )
        # self.__response = [
        #     self.request_process(
        #         method, self.__params
        #     )
        # ]

    def params_serialize(self)->list:
        """ HTTP GETパラメーターを整形
        Returns:
            list: GETパラメーターを含んだ辞書のリスト
        """

        request_range = range(1)
        params_list = []

        # cntが含まれていない場合は500に設定
        cnt = int(self.__params['cnt']) if "cnt" in self.__params else 500

        # cntが300以上なら二つに分割してリクエストするために整形
        # if 300 <= cnt:
        #     request_range = range(2)

        #     for i in range(2):
        #         params = self.__params

        #         ''' 偶数か奇数なのかを判定'''
        #         if cnt % 2 == 0:
        #             # cntの値を二つに分割 500 -> 250
        #             params['cnt'] = int(cnt/2)
        #         else:
        #             params['cnt'] = int(cnt/2) + ((cnt+i) % 2)
        #         params_list.append(params)
        # else:
        #     params = self.__params
        #     params['cnt'] = cnt
        #     params_list.append(
        #         params
        #     )

        params = self.__params
        params['cnt'] = cnt
        params_list.append(
            params
        )

        return params_list, request_range

    def request_process(self, method: str, params: dict)->None:
        """ requestsを使用しての実際にHTTPリクエストを送信する

        Args:
            method (str): HTTP Method
            params (dict): GET parameters

        Returns:
            None: None
        """
        return requests.request(
            method=method,
            url=self.__url,
            params=params
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

        # return all(
        #     [res.ok for res in [self.__response]]
        # )
        return all(
            [res.ok for res in self.__response]
        )

        # if self.__response.ok:
        #     return True

        # return False
