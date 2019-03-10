#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from jpndlpy.validator import SearchTextSchema


class JondlpyValidatorTest(unittest.TestCase):

    def setUp(self):
        self.search_text_schema = SearchTextSchema()

    def test_search_text_schema(self):
        title = "python"
        cnt = 2

        params_dict = {
            "title": title,
            "cnt": cnt
        }

        data, errs = self.search_text_schema.load(params_dict)
        self.assertEqual(type(data), dict)
        self.assertEqual(data, params_dict)

    def test_search_from_date_schema(self):
        title = "python"
        cnt = 2
        from_date = "2018-1-22"

        params_dict = {
            "title": title,
            "cnt": cnt,
            "from_date": from_date
        }

        data, errs = self.search_text_schema.load(params_dict)
        self.assertEqual(type(data), dict)
        self.assertEqual(data, params_dict)

    def test_error_from_date_schema(self):
        title = "python"
        cnt = 2
        from_date = "2018-1*22"

        params_dict = {
            "title": title,
            "cnt": cnt,
            "from_date": from_date
        }

        data, errs = self.search_text_schema.load(params_dict)
        self.assertEqual(
            errs,
            {
                "from_date": [
                    'from_date is not date type'
                ]
            }
        )

if __name__ == "__main__":
    unittest.main()
