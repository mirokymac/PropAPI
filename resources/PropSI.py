# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 22:18:40 2018

@author: Zihao.MAI
"""

PATH_TO_REFPROP = 'd:\\REFPROP'
REFPROP_READY = False

from ..common.postimport import when_imported
@when_imported('CoolProp.CoolProp')
def setup_RPPath(mod):
    mod.set_config_string(5, PATH_TO_REFPROP)
    try:
        mod.PropsSI('H', 'P', 101325, 'Q', 1, 'REFPROP::Water')
    except:
        REFPROP_READY = False
    finally:
        REFPROP_READY = True


import CoolProp.CoolProp as cp
from flask_restful import Resource

class PropSI(Resource):
    def get(self):
        pass