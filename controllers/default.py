# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - api is an example of Hypermedia API support and access control
#########################################################################

import datetime
import logging
import random
import time
from time import gmtime, strftime
import threading
from socket import *
import json
import os

data = []
totalPoints = 25
values = []
prev = 0

def getRandomDataPy():
    global data
    global values
    global totalPoints
    global prev
    if len(data) > 0:
        data = data[1:1]
    while len(data) < totalPoints:
        prev = data[len(data)-1] if len(data) > 0 else 50
        #y = prev + random.random() * 10 -5
        y=0
        if y < 0:
            y = 0
        elif y > 100:
            y = 100
        data.append(y)
    res = []
    for i in range (0,len(data) ):
         res.append((i,data[i]))
    return res

def threadingValue():
    global values
    values = getRandomDataPy()
    #threading.Timer(1.0, threadingValue).start()

def index():
    #print("hello console")

    """Better index."""
    # Let's get all data. 
    #posts = db().select(db.stocktrader.ALL)
    #q = db.stocktrader
    
    show_all = request.args(0) == 'all'
    q = (db.stocktrader2) if show_all else (db.stocktrader2.sold == False)
    
    if show_all:
        button = A('See unsold', _class='btn', _href=URL('default', 'index'))
    else:
        button = A('See all', _class='btn', _href=URL('default', 'index', args=['all'], user_signature=True))
    
    def generate_del_button(row):
        # If the record is ours, we can delete it.
        b = ''
        if auth.user_id == row.user_id:
            b = A('Delete', _class='btn', _href=URL('default', 'delete', args=[row.id]))
        return b
    
    def generate_edit_button(row):
        # If the record is ours, we can delete it.
        b = ''
        if auth.user_id == row.user_id:
            b = A('Edit', _class='btn', _href=URL('default', 'edit', args=[row.id]))
        return b
    
    def generate_toggle_sold(row):
        # If the record is ours, we can delete it.
        b = ''
        #if auth.user_id == row.user_id:
        b = A('Toggle Sold', _class='btn', _href=URL('default', 'toggle_sold', args=[row.id], user_signature=True))
        return b
    
    def shorten_post(row):
        return row.bbmessage[:10] + '...'
    
    # Creates extra buttons.
    
    links = [
        dict(header='', body = generate_del_button),
        dict(header='', body = generate_edit_button),
        dict(header='', body = generate_toggle_sold),
        ]
    
    start_idx = 1 if show_all else 0
    form = SQLFORM.grid(q, args=request.args[:start_idx])
    
    #if len(request.args) == 0:
        # We are in the main index.
    #    links.append(dict(header='Post', body = shorten_post))
    #    db.stocktrader.bbmessage.readable = False
    
    #db.stocktrader.sold.show_if = (db.stocktrader.sold == True)
#     form = SQLFORM.grid(q,
#         fields=[db.stocktrader2.user_id, db.stocktrader2.date_posted, 
#                 db.stocktrader2.category, db.stocktrader2.title, 
#                 db.stocktrader2.sold],
#         editable=False, deletable=False,
#         links=links,
#         paginate=5,
#         )
    threadingValue()
    return dict( button = button, values = values, prev = prev)

def graphJson():
    prevdb1 = db(db.stocks2.name == "1").select(orderby=~db.stocks2.id).first()
    prevdb2 = db(db.stocks2.name == "2").select(orderby=~db.stocks2.id).first()
    prevdb3 = db(db.stocks2.name == "3").select(orderby=~db.stocks2.id).first()
    prevdb4 = db(db.stocks2.name == "4").select(orderby=~db.stocks2.id).first()
    if prevdb1 is None:
        prev1 = random.randint(0,100)
    else:
        prev1 = prevdb1.price
    if prevdb2 is None:
        prev2 = random.randint(0,100)
    else:
        prev2 = prevdb2.price
    if prevdb3 is None:
        prev3 = random.randint(0,100)
    else:
        prev3 = prevdb3.price
    if prevdb4 is None:
        prev4 = random.randint(0,100)
    else:
        prev4 = prevdb4.price
    g1y = abs(int(prev1) + random.randint(0,10) -5)
    g2y = abs(int(prev2) + random.randint(0,10) -5)
    g3y = abs(int(prev3) + random.randint(0,10) -5)
    g4y = abs(int(prev4) + random.randint(0,10) -5)
    if g1y > 100:
        g1y = 100
    if g2y > 100:
        g2y = 100
    if g3y > 100:
        g3y = 100
    if g4y > 100:
        g4y = 100
    db.stocks2.insert(name = "1", price = g1y)
    db.stocks2.insert(name = "2", price = g2y)
    db.stocks2.insert(name = "3", price = g3y)
    db.stocks2.insert(name = "4", price = g4y)
    z = strftime("%H:%M:%S", gmtime() )
    return dict(g1y = g1y, g2y = g2y, g3y = g3y, g4y = g4y, z=z)

@auth.requires_login()
def add1():
    """Add a post."""
    '''
    get price at current index, subtract from user total, store name in user file. increase current stock value by randint(0,5)
    if user total is neg, dont process anything
    '''
#     form = SQLFORM(db.stocktrader)
#     if form.process().accepted:
#         # Successful processing.
#         session.flash = T("inserted")
#         redirect(URL('default', 'index'))
    return dict()#form=form)

def sell1():
    '''
    get price at current index, add to user total, remove stock name from user file, decrease current stock value by randint (0,5)
    '''
    return dict()
#@auth.requires_login()
def toggle_sold():
     item = db.stocktrader(request.args(0)) or redirect(URL('default', 'index'))
     item.update_record(sold = not item.sold)
     redirect(URL('default', 'index')) # Assuming this is where you want to go

def view():
    """View a post."""
    # p = db(db.stocktrader.id == request.args(0)).select().first()
    p = db.stocktrader(request.args(0)) or redirect(URL('default', 'index'))
    form = SQLFORM(db.stocktrader, record=p, readonly=True)
    # p.name would contain the name of the poster.
    return dict(form=form)

#@auth.requires_login()
def edit():
    """View a post."""
    # p = db(db.stocktrader.id == request.args(0)).select().first()
    p = db.stocktrader(request.args(0)) or redirect(URL('default', 'index'))
    if p.user_id != auth.user_id:
        session.flash = T('Not authorized.')
        redirect(URL('default', 'index'))
    form = SQLFORM(db.stocktrader, record=p)
    if form.process().accepted:
        session.flash = T('Updated')
        redirect(URL('default', 'view', args=[p.id]))
    # p.name would contain the name of the poster.
    return dict(form=form)

#@auth.requires_login()
#@auth.requires_signature()
def delete():
    """Deletes a post."""
    p = db.stocktrader(request.args(0)) or redirect(URL('default', 'index'))
    if p.user_id != auth.user_id:
        session.flash = T('Not authorized.')
        redirect(URL('default', 'index'))
    db(db.stocktrader.id == p.id).delete()
    redirect(URL('default', 'index'))

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

def api():
    """
    this is example of API with access control
    WEB2PY provides Hypermedia API (Collection+JSON) Experimental
    """
    from gluon.contrib.hypermedia import Collection
    rules = {
        '<tablename>': {'GET':{},'POST':{},'PUT':{},'DELETE':{}},
        }
    return Collection(db).process(request,response,rules)
