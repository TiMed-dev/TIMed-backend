#!/usr/bin/env python

import os
import sys
import routes
import logging
import coloredlogs
import numpy as np
import tornado.web
import tornado.ioloop
import psycopg2.extras
import db.dbconn as db
from tornado import gen
import tornado.platform.twisted
tornado.platform.twisted.install()
from toradbapi import ConnectionPool
from twisted.internet import reactor


USER = 'airinfo'
PASSWORD = 'password(8)'
DATABASE = 'flights'
HOST = 'margffoy-tuay.com'

LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(name) -30s %(funcName) '
              '-35s %(lineno) -5d: %(message)s')
LOGGER = logging.getLogger(__name__)
coloredlogs.install(level='info')

clr = 'clear'
if os.name == 'nt':
    clr = 'cls'


def main():
    logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)
    settings = {}
    # settings = {"static_path": os.path.join(
        # os.path.dirname(__file__), "static")}
    application = tornado.web.Application(routes.ROUTES,
                                          debug=True, serve_traceback=True, autoreload=True, **settings)
    print "Server is now at: 127.0.0.1:8000"
    ioloop = tornado.ioloop.IOLoop.instance()
    db.initialize_db('psycopg2', cp_noisy=True, user=USER, password=PASSWORD,
                     database=DATABASE, host=HOST, cursor_factory=psycopg2.extras.DictCursor)

    W = np.load('./nn/W_partial.npz')['arr_0']
    application.W = W
    application.db = db
    application.listen(8000)
    try:
        ioloop.start()
    except KeyboardInterrupt:
        pass
    finally:
        print "Closing server...\n"
        db.close()
        tornado.ioloop.IOLoop.instance().stop()

if __name__ == '__main__':
    os.system(clr)
    main()
