# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 14:17:11 2018

@author: zihao.mai
"""

from flask import Flask
from flask_restful import Api
from propAPI.resources.PropSI import PropSI
from propAPI.resources.HAProp import HAProp

import logging
logger = logging.getLogger(__name__)

logging.info('Initializing flask app...')
app = Flask(__name__)
logging.info('Done.')
logging.info('Initializing rest API...')
api = Api(app)

logging.info('Initializing rest API...')
api.add_resource(PropSI, '/propsi')
api.add_resource(HAProp, '/haprop')

logging.info('Done.')