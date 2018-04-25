# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 22:42:29 2018

@author: Zihao.MAI
"""

import logging
logger = logging.getLogger(__name__)

#==============================================================================
import CoolProp.CoolProp as cp
from flask_restful import Resource, reqparse, fields, marshal_with

TYPES = ('T', # Dry-Bulb temperature
         'B', # Wet-Bulb temperature
         'D', # Dew-Point temperature
         'P', # Pressure
         'V', # Mixture volume
         'R', # Relative humidity
         'W', # Humity ratio
         'H', # Mixture enthalpy
         'S', # Mixture entropy
         'C', # Mixture specific heat
         'M', # Mixture viscosity
         'K') # Mixture thermal conductivity

parser = reqparse.RequestParser()
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
parser.add_argument('intype3',
                    type=str,
                    choices=TYPES,
                    required=True,
                    help='Input Type 3 out of range.')
parser.add_argument('invalue3',
                    type=float,
                    required=True)
parser.add_argument('extra', nullable=True)
#==============================================================================
ret_fields = {
        'CRC':fields.Raw,
        'result': fields.Raw
        }
#==============================================================================
class HAProp(Resource):
    @marshal_with(ret_fields)
    def get(self):
        def get_result(args):
            result = cp.HAPropsSI(args.output_type,
                                  args.intype1,
                                  args.invalue1,
                                  args.intype2,
                                  args.invalue2,
                                  args.intype3,
                                  args.invalue3)
            return result

        args = parser.parse_args()
        if args.intype1 in 'TRDW' or \
           args.intype2 in 'TRDW' or \
           args.intype3 in 'TRDW':
               result = {
                       args.intype1: args.invalue1,
                       args.intype2: args.invalue2,
                       args.intype3: args.invalue3
                       }
               if args.output_type == 'A':
                   keys = (i for i in TYPES if i not in (args.intype1,
                                                         args.intype2,
                                                         args.intype3))
                   error_counter = 0
                   for key in keys:
                       args.output_type = key
                       try:
                           res = get_result(args)
                           result.update({key: res})
                       except Exception as e:
                           logger.error("%r\n%s key failed to calculate." % (e, key))
                           error_counter += 1
                   else:
                        if error_counter > 0:
                            result.update({'warning': True})
               else:
                   try:
                       result.update({args.output_type: get_result(args)})
                   except Exception as e:
                       logger.error("%r\n%s key failed to calculate." % \
                                    (e, args.output_type))
                       result.update({'warning': True})
        else:
            logger.error('Input Error:\nAt lease one of the parameters must in \'TRWD\'')
            result.update({'warning': True})
        return {'result': result}