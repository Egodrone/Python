#!/usr/bin/env python3

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 3 - python
#
# In these exercises we will work with functions.
#



# --------------------------------------------------------------------------
# Section 1. Functions
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a function called `greeter` that returns `"Hi, the weather is nice
# today!"`.
#
# Answer with the return value from a call to the function.
#
# Write your code below and put the answer into the variable ANSWER.
#

def greeter():
    ''' Function that return some text'''
    return "Hi, the weather is nice today!"





ANSWER = greeter()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Assign the words: 'carrot' and 'candy' to two different variables.
#
# Create a function and pass the two words as arguments to it. Your function
# should return them as a single word.
#
# Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

variableOne = "carrot"
variableTwo = "candy"

def merge(someOne, someTwo):
    ''' Function that merges two strings together'''
    mergedValues = str(someOne) + str(someTwo)
    return mergedValues

ANSWER = merge(variableOne, variableTwo)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a function called `funny_word` that takes one argument and prepends
# it to the string ' is a funny word'. **EXAMPLE:** If the argument is
# 'water', the function should return: `"water is a funny word"`.
#
# Use the argument 'sunshine' and answer with a call to the function.
#
# Write your code below and put the answer into the variable ANSWER.
#

argumentOne = "sunshine"

def funny_word(argOnepass):
    ''' Function that add extra string and return the result'''
    result = str(argOnepass) + " is a funny word"
    return result
    


ANSWER = funny_word(argumentOne)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Create a function called `summation` that takes two arguments. The function
# should return the sum of the two arguments.
#
# Answer with the return value from a call to the function with the two
# arguments 74 and 91.
#
# Write your code below and put the answer into the variable ANSWER.
#
firstNumber = 74
secondNumber = 91

def summation(first_value, second_value):
    ''' Function that return sum of two arguments'''
    result = first_value + second_value
    return result



ANSWER = summation(firstNumber, secondNumber)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Create a function called `multiplication` that takes two arguments. The
# function should return the product of the two arguments.
#
# Answer with the return value from a call to the function with the two
# arguments 74 and 91.
#
# Write your code below and put the answer into the variable ANSWER.
#


def multiplication(firstValue, secondValue):
    ''' multiplication function '''
    result = firstValue * secondValue
    return result
    




ANSWER = multiplication(firstNumber, secondNumber)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# Create a function called `in_range` that takes one argument. The function
# should return `True` if the argument is higher than 50 and lower than 100.
# If the number is out of range, the function should return `False`. The
# return type should be boolean.
#
# Use the argument 75 and answer with a call to the function.
#
# Write your code below and put the answer into the variable ANSWER.
#

def in_range(test_value):
    ''' in_range function '''
    return bool(test_value > 50 and test_value < 100)


ANSWER = in_range(firstNumber)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.7 (1 points)
#
# Create a function called `multiplicator`. Inside the function create a loop
# that iterates from 2 to 21 (both included). For each number use the
# `multiplication` function from above to get the square of the current
# number. The function should return a comma-separated string of the squared
# numbers,  without an ending `,`.
#
# Answer with a call to the function `multiplicator`.
#
# Write your code below and put the answer into the variable ANSWER.
#

def multiplicator():
    ''' multiplicator function '''
    result = ""
    for x in range(2, 22):
        z = (multiplication(x, x))
        if(x < 21):
            result = str(result) + str(z) + ","
        else:
            result = str(result) + str(z)
    return result


ANSWER = multiplicator()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.7", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.8 (1 points)
#
# Create a function called `decider`. The function takes one argument. If the
# argument is a string return a call to `funny_word()`, if the argument is an
# integer return the square of the argument by using the `multiplication`
# function.
#
# Answer with a call to the function `decider` with the value `25` as
# argument.
#
# Write your code below and put the answer into the variable ANSWER.
#

def decider(oneArg):
    ''' decider function '''
    if(isinstance(oneArg, str)):
        return funny_word(oneArg)
    if(isinstance(oneArg, int)):
        return multiplication(oneArg, oneArg)




ANSWER = decider(25)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.8", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.9 (1 points)
#
# Create a function called `double_decider`. The function takes two
# arguments. For each argument call the `decider` function. Concatenate the
# returned values in a string.
#
# Separate the two values by ' and the square is '.
#
# Answer with a call to the function `double_decider` with the values:
# filibuster and 66 as arguments.
#
# Write your code below and put the answer into the variable ANSWER.
#

def double_decider(argA, argB):
    ''' double_decider function '''
    result = ""
    firstRes = decider(argA)
    secondRes = decider(argB)
    result = str(firstRes) + ' and the square is ' + str(secondRes)
    return result


filibuster = "filibuster"
answVar = double_decider(filibuster, 66)
ANSWER = answVar

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.9", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (3 points)
#
# Create a function that returns a binary string value of a given integer.
# Return only the binary number and not any identification that it is a
# binary number.
#
# Example: Calling the function with the number 3 should return `"11"`.
#
# Answer with a call to the function with the argument 75.
#
# Write your code below and put the answer into the variable ANSWER.
#

def binaryGen(transform):
    ''' returns a binary string value of a given integer '''
    resultOfTransf = bin(transform)
    resultOfTransf = resultOfTransf[2:]
    return resultOfTransf


ansVariable = binaryGen(75)

ANSWER = ansVariable

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (3 points)
#
# Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters. The function should return a
# string with the format "Lower case letters: #, upper case letters: #". Only
# count letters, you can ignore space and special characters.
#
# Answer with a call to the function with the argument: `"JackDaws Love my
# big Sphinx of QuarTz."`.
#
# Write your code below and put the answer into the variable ANSWER.
#

def countLetters(valOfTheStr):
    ''' This function count upper and lower case letters '''
    countUpper = sum(1 for x in valOfTheStr if x.isupper())
    countLower = sum(1 for y in valOfTheStr if y.islower())
    result = "Lower case letters: " + str(countLower) + ", upper case letters: " + str(countUpper)
    return result


message = "JackDaws Love my big Sphinx of QuarTz."
ANSWER = countLetters(message)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)


dbwebb.exit_with_summary()
