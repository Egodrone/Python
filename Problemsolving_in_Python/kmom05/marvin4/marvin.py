#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created by: Egodrone
Simple script to give some output on users input.
Presents a menu with different choices.
Script don't have a solid filter so user have to give right input in terms of
strings and integers
"""
import random
from random import randint
#import main
#import quote
import datetime

def quitMenu():
    ''' quit function '''
    print("Bye, bye - and welcome back anytime!")
    exit()

def eleventhree(aArg, bArg):
    ''' function '''
    x = 0
    strToRet = ""
    while(x < bArg):
        #print(aArg)
        if(str(aArg) != "#"):
            strToRet = strToRet + " " + str(aArg)
            x = x + 1
        if(str(aArg) == "#"):
            strToRet = strToRet + str(aArg)
            x = x + 1
    return strToRet

def choice1():
    ''' function '''
    name = input("Hello human, What is your name? ")
    print("\nOverlord says:\n")
    print("Hello %s - what a beautiful name! " % name)
    print("Need help with anything?!")

def choice2():
    ''' function '''
    celcius = input("Enter temperature in Celcius: ")
    convert_cel_to_far = int(celcius) * 9/5 + 32
    print("\nThat is: " + str(convert_cel_to_far) + " in Farenheit")

def choice3():
    ''' function '''
    name = input("Enter a word: ")
    repeat = input("Enter how many times you want to repeat this word: ")
    '''
    x = 0
    while(x < int(repeat)):
        print(name)
        x = x + 1
    '''
    name = eleventhree(name, int(repeat))
    print(name)

def choice4():
    ''' function '''
    sum_of_numbers = 0
    number = ""
    mean_value = 0
    count_numbers = 0

    print("Press 'enter' after every number. Enter 'done' to get a result!")
    while(number != "done"):
        number = input("Enter any number: ")
        if(number != "done"):
            sum_of_numbers = sum_of_numbers + float(number)
            count_numbers = count_numbers + 1

    print("Sum of all numbers from input: " + str(sum_of_numbers))
    mean_value = round(sum_of_numbers/count_numbers, 2)
    print("Mean value of the numbers from input: " + str(mean_value))

def choice5():
    ''' function '''
    first_value = 0
    shifting_value = 0
    count = 0
    store_input = 0
    boolean_compare = False

    while(str(shifting_value) != "done"):
        if(count == 0):
            first_value = input("Enter number here to compare: ")
            count = count + 1
            print("This is your first number! Type in another one to compare: ")
        elif(count > 0):
            if(boolean_compare is False):
                shifting_value = input("Enter any number: ")
                store_input = shifting_value
                if(str(shifting_value) != "done"):
                    if(shifting_value > first_value):
                        print("Bigger")
                        boolean_compare = True
                    elif(shifting_value < first_value):
                        print("Smaller")
                        boolean_compare = True
                    else:
                        print("equal")
                        boolean_compare = True

        if boolean_compare is True:
            shifting_value = input("Enter any number: ")
            first_value = shifting_value
            if(str(shifting_value) != "done"):
                if(shifting_value > store_input):
                    print("Bigger")
                    boolean_compare = False
                elif(shifting_value < store_input):
                    print("Smaller")
                    boolean_compare = False
                else:
                    print("equal")
                    boolean_compare = False

def choice6():
    ''' function '''
    count_iteretions = 0
    count = 0
    display = ""
    echo_out = input("Enter any word: ")
    for i in echo_out:
        count = count + 1
        count_iteretions = 0
        while count_iteretions != count:
            display = display + str(i)
            count_iteretions = count_iteretions + 1
            if count_iteretions == count:
                if count_iteretions != len(echo_out):
                    display = display + "-"
                else:
                    print(display)

def choice7():
    ''' function '''
    word_to_check = input("Enter any word: ")
    howmany = 0
    result = False
    for i in word_to_check:
        howmany = word_to_check.count(i)
        if howmany > 1:
            result = True
    if result is True:
        print("No Match")
    else:
        print("Match")

def choiceA1():
    ''' function '''
    first_word = input("Enter your first word: ")
    second_word = input("Enter second word to compare characters: ")
    count = 0
    first_word = first_word.lower()
    second_word = second_word.lower()
    compareLen = len(second_word)

    for i in range(0, compareLen):
        for x in range(0, compareLen):
            if first_word[i] == second_word[x]:
                count = count + 1
                break
    if (count == compareLen):
        print("\nMatch")
    else:
        print("\nNo Match")

def choiceA2():
    ''' function '''
    brackets = input("Enter brackets and press enter: ")

    def brackets_territory(abc):
        ''' Function to balance brackets'''
        neverBother = []
        letters = list(brackets)

        for tes in letters:
            dxdydz = {'(': ')', '[': ']', '{': '}'}
            lenVektor1 = len(neverBother)
            if tes in dxdydz.keys():
                neverBother.append(tes)
            elif tes in dxdydz.values() and lenVektor1 > 0:
                doThePop = neverBother.pop()
                if dxdydz.get(doThePop) != tes:
                    return "No match"

        lenVektor2 = len(neverBother)
        if lenVektor2 == 0:
            return "Match"
        del abc

    print(brackets_territory(brackets))

def choice8():
    ''' function '''
    changeWord = input("Give a word: ")
    checkLength = len(changeWord)
    changeWord = list(changeWord)
    random.shuffle(changeWord)
    randWord = ""
    #newWord = ""
    #saveChar = []
    #randomDigit = 0
    #randomDigit = randint(1, checkLength - 2)
    #print(randomDigit)
    #count = 0
    for cd in range(0, checkLength):
        randWord = str(randWord) + str(changeWord[cd])
    '''
    for x in range(0, checkLength):
        if(count < 1):
            #print(randomDigit)
            saveChar.append(changeWord[randomDigit])
            #print(saveChar[0])
            changeWord[randomDigit] = changeWord[randomDigit + 1]
            changeWord[randomDigit + 1] = saveChar[0]
        else:
            if(count < checkLength - 1):
                saveChar.append(changeWord[x])
                #print(count)
                changeWord[x] = changeWord[x + 1]
                changeWord[x + 1] = saveChar[x]
        count = count + 1
    for cd in range(0, checkLength):
        newWord = str(newWord) + str(changeWord[cd])
    print(newWord)
    '''
    print(randWord)

def choice9():
    ''' function '''
    firstStr = input("Enter first string: ")
    secondStr = input("Enter second string: ")
    firstStr = firstStr.lower()
    secondStr = secondStr.lower()
    firstStr = ''.join(sorted(firstStr))
    secondStr = ''.join(sorted(secondStr))
    if(firstStr == secondStr):
        print("Match")
    else:
        print("No Match")

def choice10():
    ''' function '''
    generatorWord = input("Enter a string to create ancronym: ")
    storeLarge = generatorWord.isupper()
    if(storeLarge is False):
        print(''.join([c for c in generatorWord if c.isupper()]))

def choice11():
    ''' function '''
    wordToMask = input("Enter number to mask: ")
    '''
    wordToMaskLen = len(wordToMask) - 3
    modifiedWord = ""
    hashesStr = ""
    for x in range(0, wordToMaskLen):
        modifiedWord = wordToMask[x:]
        hashesStr = str(hashesStr) + "#"
    hashesStr = str(hashesStr) + str(modifiedWord)
    print(hashesStr[1:])
    '''
    wordToMaskLen = len(wordToMask) - 4
    displayAnsw = eleventhree("#", wordToMaskLen)
    print(displayAnsw + wordToMask[wordToMaskLen:])

def choiceB1():
    ''' function '''
    points = input("Enter score: ")
    points = float(points)
    if(points <= 1 and points > 0):
        if(points < 0.5):
            print("F")
        elif(points >= 0.6 and points < 0.7):
            print("D")
        elif(points >= 0.7 and points < 0.8):
            print("C")
        elif(points >= 0.8 and points < 0.9):
            print("B")
        else:
            print("A")
    else:
        print("Enter points between 0.0 and 1.0")

def choiceB2():
    ''' function '''
    firstStr = input("Enter the first word: ")
    secondStr = input("Enter second word: ")
    thirdStr = input("Enter the third word: ")
    fourthStr = input("Enter the fourth word: ")
    if(firstStr.startswith(secondStr) is True and firstStr.endswith(fourthStr, 2) is True):
        if firstStr.find(thirdStr) == -1:
            print("No match")
        else:
            print("Match")
    else:
        print("No match")

def stateAndDate():
    ''' function to display date and time. Genereta random mood of Marvin Overlord Beta. '''
    #mylist = []
    #today = datetime.date.today()
    #mylist.append(today)
    dateAndTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    #https://github.com/reechani/python/blob/master/example/marvin/format.py
    fhand = open("format.txt", "r")
    # Generate random digit to read the line from the file
    randomDig = randint(0, 8)
    line = fhand.readline()[randomDig]
    #print(line)
    line = open("format.txt", "r").readlines()[randomDig]
    stateOfMind = line
    reference = 10
    pointToReference = str(randint(0, 9)) + ","
    for skr in range(0, 3):
        slump = randint(0, 9)
        skr = skr
        pointToReference = str(pointToReference) + str(slump)
    #moods = ["happy", "sad", "depressed", "angry", "annoyed", "bored", "confused", "excited", "lonely"]
    #mood = random.choice(moods)
    #smilies = [":)", ":(", ":D", ":/", ":|", ":'(", ":O", ":@", ":P", ":3"]
    #smiley = random.choice(smilies)
    varTd = " of possible units right now."
    #print(line.format(mood=mood, smiley=smiley))

    '''
    This is a multiline
    comment.
    '''
    return print(dateAndTime + " Feeling " \
 + str(stateOfMind) + " " + str(reference) + "/" + str(pointToReference) \
 + varTd)

def inventory():
    ''' function for the inventory'''
    filename = "inv.data"
    count = 0
    with open(filename) as filehandle:
        count = count + 1
        line = filehandle.readline().strip()
        #lenLine = len(filehandle.readline().strip())
        if line == '\n':
            print("Found")
        #print(line)
        items_as_list = line.split(",")
        lengOfList = len(items_as_list)
        if(lengOfList == 1):
            print("Inventory is empty []")
        else:
            print(" \n You have " + str(lengOfList - 1) + " thing(s): " + str(items_as_list[1:lengOfList]))
        #print(items_as_list)

def inventoryAdd(passedChoce):
    ''' Function to add items to the file '''
    #filename = open("inv.data", "a")
    #filename.write("Add datetime ")
    #filename.close()
    filename = "inv.data"
    # with - as for reading a file automatically closes it after reading is done
    with open(filename) as filehandle:
        line = filehandle.readline().strip()
        # split the line into a list on the comma ","
        items_as_list = line.split(",")
        # print what the list looks like
        #print(items_as_list)
        passedLen = len(passedChoce)
        items_as_list.append(str(passedChoce[9:passedLen]))
        list_as_str = ",".join(items_as_list)
        #print(list_as_str)
        with open(filename, "w") as filehandle:
            filehandle.write(list_as_str)
    print("\n " + "You have picked up: " + str(passedChoce[9:passedLen]))

def inventoryRemove(passedChoce):
    ''' Function to remove items from the inv'''
    filename = "inv.data"
    # with - as for reading a file automatically closes it after reading is done
    with open(filename) as filehandle:
        line = filehandle.readline().strip()
        # split the line into a list on the comma ","
        items_as_list = line.split(",")
        # print what the list looks like
        #print(items_as_list)
        passedLen = len(passedChoce)
        #print(len(items_as_list))
        count = 0
        check = 0
        for x in items_as_list:
            #print(x)
            #print(count)
            #print(str(passedChoce[9:passedLen]))
            if(x == str(passedChoce[9:passedLen])):
                items_as_list.pop(count)
                check = check + 1
                print("\n" + str(passedChoce[9:passedLen]) + " was removed from the inventory")
                #print("Value of x: " + str(x))
            else:
                pass
            count = count + 1
        list_as_str = ",".join(items_as_list)
        if(check == 0):
            print("\n Trere are no " + str(passedChoce[9:passedLen]) + " in your inventory")
        #print(list_as_str)
        with open(filename, "w") as filehandle:
            filehandle.write(list_as_str)

    '''
    filename = "inv.data"
    # with - as for reading a file automatically closes it after reading is done
    with open(filename) as filehandle:
        line = filehandle.readline().strip()
        # split the line into a list on the comma ","
        items_as_list = line.split(",")
        # print what the list looks like
        print(items_as_list)
        passedLen = len(passedChoce)
        #print(len(items_as_list))
        listLength = len(items_as_list)
        print(listLength)
        for x in range(0, listLength):
            print(x)
        for x in range(0, listLength-1):
            print(items_as_list[3])
            print(str(passedChoce[9:passedLen]))
            if(items_as_list[x] == str(passedChoce[9:passedLen])):
                items_as_list.pop(x)
                print("Value of x: " + str(x))
            else:
                pass
        list_as_str = ",".join(items_as_list)
        #print(list_as_str)
        with open(filename, "w") as filehandle:
            try:
                filehandle.write(list_as_str)
                print(str(passedChoce[9:passedLen]) + " was removed from the inventory")
            except:
                print(str(passedChoce[9:passedLen]) + " was not in the inventory")
    '''
    '''
    filename = "inv.data"
    lenOfAll = len(passedChoice)
    with open(filename) as filehandle:
        line = filehandle.readline().strip()
        print(line + " ooo ")
        if any(s in line for s in str(passedChoice[9:lenOfAll])):
            #line.replace(str(passedChoice[9:lenOfAll]),"Replaced")
            print("yay!")
        #print(line)
        items_as_list = line.split(",")
        #print(items_as_list)
        #print(passedChoice[9:lenOfAll])
        if any(str(passedChoice[9:lenOfAll]) in s for s in items_as_list):
            print("This worked")
            with open(filename, "w") as filehandle:
                items_as_list.remove(str(passedChoice[9:lenOfAll]))
                print(items_as_list[0])
            #items_as_list.remove(passedChoice[9:lenOfAll]);
    '''
