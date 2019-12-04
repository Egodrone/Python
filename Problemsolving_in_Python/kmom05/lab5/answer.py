#!/usr/bin/env python3

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 5 - python
#
# "In these exercises we will take a look into lists."
#



# --------------------------------------------------------------------------
# Section 1. List basics
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Concatenate the two lists [mosquito, Berenger] and [cougar, floor].
#
# Answer with your list.
#
# Write your code below and put the answer into the variable ANSWER.
#

newList = []
first = ["mosquito", "Berenger"]
second = ["cougar", "floor"]

newList.insert(0, first[0])
newList.append(first[1])
newList.append(second[0])
newList.append(second[1])



ANSWER = newList

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Use the list [wasp, fly, butterfly, bumblebee, mosquito].
#
# Add the words 'hotdog' and 'bag' as the second and third element.
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#

list1 = ['wasp', 'fly', 'butterfly', 'bumblebee', 'mosquito']
list1.insert(1, 'hotdog')
list1.insert(2, 'bag')




ANSWER = list1

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Use the list [wasp, fly, butterfly, bumblebee, mosquito].
#
# Replace the third word with: 'painting'.
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#

anotherList = ['wasp', 'fly', 'butterfly', 'bumblebee', 'mosquito']
anotherList[2] = "painting"



ANSWER = anotherList

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Sort the list
#
# > [flute, guitar, drums, piano, bass]
#
# in descending alphabetical order. Answer with the sorted list.
#
# Write your code below and put the answer into the variable ANSWER.
#

listToSort = ['flute', 'guitar', 'drums', 'piano', 'bass']
listToSort.sort()
listToSort = listToSort[::-1]

ANSWER = listToSort

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Use `remove()` to delete the word:
#
# > 'butterfly'
#
# from the list:
#
# > [wasp, fly, butterfly, bumblebee, mosquito]
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#
oneTwo = ['wasp', 'fly', 'butterfly', 'bumblebee', 'mosquito']
oneTwo.remove('butterfly')




ANSWER = oneTwo

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Built-in list functions
#
# Some basic built-in functions.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Use a built-in function to sum all numbers in the list:
#
# > [45, 22, 2, 498, 78]
#
# Answer with the result as an integer.
#
# Write your code below and put the answer into the variable ANSWER.
#

numList = [45, 22, 2, 498, 78]
result = sum(numList)




ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Use built-in functions, such as `sum` and `len` to get the average value of
# the list:
#
# > [45, 22, 2, 498, 78]
#
# Answer with the result as a float with at most one decimal.
#
# Write your code below and put the answer into the variable ANSWER.
#
numList2 = [45, 22, 2, 498, 78]
summa = sum(numList2)
lengthOf = len(numList2)
result2 = summa/lengthOf





ANSWER = result2

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Use the built-in functions `split()` and `join()` to fix this string:
#
# > "The?wind?is?blowing"
#
# into a real sentence, (without '?').
#
# Answer with the fixed string.
#
# Write your code below and put the answer into the variable ANSWER.
#
fstring = "The?wind?is?blowing"
result3 = fstring.split("?")
swe = " "
ddos = " ".join(result3)




ANSWER = ddos

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# Use slice on the list
#
# > [dvd, mp3, blu-ray, vhs, cd]
#
# and replace the second and third element with
#
# > "green, purple"
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#

ufck = ['dvd', 'mp3', 'blu-ray', 'vhs', 'cd']
ufck[1:-2] = ["green", "purple"]
#print(ufck)


ANSWER = ufck

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.5 (1 points)
#
# Assign the list
#
# > [b, a, e, d, c]
#
# to a variable called 'list1'.
#
# Assign the list again, but to another variable called 'list2'.
#
# Answer with the result of 'list1 is list2'.
#
# Write your code below and put the answer into the variable ANSWER.
#

list1 = ['b', 'a', 'e', 'd', 'c']
list2 = ['b', 'a', 'e', 'd', 'c']
result4 = bool(list1 is list2)



ANSWER = result4

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.6 (1 points)
#
# Use your lists from the last exercise. Assign 'list1' to another variable
# called 'list3' like this:
#
# > list3 = list1
#
# Answer with the result of 'list1 is list3'.
#
# Write your code below and put the answer into the variable ANSWER.
#
list3 = list1
result5 = bool(list1 is list3)





ANSWER = result5

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.6", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.7 (1 points)
#
# Use your lists from the last exercise. Change the first element in 'list1'
# to
#
# > "p"
#
# Answer with 'list3'.
#
# Write your code below and put the answer into the variable ANSWER.
#
list1[0] = "p"
list3 = list1





ANSWER = list3

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.7", ANSWER, False)

# --------------------------------------------------------------------------
# Section 3. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (3 points)
#
# Create a function that returns the list passed as argument sorted in
# numerical and ascending order. Also multiply all values with 10.
#
# Use the list:
#
# > [45, 22, 2, 498, 78]
#
# and the built-in method `sort()`.
#
# Answer with the sorted list.
#
# Write your code below and put the answer into the variable ANSWER.
#
prty = [45, 22, 2, 498, 78]
def megaTrip(gruy):
    ''' function '''
    gruy = sorted(gruy, key=int)
    lengG = len(gruy)
    for x in range(lengG):
        gruy[x] = gruy[x] * 10
    return gruy

prty = megaTrip(prty)





ANSWER = prty

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (3 points)
#
# Create a function that takes the list:
#
# > [45, 22, 2, 498, 78]
#
# as argument.
#
# The function should multiply all even numbers by 1 and add 6 to all odd
# numbers.
#
# Answer with the modified list sorted in numerical order, descending.
#
# Write your code below and put the answer into the variable ANSWER.
#

thgy = [45, 22, 2, 498, 78]
def evilF(ghds):
    ''' function '''
    lengh = len(ghds)
    for x in range(lengh):
        if(ghds[x]%2 == 0):
            ghds[x] = ghds[x]*1
        else:
            ghds[x] = ghds[x] + 6
    ghds.sort()
    ghds = ghds[::-1]
    return ghds
thgy = evilF(thgy)

ANSWER = thgy

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, False)


dbwebb.exit_with_summary()
