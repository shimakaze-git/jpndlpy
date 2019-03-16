#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' SearchText
SearchText is validator for search_text method
Details: https://marshmallow.readthedocs.io/en/latest/quickstart.html
created by @shimakaze-git
'''
from datetime import datetime
from marshmallow import Schema, fields, validates, ValidationError


class SearchTextSchema(Schema):
    dpid = fields.String()
    dpgroupid = fields.String()
    title = fields.String(required=True)
    creator = fields.String()
    digitized_publisher = fields.String()
    ndc = fields.String()
    from_date = fields.String(load_to='from', dump_to='from')
    until_date = fields.String(load_to='until', dump_to='until')
    cnt = fields.Integer(
        validate=lambda n: 1 <= n <= 500
    )
    idx = fields.Integer(
        validate=lambda n: 1 <= n <= 500
    )
    isbn = fields.String()
    mediatype = fields.Method("validate_mediatype")

    def validate_mediatype(self, obj: dict)->str:
        """mediatypeのバリデーションとシリアライズ

        Args:
            obj (dict): リクエストから送られてきた内容の辞書型

        Returns:
            str: mediatypeの文字列型
        """
        if 'mediatype' in obj:
            mediatype = obj['mediatype']

            mediatype_str = ""
            if type(mediatype) is list:
                for i, v in enumerate(mediatype):
                    mediatype_str += '{} '.format(v)
                mediatype_str = mediatype_str.rstrip()

            elif (type(mediatype) is int) and (1 <= mediatype <= 9):
                mediatype_str = str(mediatype_str)
            else:
                # 範囲外の場合は強制的に1に変換する
                mediatype_str = str(1)

            return mediatype_str

    @validates('from_date')
    def validate_from_date(self, value)->None:
        """ form_dateのバリデーションチェック

        Args:
            value ([type]): [description]

        Raises:
            ValidationError: [description]
            ValidationError: [description]
            ValidationError: [description]
            ValidationError: [description]

        Returns:
            None: [description]
        """
        # YYYY, YYYY-MM, YYYY-MM-DD
        value_list = value.split('-')

        try:
            for i, date in enumerate(value_list):
                if i == 0:
                    year = int(date)
                    if not (1970 <= year <= 9999):
                        raise ValidationError(
                            'from_date year is not date type'
                        )
                elif i == 1:
                    month = int(date)
                    if not (1 <= month <= 12):
                        raise ValidationError(
                            'from_date month is not date type'
                        )
                elif i == 2:
                    day = int(date)
                    if not (1 <= day <= 31):
                        raise ValidationError(
                            'from_date day is not date type'
                        )
        except Exception:
            raise ValidationError('from_date is not date type')

    @validates('until_date')
    def validate_until_date(self, value):
        """until_dateのバリデーションチェック

        Args:
            value ([type]): [description]

        Raises:
            ValidationError: [description]
            ValidationError: [description]
            ValidationError: [description]
            ValidationError: [description]
        """
        # YYYY、YYYY-MM、YYYY-MM-DD
        value_list = value.split('-')

        try:
            for i, date in enumerate(value_list):
                if i == 0:
                    year = int(date)
                    if not (1970 <= year <= 9999):
                        raise ValidationError(
                            'until_date year is not date type'
                        )
                elif i == 1:
                    month = int(date)
                    if not (1 <= month <= 12):
                        raise ValidationError(
                            'until_date month is not date type'
                        )
                elif i == 2:
                    day = int(date)
                    if not (1 <= day <= 31):
                        raise ValidationError(
                            'until_date day is not date type'
                        )
        except Exception:
            raise ValidationError('until_date is not date type')
