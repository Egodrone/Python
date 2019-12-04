#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created by: Egodrone
Simple script to give some output on users input.
Presents a menu with 15 different choices.
Script don't have a filter so user have to give right input in terms of
strings and integers
"""
import random
#from random import randint

marvin_image = r"""
                           www
                          /n n\        /\
                          |/^\|       /  \
                          | , |       ^||^
                           \_/         ||
                           _U_         ||
                         /`   `''-----'P3
                        / |. .|''-----"||
                        \'|   |        ||
                         \|   |        ||
                          E   |        ||
                         /#####\       ||
                         /#####\       ||
                           |||         ||
                           |||         ||
                           |||         ||
                           |||         ||
                      Overlord Beta    Ll
"""

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""
while True:
    def displayMenu():
        ''' menu display '''
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Overlord. I know some things. If you need help, let me know! :)\n")
        print("1) Present yourself to Overlord.")
        print("2) Convert from Celcius to Farenheit")
        print("3) Multiply words.")
        print("4) Sum of numbers and middlevalue.")
        print("5) Evaluate numbers input.")
        print("6) Echo the word out.")
        print("7) Check if the word is an isogram.")
        print("A1) Compare characters in a string.")
        print("A2) Balance brackets.")
        print("8) Random change of the word.")
        print("9) Check if the word is anagram.")
        print("10) Acronym generator.")
        print("11) Mask string.")
        print("B1) Points of the grade.")
        print("B2) Compare 4 strings.")
        print("q) Quit.\n")

        userChoice = input("--> ")
        return userChoice
    choice = displayMenu()
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

    if choice == "q":
        quitMenu()

    elif choice == "1":
        choice1()

    elif choice == "2":
        choice2()

    elif choice == "3":
        choice3()

    elif choice == "4":
        choice4()

    elif choice == "5":
        choice5()

    elif choice == "6":
        choice6()

    elif choice == "7":
        choice7()

#Extra task 1
    elif choice == "A1":
        choiceA1()

#Extra task 2
    elif choice == "A2":
        choiceA2()

    elif choice == "8":
        choice8()

    elif choice == "9":
        choice9()

    elif choice == "10":
        choice10()

    elif choice == "11":
        choice11()

    elif choice == "B1":
        choiceB1()

    elif choice == "B2":
        choiceB2()

    else:
        print("That is not a valid choice. You can only choose from the menu.")

    input("\nPress enter to continue...")
