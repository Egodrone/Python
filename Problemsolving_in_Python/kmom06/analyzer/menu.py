#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Analyzer 
'''

import time
import sys
import analyzer as m

analyzer_image = r"""
    _                      _______                      _
   _dMMMb._              .adOOOOOOOOOba.              _,dMMMb_
  dP'  ~YMMb            dOOOOOOOOOOOOOOOb            aMMP~  `Yb
  V      ~"Mb          dOOO          OOOOb          dM"~      V
           `Mb.       dOOOO ANALYZER OOOOOb       ,dM'
            `YMb._   |OOOOO          OOOOOO|   _,dMP'
       __     `YMMM| OP'~"YOOOOOOOOOOOP"~`YO |MMMP'     __
     ,dMMMb.     ~~' OO     `YOOOOOP'     OO `~~     ,dMMMb.
  _,dP~  `YMba_      OOb      `OOO'      dOO      _aMMP'  ~Yb._
 <MMP'     `~YMMa_   YOOo   @  OOO  @   oOOP   _adMP~'      `YMM>
              `YMMMM\`OOOo     OOO     oOOO'/MMMMP'
      ,aa.     `~YMMb `OOOb._,dOOOb._,dOOO'dMMP~'       ,aa.
    ,dMYYMba._         `OOOOOOOOOOOOOOOOO'          _,adMYYMb.
   ,MP'   `YMMba._      OOOOOOOOOOOOOOOOO       _,adMMP'   `YM.
   MP'        ~YMMMba._ YOOOOPVVVVVYOOOOP  _,adMMMMP~       `YM
   YMb           ~YMMMM\`OOOOI`````IOOOOO'/MMMMP~           dMP
    `Mb.           `YMMMb`OOOI,,,,,IOOOO'dMMMP'           ,dM'
      `'                  `OObNNNNNdOO'                   `'
                            `~OOOOO~'
"""

countOnce = 0
#Default text file
filename = "phil.txt"
while True:
    def displayMenu(timeVar):
        ''' menu display '''
        print(analyzer_image)
        if(countOnce == 0):
            toolbar_width = 64

            sys.stdout.write("[%s]" % (" " * toolbar_width))
            sys.stdout.flush()
            sys.stdout.write("\b" * (toolbar_width + 1))
            countTime = 0
            textAnn = list("ANALYZER")
            countText2 = 0
            for i in range(toolbar_width):
                time.sleep(0.02)
                countTime = countTime + 1
                i = i
                if(countTime > 28 and countTime < 37):
                    sys.stdout.write(textAnn[countText2])
                    countText2 = countText2 + 1
                    sys.stdout.flush()
                else:
                    sys.stdout.write("-")
                    sys.stdout.flush()
                timeVar = 5
        print("\n\nChoose in the menu below:")
        print("lines: Analyze how many lines there is in a text file")
        print("words: Analyze number of words in a text file")
        print("letters: Analyze number of letters in a text file")
        print("word_frequency: Analyze word frequency in text file")
        print("letter_frequency: Analyze letter frequency of the file")
        print("all: Analaze the whole file")
        print("change: Change text file")
        print("quit: End the program\n")
        userChoice = input("Write filename to analyze or choose from the menu: ")
        return userChoice, timeVar
    choice, countOnce = displayMenu(countOnce)
    if choice == "quit":
        m.quitMenu()

    elif choice == "lines":
        m.choice2(filename, "lines")

    elif choice == "change":
        filename = m.choice3()

    elif choice == "words":
        m.choice2(filename, "words")

    elif choice == "letters":
        m.choice2(filename, "letters")

    elif choice == "all":
        m.choice2(filename, "all")

    elif choice == "word_frequency":
        m.choice2(filename, "word_frequency")

    elif choice == "letter_frequency":
        m.choice2(filename, "letter_frequency")

    else:
        print("\nNot a valid choice. You can only choose from the menu.")

    input("\nPress enter to continue...")
