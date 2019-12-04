#!/usr/bin/env python3

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 6 - python
#
# A look into dictionaries and tuples.
#



# --------------------------------------------------------------------------
# Section 1. Dictionaries
#
# Some basics with dictionaries.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a small phonebook using a dictionary. Use the names as keys and
# numbers as values.
#
# Use
#
# > Chandler, Monica, Ross
#
# and corresponding numbers
#
# > 55523645, 55564452, 55545872
#
# Add the phonenumbers as integers. Answer with the resulting dictionary.
#
# Write your code below and put the answer into the variable ANSWER.
#


dict1 = {
    "Chandler" : 55523645,
    "Monica" : 55564452,
    "Ross": 55545872
}



ANSWER = dict1

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# How many items are there in the phonebook dictionary?
#
# Write your code below and put the answer into the variable ANSWER.
#
result = len(dict1)





ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Use the `get()` method on your phonebook and answer with the phonenumber of
# 'Ross'.
#
# Write your code below and put the answer into the variable ANSWER.
#

resultFrom = dict1.get("Ross")



ANSWER = resultFrom

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Get all keys from the phonebook dictionary and return them in a sorted
# list.
#
# Write your code below and put the answer into the variable ANSWER.
#

list1 = []
def sortKeys(listPassed, dictPassed):
    '''Function'''
    for key2 in dictPassed.keys():
        listPassed.append(key2)
    return sorted(listPassed)

list1 = sortKeys(list1, dict1)




ANSWER = list1

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Get all values from the phonebook dictionary and return them in a sorted
# list.
#
# Write your code below and put the answer into the variable ANSWER.
#
listOfValues = []
listOfValues = dict1.values()
listOfValues = sorted(listOfValues)





ANSWER = listOfValues

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# Use the in-operator to test if the name 'Ross' exists in the phonebook
# dictionary. Answer with the return boolean value.
#
# Write your code below and put the answer into the variable ANSWER.
#

result = bool("Ross" in dict1)




ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.7 (1 points)
#
# Create a copy of the phonebook dictionary.
# Get and remove the item 'Ross' from the copied phonebook (use pop()).
# Answer with the resulting dictionary.
#
# Write your code below and put the answer into the variable ANSWER.
#
dict2 = dict1

def remWithKey(dictionary, key3):
    """Return the copy of dictionary without the key"""
    s_dict = dictionary.copy()
    s_dict.pop(key3, None)
    return s_dict


dict2 = remWithKey(dict2, "Ross")

ANSWER = dict2

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.7", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Tuples
#
# Some basics with tuples.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Create a tuple with 'frog, 54, 4.77, fridge, 2'. Answer with the length of
# the tuple as an integer.
#
# Write your code below and put the answer into the variable ANSWER.
#


tuple1 = ("frog", 54, 4.77, "fridge", 2)
lenOfTuple1 = len(tuple1)



ANSWER = lenOfTuple1

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Create a tuple out of:
#
# > (frog, 54, 4.77, fridge, 2).
#
# Assign each value in the tuple to different variables:
#
# > 'a','b','c','d','e'.
#
# Answer with the variable: 'd'.
#
# Write your code below and put the answer into the variable ANSWER.
#

tuple2 = ("frog", 54, 4.77, "fridge", 2)
wordabc = "abcde"
listwordAbc = list(wordabc)
dicW = {}
lenWord = len(wordabc)
for gt in range(0, lenWord):
    dicW[listwordAbc[gt]] = tuple2[gt]


ANSWER = dicW["d"]

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Use the list
#
# > [45, 22, 2, 498, 78]
#
# Assign the first two elements to a tuple with a slice on the list.
#
# Answer with the first element in the tuple as an integer.
#
# Write your code below and put the answer into the variable ANSWER.
#

listUse = [45, 22, 2, 498, 78]
tuplex = tuple(listUse[0:2])




ANSWER = int(tuplex[0])

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# Create a tuple with
#
# > (snake, 89, 9.63, bookshelf, 1)
#
# Convert it to a list and replace the second element with:
#
# > "elephant"
#
# Convert it back to a tuple and answer with the first three elements in a
# comma-separated string,  without an ending `,`.
#
# Write your code below and put the answer into the variable ANSWER.
#

tupleToConv = ("snake", 89, 9.63, "bookshelf", 1)
tupleL = list(tupleToConv)
tupleL[1] = "elephant"
tupleToConv = tuple(tupleL)
strAnsw = ""
for x in range(0, 3):
    if x == 0:
        strAnsw = str(tupleToConv[x])
    else:
        strAnsw = strAnsw + "," + str(tupleToConv[x])


ANSWER = strAnsw

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.4", ANSWER, False)

# --------------------------------------------------------------------------
# Section 3. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (3 points)
#
# Use a for-loop to walk through the original phonebook dictionary and create
# a string representing it. Each name and number should be on its own row,
# separated by a space. The names must come in alphabetical order. Note that
# every row should end with a newline character, `\n`.
#
# Answer with the resulting string.
#
# Write your code below and put the answer into the variable ANSWER.
#

strReprs = ""
dictSr = dict1
for key, value in sorted(dictSr.items()):
    storeValue = dictSr.get(key)
    strReprs = str(strReprs) + str(key) + " " + str(storeValue) + "\n"



ANSWER = strReprs

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (3 points)
#
# Convert the phonenumber to a string and add the prefix '+1-', representing
# the language code, to each phone-number.
#
# Answer with the resulting dictionary.
#
# Write your code below and put the answer into the variable ANSWER.
#

dictCh = {}
for key, value in dict1.items():
    storeValue = dict1.get(key)
    storeValue = '+1-' + str(storeValue)
    dictCh[key] = storeValue





ANSWER = dictCh

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, False)


dbwebb.exit_with_summary()
