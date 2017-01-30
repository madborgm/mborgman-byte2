#!/usr/bin/env python
#
# Byte 2 Version 2


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

# we are adding a new class that will 
# help us to use jinja. MainHandler will sublclass this new
# class (BaseHandler), and BaseHandler is in charge of subclassing
# webapp2.RequestHandler
class BaseHandler(webapp2.RequestHandler):
    @webapp2.cached_property
    def jinja2(self):
        # Returns a Jinja2 renderer cached in the app registry.
        return jinja2.get_jinja2(app=self.app)
    
    #lets jinja render our response
    def render_response(self, _template, context):
    	values = {'url_for': self.uri_for}
    	
    	logging.info(context)
    	values.update(context)
    	self.response.headers['Content-Type'] = 'text/html'
    	
    	#renders a template and writes the result to the response.
    	try: 
    		rv = self.jinja2.render_template(_template, **values)
			self.response.headers['Content-type'] = 'text/html; charset=utf-8'
			self.response.write(rv)
		except TemplateNotFound:
			self.abort(404)
#			
#class MainHandler(BaseHandler):
#	
#	def get(self): 
#		"""default landing page"""
#		
#		data = self.get_all_data()
#		context = {}
#		
#		self.render_response('index.html', context)
#		
#	def get_all_data(self):
#		"""collect data from the server"""
#		query = "SELECT * FROM " + TABLE_ID + "WHERE "


