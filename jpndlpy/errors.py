# -*- coding: utf-8 -*-
import json


class SearchTextValidationException(Exception):
    def __init__(self, errors):
        self.errors = errors
