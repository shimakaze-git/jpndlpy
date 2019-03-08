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

    def to_json(self):
        return {
            'title': self._title,
            'link': self._link,
            'author': self._author,
            'category': self._category,
            'guid': self._guid,
            'pubDate': self._pubDate
        }
