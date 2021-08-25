# Python - 2021 Summer Course
# Day 8
# Topic: Complexity, Recursion, and Sorting
# Instructor: Ben Noble
# Former Instructors: Patrick Cunha Silva, Ryden Buttler, 
#                     Erin Rossiter, Michele Torres
#                     David Carlson, and Betul Demirkaya
# First Instructor: Matt Dickenson


#---------- Recursion ----------#

# Function calls itself
# You need to know
#   - the base case
#   - when to call the function
#   - when to stop
# The typical example is (n)! = n * (n-1) * (n-2)...
# A physical world example would be to place two parallel mirrors
#   facing each other. Any object in between them would be reflected 
#   recursively. 
# Why recursion? Why not recursion?
#   Make the code look clean
#   Sequence generation is easier
#   Logic behind is hard to follow sometimes
#   Recursiveness is expensive and inefficient uses a lot of memory
#   Hard to debug
# Source: https://www.programiz.com/python-programming/recursion

# Example, Factorial:
# n! = n * (n-1) * (n - 2) * ... * 2 * 1

# def nFactorial(n):
#   if base case:
#       return something
#   else:
#       return a recursive call

def nFactorial(n):
    if n == 1:
        return n
    else: 
        return n * nFactorial(n = n-1)
nFactorial(5)

# How does it work?
# n = 5, so return 5 * f(4)
# n = 4, so return 5 * 4 * f(3)...
# ...
# n = 1 so return n = 5 * 4 * 3 * 2 * 1 = 120

# Using factorial from math
import math
math.factorial(5)

#---------- Recursive Fibonacci Sequence ----------#

# Find n'th number in fibonacci sequence
# 1, 1, 2, 3, 5, 8, 13, 21...
def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)

fib(3)

# How does this work?
# fib(0): 0 <= 1, n = 0 
# fib(1): 1 <= 1, n = 1
# fib(2): 2 > 1...
    # return fib(1) + fib(0) = 1 + 0 = 1 
# fib(3): 3 > 1... 
    # return fib(2) + fib(1) = fib(1) + fib(0) + 1 = 1 + 0 + 1 = 2

for i in range(9):
    print("{0} : {1}".format(i, fib(i)))


# We are going to change directions now and discuss 
# searching and sorting algortithms. Although you
# will not necessarily need to worry about creating
# your own (as many good ones exist), this is a valuable
# lesson for thinking about complexity—both time and
# storage, see for a good overview: 
# https://python-textbok.readthedocs.io/en/1.0/Sorting_and_Searching_Algorithms.html

#---------- Search Algorithms ----------#
import random

# 1 - Linear Search:
# returns element in a list and its position
def linear_search(mylist, element):
    steps = 0
    for item in mylist:
        steps += 1
        if item == element:
            print(steps)
            return item

mylist = list(range(26))
random.shuffle(mylist)

linear_search(mylist, 1)
linear_search(mylist, 5)
linear_search(mylist, 10)

# 2 - Binary Search:
# returns element if it is in sorted list
def binary_search(sorted_list, element):
    print("Input list is {0}".format(sorted_list))
    print("Input size is {0}".format(len(sorted_list)))
    middle = len(sorted_list)//2
    median = sorted_list[middle]
    if len(sorted_list) <= 1:
        if element == median:
            return median
        else:
            return 'No such element'
    if element < median:
        left = sorted_list[0:middle]
        return binary_search(sorted_list = left, element = element)
    else: 
        right = sorted_list[middle:]
        return binary_search(sorted_list = right, element = element)

mylist = range(0, 1000, 2)
binary_search(mylist, 72)
binary_search(mylist, 71)

#---------- Sorting ----------#

my_numbers = [1, 9, 8, 5, 4, 6, 0, 2, 3, 7]

# Selection Sort
# 1) Find minimum of the unsorted list
# 2) Remove minimum and place it in first element on new list
# 3) Repeat until unsorted list is empty

def selection_sort(numbers):
    # Answer object 
    numbers = numbers.copy()  # to not modify the original input
    answer = []
    while len(numbers) > 0:
        answer.append(min(numbers))
        # syntax I showed you the other day to find 
        # items by index position
        del numbers[numbers.index(answer[-1])]    
    return answer

selection_sort(numbers = my_numbers)


# Bubble Sort
# 1) Compare first two contiguous elements, swap if necessary
# 2) Compare next two contiguous elements, swap if necessary
# 3) Continue until end of list
# 4) If swaps occurred in steps 1 - 3, repeat for first n - 1 elements
# Not the most efficient
# Source: https://stackabuse.com/bubble-sort-in-python

