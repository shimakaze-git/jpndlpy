#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' JapanNdlClient
Python wrapper for Japan National Dict Library API
Details: http://iss.ndl.go.jp/information/api/
created by @shimakaze-git
'''
from .validator import SearchTextSchema
from .client_base import JapanNdlClientBase


class JapanNdlClient(JapanNdlClientBase):
    ''' Client for JP NDL API v2
    '''

    def __init__(self):
        self.search_text_schema = SearchTextSchema()
        self.response = None

    def search_text(
        self,
        # dpid=None,
        # dpgroupid=None,
        # title="",
        # creator=None,
        # digitized_publisher=None,
        # ndc=None,
        # from_date=None,
        # until_date=None,
        # cnt=500,
        # idx=1,
        # isbn=str,
        # mediatype=1,
        *args,
        **kwargs
    ):
        """
        OpenSearchに対して検索処理を行う

        Parameters
        ----------
        dpid : str
            データプロバイダID
        dpgroupid : str
            データプロバイダグループID
        any : str
            すべての項目を対象に検索
        title : str
            タイトル
        creator : str
            作成者
        publisher : str
            出版社
        digitized_publisher : str
            デジタル化した製作者
        ndc : str
            分類（NDC）
        from_date : str
            開始出版年月日（YYYY、YYYY-MM、YYYY-MM-DD）
        until_date : str
            終了出版年月日（YYYY、YYYY-MM、YYYY-MM-DD）
        cnt : int
            出力レコード上限値（省略時は200 とする）
        idx : int
            レコード取得開始位置（省略時は1 とする）
        isbn : str
            ISBN
            10 桁または13 桁で入力した場合は、10 桁、13 桁
            の両方に変換して完全一致検索を行う。
            それ以外の桁で入力した場合は前方一致検索を行う
        mediatype : int
            資料種別
            国立国会図書館サーチの詳細検索の資料種別に対応
            “1”：本
            “2”：記事・論文
            “3”：新聞
            “4”：児童書
            “5”：レファレンス情報
            “6”：デジタル資料
            “7”：その他
            “8”：障害者向け資料（障害者向け検索対象資料）
            “9”：立法情報

        Returns
        -------
        items : json
            複数の図書情報
        """

        data, errs = self.search_text_schema.load(kwargs)
        if not errs:
            serialize_params = self.serializer(data)
            self.response = self.get(serialize_params)
            return self.response
        else:
            erros_mes = ''.join(
                [key + ':' + errs[key][0] + '\n' for key in errs]
            )
            raise Exception(erros_mes)

    @property
    def search_title(self):
        ''' Returns text of search
        '''
        return self.response._title

    @property
    def search_link(self):
        ''' Returns link of search
        '''
        return self.response._link

    @property
    def search_language(self):
        ''' Returns language of search
        '''
        return self.response._language

    @property
    def search_total_results(self):
        ''' Returns total_results of search
        '''
        return self.response._total_results

    @property
    def search_start_index(self):
        ''' Returns start_index of search
        '''
        return self.response._start_index

    @property
    def search_items_per_page(self):
        ''' Returns items_per_page of search
        '''
        return self.response._items_per_page
