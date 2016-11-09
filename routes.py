# -*- coding: iso-8859-15 -*-

"""
routes
======

This module establishes and defines the Web Handlers and Websockets
that are associated with a specific URL routing name. New routing
associations must be defined here.

Notes
-----
For more information regarding routing URL and valid regular expressions
visit: http://www.tornadoweb.org/en/stable/guide/structure.html
"""

import os
import sys
import web
import rest
import tornado.web

#Define new rest associations
REST = [
(r"/api/countries(/?([A-Z]{2})?)", rest.countries_rest.MainHandler),
(r'/api/flights', rest.flights_rest.MainHandler),
(r'/api/users', rest.users_rest.MainHandler),
(r'/api/random', rest.random_rest.MainHandler)
]

# Define new web rendering route associations
WEB = [
(r'/', web.main_handler.MainHandler)
]

STATIC = [
    (r'/static/(.*)', tornado.web.StaticFileHandler, {'path':'static'})
]

ROUTES = REST + WEB + STATIC
