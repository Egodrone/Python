#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import sys
import operator
from string import ascii_lowercase

peace_image = r"""
    _                      _______                      _
   _dMMMb._              .adOOOOOOOOOba.              _,dMMMb_
  dP'  ~YMMb            dOOOOOOOOOOOOOOOb            aMMP~  `Yb
  V      ~"Mb          dOOOOOOOOOOOOOOOOOb          dM"~      V
           `Mb.       dOOOO ANALYZER OOOOOb       ,dM'
            `YMb._   |OOOOOOOOOOOOOOOOOOOOO|   _,dMP'
       __     `YMMM| OPYOOOOOOOOOOOOOOOOOOOYO |MMMP'     __
     ,dMMMb.     ~~' OOOOOOOOOOOOOOOOOOOOOOO `~~     ,dMMMb.
  _,dP~  `YMba_      OOOOOOOOOOOOOOOOOOOOOOO      _aMMP'  ~Yb._
 <MMP'     `~YMMa_   YOOOOOOOOOOOOOOOOOOOOOP   _adMP~'      `YMM>
              `YMMMM\`OOOOOOOOOOOOOOOOOOoOOO'/MMMMP'
      ,aa.     `~YMMb `OOOOOOOOOOOOOOOOOOOO'dMMP~'       ,aa.
    ,dMYYMba._         `OOOOOOOOOOOOOOOOO'          _,adMYYMb.
   ,MP'   `YMMba._      OOOOOOOOOOOOOOOOO       _,adMMP'   `YM.
   MP'        ~YMMMba._ YOOOOPVVVVVYOOOOP  _,adMMMMP~       `YM
   YMb           ~YMMMM\`OOOOOOOOOOOOOOOO'/MMMMP~           dMP
    `Mb.           `YMMMb`OOOOOOOOOOOO'dMMMP'           ,dM'
      `'                  `OObNNNNNdOO'                   `'
                            `~OOOOO~'
"""
def quitMenu():
    ''' Function to exit while loop '''

    print(peace_image)
    toolbar_width = 64

    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width + 1))
    countTime2 = 0
    textAnalyzer = list("ANALYZER")
    countAText = 0
    for i in range(toolbar_width):
        time.sleep(0.02)
        countTime2 = countTime2 + 1
        i = i
        if(countTime2 > 28 and countTime2 < 37):
            sys.stdout.write(textAnalyzer[countAText])
            countAText = countAText + 1
            sys.stdout.flush()
        else:
            sys.stdout.write("-")
            sys.stdout.flush()
    exit()

def choice2(nameOfTheFile, userChoice):
    ''' Main analyze function '''

    numberOfLines = 0
    numberOfWords = 0
    numberOfLetters = 0

    with open(nameOfTheFile, 'r') as dragon:
        for line in dragon:
            words = line.split()
            numberOfLines += 1
            numberOfWords += len(words)
            numberOfLetters += len(line)

    if(userChoice == "lines"):
        num_lines = sum(1 for line in open(nameOfTheFile))
        print("\nNumber of lines in a text file " + str(nameOfTheFile) + ": "  + str(num_lines))

    if(userChoice == "words"):
        print("\nNumber of words in file " + str(nameOfTheFile) + ": " + str(numberOfWords))

    if(userChoice == "letters"):
        with open(nameOfTheFile) as f:
            text = f.read().lower().strip()
            dic = {}
            for x in ascii_lowercase:
                dic[x] = text.count(x)
        sumAll = 0
        for key, value in sorted(dic.items()):
            value = value
            sumAll = sumAll + dic.get(key)
        print("\nNumber of letters in file " + str(nameOfTheFile) + ": " + str(sumAll))

    if(userChoice == "all"):
        num_lines = sum(1 for line in open(nameOfTheFile))
        print("\nNumber of lines in a text file " + str(nameOfTheFile) + ": "  + str(num_lines))
        print("\nNumber of words in file " + str(nameOfTheFile) + ": " + str(numberOfWords))
        with open(nameOfTheFile) as f:
            text = f.read().lower().strip()
            dic = {}
            for x in ascii_lowercase:
                dic[x] = text.count(x)
        sumAll = 0
        for key, value in sorted(dic.items()):
            sumAll = sumAll + dic.get(key)
        print("\nNumber of letters in file " + str(nameOfTheFile) + ": " + str(sumAll))

        print("\nSeven most common letters from the text in %:")
        with open(nameOfTheFile) as f:
            text = f.read().lower().strip()
            dic = {}
            for x in ascii_lowercase:
                dic[x] = text.count(x)
        dic2 = dic

        sumAll = 0
        for key, value in sorted(dic2.items()):
            sumAll = sumAll + dic2.get(key)
        procentHere = 100/sumAll

        sorted_dic = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
        county = 0

        for x in sorted_dic:
            if(county < 7):
                roundedAnsw = round(x[1] * procentHere, 2)
                print(x[0], roundedAnsw, "%")
            county = county + 1

        hand = open(nameOfTheFile)

        di = dict()
        for linez in hand:
            linez = linez.lower().rstrip()
            ddos = linez.split()
            for w in ddos:
                if(w.endswith(',') or w.endswith('.')):
                    w = w[:-1]
                    di[w] = di.get(w, 0) + 1
                else:
                    di[w] = di.get(w, 0) + 1

        procentW = 100/numberOfWords
        sorted_dic = sorted(di.items(), key=operator.itemgetter(1), reverse=True)
        county = 0
        print("\nSeven most common words from the text in %:")

        for x in sorted_dic:
            if(county < 7):
                roundProc = round(procentW * x[1], 2)
                print(x[0], roundProc, "%")
            county = county + 1
    if(userChoice == "word_frequency"):
        hand = open(nameOfTheFile)
        di = dict()

        for lin in hand:
            lin = lin.lower().rstrip()
            ddos = lin.split()

            for w in ddos:
                if(w.endswith(',') or w.endswith('.')):
                    w = w[:-1]
                    di[w] = di.get(w, 0) + 1
                else:
                    di[w] = di.get(w, 0) + 1

        procentW = 100/numberOfWords

        sorted_dic = sorted(di.items(), key=operator.itemgetter(1), reverse=True)
        county = 0
        print("\nSeven most common words from the text in %:")
        for x in sorted_dic:
            if(county < 7):
                roundProc = round(procentW * x[1], 2)
                print(x[0], roundProc, "%")
            county = county + 1

    if(userChoice == "letter_frequency"):
        print("\nSeven most common letters from the text in %:")
        with open(nameOfTheFile) as forx:
            text = forx.read().lower().strip()
            dic = {}
            for x in ascii_lowercase:
                dic[x] = text.count(x)
        dic2 = dic

        sumAll = 0
        for key, value in sorted(dic2.items()):
            sumAll = sumAll + dic2.get(key)

        procentHere = 100/sumAll

        sorted_dic = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
        county = 0
        for x in sorted_dic:
            if(county < 7):
                roundedAnsw = round(x[1] * procentHere, 2)
                print(x[0], roundedAnsw, "%")
            county = county + 1

def choice3():
    '''Function to change file that will be analyzed'''

    filename = input("Write new filename you want to analyze: ")
    return filename
