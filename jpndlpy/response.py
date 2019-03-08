#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' jpndlpy.JapanNdlResponse
handling JapanNdlClient response
created by @shimakaze-git
'''
import re
import xmltodict
import json

# from xml import etree.ElementTree as et
import xml.etree.ElementTree as et

from .item_entity import ItemEntity


class JapanNdlResponse():
    ''' Wrap requests.Response
    '''

    def __init__(self, response):
        ''' initialize with requests.Response
        :params response: instance of requests.Response
        '''
        self.response = response
        self.headers = response.headers
        self.items = []

        self._title = None
        self._link = None
        self._description = None
        self._language = None
        self._total_results = None
        self._start_index = None
        self._items_per_page = None

        """ serialization """
        self.serialize()

    def to_json(self):
        ''' Returns jsonified contents of response
        '''
        return {
            'title': self._title,
            'link': self._link,
            'language': self._language,
            'total_results': self._total_results,
            'start_index': self._start_index,
            'items_per_page': self._items_per_page,
            'items': [
                item.to_json() for item in self.items
            ]
        }

    def serialize(self):
        ''' serialization jsonResponse
        '''
        # root = self.xml_parse()
        root = self.xml_to_dict()

        """ 検索情報を抽出していく """
        self.extract_search_info(root)

        """
        item 要素を抽出していく
        """
        if 'item' in root:
            items = root['item']
            self.extract_items(items)

    def xml_to_dict(self):
        """ xml to dict """
        response = self.response

        dict_items = xmltodict.parse(
            response.text
        )

        enc_items = json.dumps(
            dict_items
            # indent=4
        )
        dec_items = json.loads(
            enc_items
        )['rss']['channel']
        return dec_items

    def extract_search_info(self, root):
        """ extract search info """

        self._title = root['title'].split()[0]
        self._link = root['link']
        self._description = root['description']
        self._language = root['language']

        self._total_results = root['openSearch:totalResults']
        self._start_index = root['openSearch:startIndex']
        self._items_per_page = root['openSearch:itemsPerPage']

    def extract_items(self, items):
        '''
        item情報を抽出する
        '''
        for item in items:
            """ Entity Object """
            item_object = ItemEntity()
            item_object.regist(item)

            self.items.append(item_object)
