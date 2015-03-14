# -*- coding: utf-8 -*-
from datetime import datetime


def get_first_name():
    name = 'Nobody'
    if auth.user:
        name = auth.user.first_name
    return name

def get_email():
    email = 'NoEmail'
    if auth.user:
        email = auth.user.email
    return email

db.define_table('stocktrader',
                Field('name'),
                Field('user_id', db.auth_user),
                Field('email', db.auth_user),
                Field('date_posted', 'datetime'),
                Field('money'),
                Field('stock1_shares_owned'),
                Field('stock2_shares_owned'),
                Field('stock3_shares_owned'),
                Field('stock4_shares_owned'),
                format = '%(title)s',
                )
db.stocktrader.stock1_shares_owned.default = 0
db.stocktrader.stock2_shares_owned.default = 0
db.stocktrader.stock3_shares_owned.default = 0
db.stocktrader.stock4_shares_owned.default = 0

db.stocktrader.stock1_shares_owned.writable = False
db.stocktrader.stock2_shares_owned.writable = False
db.stocktrader.stock3_shares_owned.writable = False
db.stocktrader.stock4_shares_owned.writable = False

db.stocktrader.id.readable = False
db.stocktrader.name.default = get_first_name()
#db.stocktrader.name.writable = False
db.stocktrader.user_id.default = auth.user_id
db.stocktrader.user_id.writable = db.stocktrader.user_id.readable = False
db.stocktrader.email.requires = IS_EMAIL()
db.stocktrader.email.default = get_email()
db.stocktrader.date_posted.default = datetime.utcnow()
db.stocktrader.date_posted.writable = False
db.stocktrader.money.writable = False
#db.stocktrader.money.requires = IS_FLOAT_IN_RANGE(0, 100000.0, error_message='The price should be in the range 0..100000')
db.stocktrader.money.default = 10000

db.define_table('stocks',
                Field('name'),
                Field('price'),
                Field('date_posted', 'datetime'),
                )
db.stocks.date_posted.default = datetime.utcnow()

db.define_table('AI',
                Field('name'),
                Field('user_id', db.auth_user),
                Field('date_posted', 'datetime'),
                Field('money'),
                Field('stock1_shares_owned'),
                Field('stock2_shares_owned'),
                Field('stock3_shares_owned'),
                Field('stock4_shares_owned'),
                format = '%(title)s',
                )
db.AI.user_id.default = auth.user_id
db.AI.user_id.writable = db.AI.user_id.readable = False
db.AI.stock1_shares_owned.default = 0
db.AI.stock2_shares_owned.default = 0
db.AI.stock3_shares_owned.default = 0
db.AI.stock4_shares_owned.default = 0
db.AI.money.default = 10000
db.AI.date_posted.default = datetime.utcnow()