def bubble_sort(numbers):
    answer = numbers.copy()
    # We go through the list as many times as there are elements
    for i in range(len(answer)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(answer) - 1):
            if answer[j] > answer[j+1]:
                # Swap
                answer[j], answer[j+1] = answer[j+1], answer[j]
        # print(answer)
    return answer

bubble_sort(my_numbers)

# Bogo Sort
# 1) Randomize number order
# 2) If sorted: stop; else: repeat
# Very silly, very inefficient

import random 

my_numbers2 = [8, 2, 1, 3, 4]

def bogo_sort(numbers):
    n = 0
    answer = numbers.copy() 
    while answer != sorted(numbers):
      random.shuffle(answer)
      n += 1 
      steps = n
    return answer, steps

bogo_sort(my_numbers2)


#---------- Complexity ----------#

# The amount of time/the number of operations need to complete a task.
# O(n) notation:
#   - Big-O notation is a relative representation of the complexity of 
#     an algorithm.
#   - Classify algorithms according to how their running time 
#     or space requirements grow as the input size
#   - Informally, we can think of the Big-O notation as 
#     the run time in the worst case scenario 

# See Towards Data Science for more 
# information on the Big O notation:
# https://bit.ly/3iYs4kb 
# Another good resource: https://www.freecodecamp.org/news/big-o-notation-why-it-matters-and-why-it-doesnt-1674cfa8a23c/

# Table of common time complexities:

#       Name        Time Complexity

#   Constant Time         O(1)
# Logarithmic Time      O(log n)
#    Linear Time          O(n)
# Quasilinear Time     O(n log n)
#  Quadratic Time        O(n^2)
# Exponential Time       O(2^n)
#  Factorial Time         O(n!) 

from datetime import datetime

s = [i for i in range(10)]
l = [i for i in range(1000)]

# Examples:
# O(1) - Constant Time:
# Independent of the size of x
def o_1(x):
    out = x[0] + 1 
    return out

o_1(s)
o_1(l)

# O(n) - Linear Time:
# Linearly increases with the size of x
def o_n(x):
    for i in range(len(x)):
        x[i] += 1 
        return x

o_n(s)
o_n(l)

# O(n^2) - Quadratic Time:
# increases at a rate of x^2 for each additional 
# item we add to x since we loop twice

def o_nsqr(x): 
    out = []
    for i in range(len(x)): 
        for j in range(len(x)):
          out.append(i + j) 
    return out

o_nsqr(s)
o_nsqr(l)


# O(2^n) - Exponential Time:
# for every increase in x, we are creating
# many more recurisons
def fib(x): 
  if x <= 1: 
      return x
  return fib(x - 1) + fib(x - 2)

fib(10)
fib(35)

# Graphically
import matplotlib.pyplot as plt
import math
import numpy as np
import array

n = list(range(1, 11))
O1 = [1 for i in n]
OLogN = [math.log(i) for i in n]
OnLogN = [i * math.log(i) for i in n]
On2 = [i * 2 for i in n]
O2n = [2 ** i for i in n]
OnF = [math.factorial(i) for i in n]

plt.plot(n, O1, 'r-', label = "O(1)")
plt.plot(n, OLogN, 'b-', label = "O(Log n)")
plt.plot(n, OnLogN, 'g-', label = "O(n Log n )")
plt.plot(n, On2, 'y-', label = "O(2n)")
plt.plot(n, O2n, 'p-', label = "O(n^2)")
plt.plot(n, OnF, 'k-', label = "O(n!)")
plt.xlim(1, 10)
plt.ylim(1, 100)
plt.xlabel('N')
plt.ylabel('Big O')
plt.legend()
plt.show()


#---------- Plotting ----------#

#pip install matplotlib

import matplotlib.pyplot as plt

# x-axis: # of elements in list
x1 = range(1, 101) 
x2 = range(1, 101) 
# y-axis: time
y1 = range(1, 101) 
y2 = [i * 0.5 for i in range(1, 101)]
# adjust the area around the plot
plt.subplots_adjust(left = .13, right = .95, top = .9, bottom = .3) 
# Plot the data
plt.plot(x1, y1)
plt.plot(x2, y2)
# Add a legend
plt.legend(['1', '2'], loc = "upper left", prop = {"size":10})
# y label
plt.ylabel("Y")
# x label
plt.xlabel("X")
# plot title
plt.title("The Effect of Different Sort Algorithms on Runtime")
# plot description
txt = """
Maybe a description here
"""
plt.figtext(.5, .05, txt, fontsize = 10, ha = "center")
# Display plot, use the option block=False
# otherwise you will need to close the plot manually
plt.show(block=False)
# Save plot
plt.savefig('/Users/bennoble/Desktop/plot.pdf')
# Close plot
plt.close()



# Copyright of the original version:

# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.