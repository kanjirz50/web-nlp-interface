# -*- coding: utf-8 -*-

import json
from bottle import route, template, post, get, request, HTTPResponse

import your_tool

@route('/')
def index():
    return template("sample")

@get('/api/analyzer')
def return_analysis_result():
    text = request.query.input_text# .encode("utf-8")

    _text = your_tool.lowercase(text)

    body = json.dumps(_text)
    r = HTTPResponse(status=200, body=body)
    r.set_header('Content-Type', 'application/json')
    return r
