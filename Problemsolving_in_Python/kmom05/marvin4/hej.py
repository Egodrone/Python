# -*- coding: utf-8 -*-

"""This module do stuff"""
import random

def answerBack1():
    '''function'''
    hello = ['Hej själv! ', 'Trevligt att du bryr dig om mig. ', 
             'Det var länge sedan någon var trevlig mot mig. ', 'Halloj, det ser ut att bli mulet idag. ']
    quote = hello[random.randint(0, len(hello) - 1)]
    msg = quote
    print(msg)
    return msg
