#!/usr/bin python
# -*- coding: utf-8 -*-
# Created by tianjun 

from flask import make_response
from flask import jsonify
from flask.ext.httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()


@auth.get_password
def get_password(username):
    if username == 'miguel':
        return 'python'
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)
