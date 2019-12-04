#!/usr/bin/env python3

import re
from dbwebb import Dbwebb

# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 2 - python
#
# In this exercise we will look into flow-control. If-statements, for-loops
# and while-loops.
#



# --------------------------------------------------------------------------
# Section 1. Boolean operators and if-statements
#
# The basics of boolean operators and if-statements.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create three variables representing dice values: `dice1` = 5, `dice2` = 5
# and `dice3` = 2.
#
# Answer with the boolean value of the expression '`dice1` is greater than
# `dice2`'.
#
# Write your code below and put the answer into the variable ANSWER.
#

dice1 = 5
dice2 = 5
dice3 = 2
booleanValue = dice1 > dice2




ANSWER = booleanValue

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Sum the three variables `dice1`, `dice2` and `dice3`.
#
# Use an if-statement to decide if the sum of the three variables i greater
# than 11. If the sum is greater than 11 answer with 'big' otherwise answer
# with 'small'.
#
# Write your code below and put the answer into the variable ANSWER.
#

sum_of_all = dice1 + dice2 + dice3
result = ""

if sum_of_all > 11:
    result = "big"
else:
    result = "small"

ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Add the sum of `dice4` = 4 and `dice5` = 3 to the sum of the three other
# dices.
#
# Use an if, elseif, else statement to check the total value of the dices.
# Answer with 'small' if the sum is smaller than 11, 'intermediate' if the
# sum is greater than or equal to 11 but smaller than 21. If the sum is
# greater than or equal to 21 answer with 'big'.
#
# Write your code below and put the answer into the variable ANSWER.
#

dice4 = 4
dice5 = 3
sum_of_all = sum_of_all + dice4 + dice5
result = ""

if(sum_of_all >= 21):
    result = "big"
elif(sum_of_all >= 11):
    result = "intermediate"
else:
    result = "small"



ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Create a variable `summer_word` containing the word 'beach'.
#
# Answer with True if `summer_word` contains the letter 's' otherwise answer
# with False.
#
# Tip: Use the `in` operator.
#
# Write your code below and put the answer into the variable ANSWER.
#

summer_word = 'beach'

result = bool(re.search('[s]', summer_word))


ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. For-loops
#
# The basics of iteration and for-loops.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Loop through the numbers 0 to 10 (10 included) and concatenate a string
# with the numbers comma-separated. You should have a comma at the end of the
# string.
#
# Answer with the string.
#
# Write your code below and put the answer into the variable ANSWER.
#
string_with_numbers = ""
remember = ""

for x in range(0, 11):
    string_with_numbers = string_with_numbers + str(x) + ","

ANSWER = string_with_numbers

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Loop through the letters of the variable `summer_word` from above.
# Concatenate the consonants from `summer_word` and answer with the new word.
#
# Tip: Create a string that contains consonants and check if each letter is
# in it.
#
# Write your code below and put the answer into the variable ANSWER.
#



consonants_string = "bcdfghjklmnpqrstvwxyz"
string_without_consonants = ""

for i in summer_word:
    if i in consonants_string:
        string_without_consonants = string_without_consonants + i




ANSWER = string_without_consonants

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Loop through all numbers from 49 to 85 both numbers included. Add all odd
# (udda) numbers together and answer with the result.
#
# Tip: Use the modulus % operator.
#
# Write your code below and put the answer into the variable ANSWER.
#

sum_of_odd_numbers = 0
sum_of_even_numbers = 0

for x in range(48, 86):

    if(x % 2 == 0):
        #number is even
        sum_of_even_numbers = sum_of_even_numbers + x
    else:
        #number is odd
        sum_of_odd_numbers = sum_of_odd_numbers + x


ANSWER = sum_of_odd_numbers

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# --------------------------------------------------------------------------
# Section 3. While-loops
#
# The basics of while-loops.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (1 points)
#
# Create a while-loop that starts at value 5 and ends when the value is
# greater than 25, the value should be incremented by 3 for each iteration.
# Concatenate a string with the values comma-separated. You should have a
# comma at the end of the string.
#
# Answer with the string.
#
# Write your code below and put the answer into the variable ANSWER.
#

value_string = "5,"
value = 5

if(value == 5):
    while(value < 23):
        value = value + 3
        value_string = value_string + str(value) + ","

ANSWER = value_string

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (1 points)
#
# Create a while-loop that adds 5 to the number 37, 25 times. Answer with the
# result.
#
# Write your code below and put the answer into the variable ANSWER.
#

count = 0
result = 37

while(count < 25):
    result = result + 5
    count = count + 1

ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.3 (1 points)
#
# Create a while-loop that subtracts 4 from 55, 67 times. Answer with the
# result.
#
# Write your code below and put the answer into the variable ANSWER.
#
result = 55
count = 0
while(count < 67):
    result = result - 4
    count = count + 1

ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.3", ANSWER, False)

# --------------------------------------------------------------------------
# Section 4. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 4.1 (3 points)
#
# Use a for-loop or a while-loop to reverse the word 'philanthropist'.
#
# Answer with the reversed word.
#
# Write your code below and put the answer into the variable ANSWER.
#

word_to_reverse = "philanthropist"
result = ""
for x in range(len(word_to_reverse)-1, -1, -1):
    result += word_to_reverse[x]
'''
can also use reversed()
for x in reversed(word_to_reverse)
result += x
'''


ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("4.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 4.2 (3 points)
#
# Swedish numberplates consist of three letters and three numbers. The
# numbers range from 001 to 999. Using one of the four common rules of
# arithmetics (+, -, *, /), on how many of the numberplates can the two first
# numbers give the third number?
#
# Examples:
# 'ABC123' can be combined to 1 + 2 = 3. So this numberplate is good.
# 'ABC129' 1 and 2 cannot be combined to give 9 using the four rules of
# arithmetics, so this does not work.
#
# Order matters, so only use 1 +-*/ 2 = 3 and not 2 +-/* 1 = 3.
#
# Do not count multiple times if more than one rule of arithmetics work.
#
# Answer with the number of numberplates.
#
# Write your code below and put the answer into the variable ANSWER.
#

total = 0
exist = -2

for x in range(0, 10):
    for y in range(0, 10):
        if((x+y) == (x-y)):
            exist = exist + 1
        if((x+y) == (x*y)):
            exist = exist + 1
        if((x+y) == (x*y)):
            exist = exist + 1
        if(y > 0):
            if((x%y) == 0):
                if((x+y) == (x/y)):
                    exist = exist + 1
                if((x-y) == (x/y)):
                    exist = exist + 1
                if((x*y) == (x/y)):
                    exist = exist + 1
        if((x-y) == (x*y)):
            exist = exist + 1

        if((x + y) < 10):
            total = total + 1
        if((x-y) < 10):
            if((x-y) >= 0):
                total = total + 1
        if(y > 0):
            if((x%y) == 0):
                total = total + 1
        if((x*y) < 10):
            total = total + 1

total = total - exist

ANSWER = total

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("4.2", ANSWER, False)


dbwebb.exit_with_summary()
