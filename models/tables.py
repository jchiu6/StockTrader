# -*- coding: utf-8 -*-
from datetime import datetime


def get_first_name():
    name = 'Nobody'
    if auth.user:
        name = auth.user.first_name
    return name

CATEGORY = ['Car', 'Bike', 'Books', 'Music', 'Outdoors', 'For the House', 'Misc']


db.define_table('stocktrader',
                Field('name'),
                Field('user_id', db.auth_user),
                Field('phone'),
                Field('email'),
                Field('category'),
                Field('date_posted', 'datetime'),
                Field('title'),
                Field('price'),
                Field('sold', 'boolean'),
                Field('bbmessage', 'text'),
                Field('image', 'upload', default=''),
                format = '%(title)s',
                )

db.stocktrader.id.readable = False
db.stocktrader.bbmessage.label = 'Message'
db.stocktrader.name.default = get_first_name()
db.stocktrader.date_posted.default = datetime.utcnow()
db.stocktrader.name.writable = False
db.stocktrader.date_posted.writable = False
db.stocktrader.user_id.default = auth.user_id
db.stocktrader.user_id.writable = db.stocktrader.user_id.readable = False
db.stocktrader.email.requires = IS_EMAIL()
db.stocktrader.category.requires = IS_IN_SET(CATEGORY, zero = None)
db.stocktrader.category.default = 'Misc'
db.stocktrader.category.required = True
db.stocktrader.phone.requires = IS_MATCH('^1?((-)\d{3}-?|\(\d{3}\))\d{3}-?\d{4}$',
         error_message='not a phone number')
db.stocktrader.price.requires = IS_FLOAT_IN_RANGE(0, 100000.0, error_message='The price should be in the range 0..100000')
db.stocktrader.sold.default = False
db.stocktrader.sold.required = True
