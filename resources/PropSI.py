# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 22:18:40 2018

@author: Zihao.MAI
"""

import logging
import common.util
logger = logging.getLogger(__name__)

#==============================================================================
PATH_TO_REFPROP = 'd:\\REFPROP'
REFPROP_READY = False

from common.postimport import when_imported
@when_imported('CoolProp.CoolProp')
def setup_RPPath(mod):
    if PATH_TO_REFPROP:
        mod.set_config_string(5, PATH_TO_REFPROP)
        
    try:
        mod.PropsSI('H', 'P', 101325, 'Q', 1, 'REFPROP::Water')
    except:
        REFPROP_READY = False
    finally:
        REFPROP_READY = True
#==============================================================================

import CoolProp.CoolProp as cp
from flask_restful import Resource, reqparse, fields, marshal_with

#==============================================================================

parser = reqparse.RequestParser()
parser.add_argument('substance',
                    type=str,
                    choices=(SUBS.keys()),
                    required=True)
parser.add_argument('output_type',
                    type=str,
                    choices=(TYPES+('A',)),
                    required=True,
                    help='Output Type out of range.')
parser.add_argument('intype1',
                    type=str,
                    choices=TYPES,
                    required=True,
                    help='Input Type 1 out of range.')
parser.add_argument('invalue1',
                    type=float,
                    required=True)
parser.add_argument('intype2',
                    type=str,
                    choices=TYPES,
                    required=True,
                    help='Input Type 2 out of range.')
parser.add_argument('invalue2',
                    type=float,
                    required=True)
parser.add_argument('extra', nullable=True)

class PropSI(Resource):
    def get(self):
        pass