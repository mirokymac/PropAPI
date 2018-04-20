# -*- coding: utf-8 -*-

import CoolProp.CoolProp as cp
import os.path as path
import logging

logger = logging.getLogger(__name__)

class PropEngine():
    
    def __init__(self, refprop_path=None):
        _cp = cp
        if refprop_path:
            if path.isdir(refprop_path):
                logger.debug('Trying to load REFPROP library.')
                _cp.set_config_string(_cp.ALTERNATIVE_REFPROP_PATH, path.abspath(refprop_path))
                
                if _cp.get_global_param_string('REFPROP_version'):
                    logger.debug('REFPROP library verified.')
                    _nist_mode = True
                else:
                    logger.debug('REFPROP library invalid. Fail to load.')
                    _nist_mode = False
                    
