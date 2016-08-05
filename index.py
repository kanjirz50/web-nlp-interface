# -*- coding: utf-8 -*-

import sys
import os
# add libs path
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'libs'))

from bottle import route, static_file, default_app
from app.controllers import *


# static files routing
@route('/static/<filepath:path>')
def static(filepath):
    return static_file(filepath, root='./static/')

## bottle単品で動かしたい場合
from bottle import run
run(host='localhost', port=8080, debug=True, reloader=True)

## gunicornを使う場合
#app = default_app()
