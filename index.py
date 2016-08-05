# -*- coding: utf-8 -*-

import sys
import os
# add libs path
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'libs'))

from bottle import route, static_file, default_app
# load controller files
from app.controllers import *


# static files routing
@route('/static/<filepath:path>')
def static(filepath):
    return static_file(filepath, root='./static/')

## Run with bottle http server.
# from bottle import run
# run(host='localhost', port=8080, debug=True, reloader=True)
# e.g. python index.py

## Run with gunicorn
app = default_app()
# e.g. gunicorn -b 127.0.0.1:8080 -w 1 index:app

## Run with PasteServer
# from bottle import run, PasteServer
# run(server=PasteServer, host='localhost', port=8080, debug=True, reloader=True)
# e.g. python index.py
