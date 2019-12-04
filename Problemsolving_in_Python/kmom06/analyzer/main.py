#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Main menu
'''
import menu as m

countOnce = 0
filename = "phil.txt"
while True:
    choice, countOnce = m.displayMenu(countOnce)
