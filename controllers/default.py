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
totalPoints = 50
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
    global prev
    values = getRandomDataPy()
    #threading.Timer(1.0, threadingValue).start()

def index():
    global prev
    #print("hello console")
    #values = getRandomDataPy()
    #db.stock.insert(price=values)
    """Better index."""
    # Let's get all data. 
    #posts = db().select(db.stocktrader.ALL)
    #q = db.stocktrader
    
    show_all = request.args(0) == 'all'
    q = (db.stocktrader) if show_all else (db.stocktrader.sold == False)
    
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
    form = SQLFORM.grid(q,
        fields=[db.stocktrader.user_id, db.stocktrader.date_posted, 
                db.stocktrader.category, db.stocktrader.title, 
                db.stocktrader.sold],
        editable=False, deletable=False,
        links=links,
        paginate=5,
        )
    threadingValue()
    return dict(form = form, button = button, values = values, prev = prev)

def index2():
    global data
    prevdb = db(db.stocks).select(orderby=~db.stocks.id).first()
    if prevdb is None:
        prev = 50
    else:
        prev = prevdb.price
        #print("index 2 prevdb.price",prevdb.price)

    y = float(prev) + random.random() * 10 -5
    if y < 0:
        y = 0
    elif y > 100:
        y = 100
    db.stocks.insert(name = "A", price = y)
    z = strftime("%H:%M:%S", gmtime() )
    return dict(y=y, z=z)

#@auth.requires_login()
def add():
    """Add a post."""
    form = SQLFORM(db.stocktrader)
    if form.process().accepted:
        # Successful processing.
        session.flash = T("inserted")
        redirect(URL('default', 'index'))
    return dict(form=form)

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
