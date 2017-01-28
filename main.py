#!/usr/bin/env python
#
# Byte 2 Version 2
# 
# Copyright 11/2013 Jennifer Mankoff
#
# Licensed under GPL v3 (http://www.gnu.org/licenses/gpl.html)
#

# standard imports you should have already been using
import webapp2
import logging
from webapp2_extras import jinja2
import urllib

# this library is for decoding json responses
from webapp2_extras import json

# this is used for constructing URLs to google's APIS
from apiclient.discovery import build

# this library is for making http requests and so on
import httplib2

# this library helps with statistical calculations
import numpy

# This API key is provided by google as described in the tutorial
API_KEY = 'AIzaSyCxdIfffdjtEW5CHFlMLSGrHpU_oggLDBY'

# This is the table id for the fusion table
TABLE_ID = '1oaLDbRwmrDQGRzzwTglGqSm2q0J-FTEOrOxV0rdu'

# This uses discovery to create an object that can talk to the 
# fusion tables API using the developer key
service = build('fusiontables', 'v1', developerKey=API_KEY)

# this is used for constructing URLs to google's APIS
from googleapiclient.discovery import build



from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
