#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created by: Egodrone
Simple script to give some output on users input.
Presents a menu with 9 different choices.
Script don't have a filter so user have to give right input in terms of
strings and integers
"""

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
    print("q) Quit.\n")

    choice = input("--> ")

    if choice == "q":
        print("Bye, bye - and welcome back anytime!")
        break

    elif choice == "1":
        name = input("Hello human, What is your name? ")
        print("\nOverlord says:\n")
        print("Hello %s - what a beautiful name! " % name)
        print("Need help with anything?!")

    elif choice == "2":
        celcius = input("Enter temperature in Celcius: ")
        convert_cel_to_far = int(celcius) * 9/5 + 32
        print("\nThat is: " + str(convert_cel_to_far) + " in Farenheit")

    elif choice == "3":
        name = input("Enter a word: ")
        repeat = input("Enter how many times you want to repeat this word: ")
        for x in range(0, int(repeat)):
            print(name)

    elif choice == "4":
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

    elif choice == "5":
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

    elif choice == "6":
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

    elif choice == "7":
        word_to_check = input("Enter any word: ")
        count = 0
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

#Extra task 1
    elif choice == "A1":
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

#Extra task 2
    elif choice == "A2":
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
    else:
        print("That is not a valid choice. You can only choose from the menu.")

    input("\nPress enter to continue...")
