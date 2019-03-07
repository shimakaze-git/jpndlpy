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
    from_date = fields.String()
    until_date = fields.String()
    cnt = fields.Integer()
    idx = fields.Integer()
    isbn = fields.String()
    mediatype = fields.Integer(
        validate=lambda n: 1 <= n <= 9
    )

    @validates('from_date')
    def validate_from_date(self, value):
        # YYYY、YYYY-MM、YYYY-MM-DD
        value_list = value.split('-')

        try:
            for i, date in enumerate(value_list):
                if i == 0:
                    year = int(date)
                    if not (1970 <= year <= 9999):
                        raise ValidationError('from_date year is not date type')
                elif i == 1:
                    month = int(date)
                    if not (1 <= month <= 12):
                        raise ValidationError('from_date month is not date type')
                elif i == 2:
                    day = int(date)
                    if not (1 <= day <= 31):
                        raise ValidationError('from_date day is not date type')
        except Exception:
            raise ValidationError('from_date is not date type')

    @validates('until_date')
    def validate_until_date(self, value):
        # YYYY、YYYY-MM、YYYY-MM-DD
        value_list = value.split('-')

        try:
            for i, date in enumerate(value_list):
                if i == 0:
                    year = int(date)
                    if not (1970 <= year <= 9999):
                        raise ValidationError('until_date year is not date type')
                elif i == 1:
                    month = int(date)
                    if not (1 <= month <= 12):
                        raise ValidationError('until_date month is not date type')
                elif i == 2:
                    day = int(date)
                    if not (1 <= day <= 31):
                        raise ValidationError('until_date day is not date type')
        except Exception:
            raise ValidationError('until_date is not date type')