# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 13:50:30 2018

@author: Zihao.MAI
"""

from flask_restful import fields, marshal_with

test_fields ={
        'a': fields.Float,
        'c': fields.Integer
        }

@marshal_with(test_fields)
def get():
    return {'a':3.0, 'b':'foo', 'c': 2.0}

@marshal_with(test_fields)
def get2():
    return {'a':3.0}