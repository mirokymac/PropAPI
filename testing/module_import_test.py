# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 22:25:34 2018

@author: Zihao.MAI
"""
PATH_TO_REFPROP_LIB = 'D:\\REFPROP'
from common.postimport import when_imported

@when_imported('CoolProp.CoolProp')
def test1(mod):
    print('hello cp')
    
@when_imported('CoolProp.CoolProp')
def test2(mod):
    try:
        mod.set_config_string(mod.ALTERNATIVE_REFPROP_PATH,
                              PATH_TO_REFPROP_LIB)
        print(mod.get_global_param_string('REFPROP_version'))
    except:
        print('oops')
    
import CoolProp.CoolProp as cp

print(cp.get_global_param_string('REFPROP_version'))