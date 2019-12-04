# -*- coding: utf-8 -*-

""" Module """
import random

def answerBack():
    '''function'''
    lunchBTH = ['thairestaurangen vid korsningen',
                'det är lite mysigt i fiket jämte demolabbet',
                'Indiska',
                'Pappa curry',
                'boden uppe på parkeringen',
                'Bergåsa kebab',
                'Pasterian',
                'Villa Oscar',
                'Eat here',
                'Bistro J']
    lunchQuote = ['ska vi ta %s?',
                  'ska vi dra ned till %s?',
                  'jag tänkte käka på %s, ska du med?',
                  'På %s är det mysigt, ska vi ta där?']
    quote = lunchQuote[random.randint(0, len(lunchQuote) - 1)]
    msg = quote % lunchBTH[random.randint(0, len(lunchBTH)-1)]
    print(msg)
    return msg
