# -*- coding: utf-8 -*-

from random import randint

def choiceCitat():
    ''' Random quote '''
    countLines = 0
    filename = "quotes.txt"
    fileToOpen = open(filename)
    #check how many lines there is
    for line in enumerate(fileToOpen):
        #print(line)
        countLines = countLines + 1

    randomDig = randint(0, countLines-1)
    line = open("quotes.txt", "r").readlines()[randomDig]
    print(line)
