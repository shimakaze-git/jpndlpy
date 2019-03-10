#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' jpndlpy Item Entity
created by @shimakaze-git
'''
import json
import re


class ItemEntity:
    """ Item Entity """

    def __init__(self):
        self._title = None
        self._link = None
        self._author = None
        self._category = None
        self._guid = None
        self._pubDate = None

        self._creator = []

    def regist(self, item):
        self._title = item['title'] if 'title' in item else ""
        self._link = item['link'] if 'link' in item else ""

        description = item['description'] if 'description' in item else ""
        self._description = description

        author = item['author'] if 'author' in item else ""
        self._author = [
            author for author in re.split(r',', author) if author != ''
        ]

        self._category = item['category'] if 'category' in item else ''
        self._guid = item['guid'] if 'guid' in item else ''
        self._pubDate = item['pubDate'] if 'pubDate' in item else ''

        self._creator = self.extract_creator(item)

        # print(item['dc:creator'])
        # print(item.keys())
        # print(item['dc:subject'])
        # print(description)
        # print(self._creator)
        # print("--------------------------")

    def extract_creator(self, item):
        ''' 著者を抽出 extract author or creator'''

        creator_list = []
        if 'dc:creator' in item:
            creator_list = item['dc:creator']
        else:
            return ''

        ''' ひらがなの著者名 '''
        creatorTranscription_list = []
        if 'dcndl:creatorTranscription' in item:
            creatorTranscription_list = item[
                'dcndl:creatorTranscription'
            ]

        creator_dicts = []
        for creator, transcription in zip(
            creator_list, creatorTranscription_list
        ):
            creator_dicts.append(
                {
                    'creator': creator,
                    'transcription': transcription
                }
            )
        return creator_dicts

    def extract_identifier(self, item):
        ''' itemの固有の番号情報を抽出 '''
        pass

    def to_json(self):
        return {
            'title': self._title,
            'link': self._link,
            'author': self._author,
            'category': self._category,
            'guid': self._guid,
            'pubDate': self._pubDate,
            'creator': self._creator
        }
