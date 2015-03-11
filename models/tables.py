# -*- coding: utf-8 -*-
from datetime import datetime


def get_first_name():
    name = 'Nobody'
    if auth.user:
        name = auth.user.first_name
    return name

db.define_table('stocktrader2',
                Field('name'),
                Field('user_id', db.auth_user),
                Field('email'),
                Field('date_posted', 'datetime'),
                Field('money'),
                Field('stocks_owned'),
                Field('sold', 'boolean'),
                Field('image', 'upload', default=''),
                format = '%(title)s',
                )

db.stocktrader2.id.readable = False
db.stocktrader2.name.default = get_first_name()
db.stocktrader2.name.writable = False
db.stocktrader2.user_id.default = auth.user_id
db.stocktrader2.user_id.writable = db.stocktrader2.user_id.readable = False
db.stocktrader2.email.requires = IS_EMAIL()
db.stocktrader2.date_posted.default = datetime.utcnow()
db.stocktrader2.date_posted.writable = False
#db.stocktrader.money.requires = IS_FLOAT_IN_RANGE(0, 100000.0, error_message='The price should be in the range 0..100000')
db.stocktrader2.money.default = 10000
db.stocktrader2.sold.default = False
db.stocktrader2.sold.required = True

db.define_table('stocks2',
                Field('name'),
                Field('price'),
                Field('date_posted', 'datetime'),
                )
db.stocks2.date_posted.default = datetime.utcnow()
