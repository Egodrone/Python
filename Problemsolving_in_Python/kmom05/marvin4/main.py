#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created by: Egodrone
Simple script to give some output on users input.
Presents a menu with 16 different choices.
Script don't have a filter so user have to give right input in terms of
strings and integers
"""

import marvin
import quote
import hej
import lunch
import tic

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
        print("12) State of mind and date.")
        print("D1) TicTacToe")
        #print("citat) Print citat")
        print("q) Quit.\n")

        userChoice = input("--> ")
        return userChoice
    choice = displayMenu()
    if choice == "q":
        marvin.quitMenu()

    elif choice == "1":
        marvin.choice1()

    elif choice == "2":
        marvin.choice2()

    elif choice == "3":
        marvin.choice3()

    elif choice == "4":
        marvin.choice4()

    elif choice == "5":
        marvin.choice5()

    elif choice == "6":
        marvin.choice6()

    elif choice == "7":
        marvin.choice7()

#Extra task 1
    elif choice == "A1":
        marvin.choiceA1()

#Extra task 2
    elif choice == "A2":
        marvin.choiceA2()

    elif choice == "8":
        marvin.choice8()

    elif choice == "9":
        marvin.choice9()

    elif choice == "10":
        marvin.choice10()

    elif choice == "11":
        marvin.choice11()

    elif choice == "B1":
        marvin.choiceB1()

    elif choice == "B2":
        marvin.choiceB2()

    elif choice.lower() == "citat":
        quote.choiceCitat()

    elif choice == "12":
        marvin.stateAndDate()

    elif choice.lower() == "hej" and choice.lower().find("hej") != -1:
        hej.answerBack1()

    elif choice.lower() == "lunch" and choice.lower().find("lunch") != -1:
        lunch.answerBack()

    elif choice == "inv":
        marvin.inventory()

    elif choice[0:8] == "inv pick":
        marvin.inventoryAdd(choice)

    elif choice[0:8] == "inv drop":
        marvin.inventoryRemove(choice)

    elif choice == "D1":
        tic.main()

    else:
        print("That is not a valid choice. You can only choose from the menu.")

    input("\nPress enter to continue...")
