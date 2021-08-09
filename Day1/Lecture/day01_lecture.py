# Python - 2021 Summer Course
# Day 1
# Topic: Syntax, Loops, and Functions
# Instructor: Ben Noble
# Former Instructors: Patrick Cunha Silva, Ryden Buttler, 
# 					  Erin Rossiter, Michele Torres
#					  David Carlson, and Betul Demirkaya

# First Instructor: Matt Dickenson

#-------- Types of Objects --------#

# Variable: A simple object, for example, a = 1 
# List: [], A list is a collection of objects 
#			which is ordered and mutable 
# Tuple: (), A tuple is a collection of objects 
#	    which is ordered and immutable 
# Dictionary: {}, A dictionary is a collection which 
# 			 is unordered, changeable and indexed objects

#---------- Operators  ----------#

# Addition					x + y	
# Subtraction				x - y	
# Multiplication			x * y	
# Division					x / y	
# Modulus					x % y	
# Exponentiation  			x ** y	
# Floor division			x // y
# Equal						x == y	
# Not equal					x != y	
# Greater than				x > y	
# Less than					x < y	
# Greater than or equal to	x >= y	
# Less than or equal to		x <= y

# and, Returns True if both statements are true
# or, Returns True if one of the statements is true
# not, Reverse the result, returns False if the result is true
# is, Returns True if both variables are the same object
# in, Returns True if a sequence with the specified value is present in the object

# See https://www.w3schools.com/python/python_operators.asp for a complete list.


#---------- Strings ----------#

# Single Quotes
name = 'Ben'
# Double Quotes 
age = "30"
# Combining strings, using .format{}
intro =  "Hi, my name is {}. I'm {} years old.".format(name, age)
print(intro)
# Combining strings, using +
intro = "Hi, I'm " + name + ", I'm " + age
print(intro)
# Triple Quotes, it produces a string that spans multiple lines
new_intro = """Hello!,
I'm Ben. 
What's up?"""
new_intro # representation
print(new_intro) # print method


# Characters in a string are indexable
intro[0] 
intro[2]
intro[4] 

# Strings are immutable, we cannot replace a character in a string
name[0] = "a"

# But, we can use a string to modify itself
name = name + 'jamin'
print(name)

# We can also use +=
name += ' Noble'
print(name)

# Though strings are immutable, we can split them
name.split() # Using ' ' as the default separator

# We can use any separator
name.split('n') ## Using 'a' as separator
new_intro.split('\n') ## Using line break as separator

# We can index using negative numbers 
wustl = 'WashingtonUniversity'
wustl[-1] 

# Check how the characters are positioned...
#  0   1   2   3   4   5   6   7   8   9  10 11 12 13 14 15 16 17 18 19
#  W   a   s   h   i   n   g   t   o   n   U  n  i  v  e  r  s  i  t  y
#-20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
# Notice that W is 0, but y is -1

# We can recover multiple characters from a string:
wustl[2:] ## index 2 through end
wustl[-2:] ## index -2 through end
wustl[:2] ## up to index 2
wustl[:-2] # up to index -2
wustl[::2] ## sequence, every other
wustl[::-2] ## sequence, every other from the end
wustl[::3] ## sequence, every third from beginning
wustl[1:8] # sequence, from index 1 to 7, remember: Python indexes are n through i exclusive; we drop the 'W' (index 0) and do not include 'o' (index 8)

# We can use a loop to split a string into characters
[letter for letter in wustl] # the output is a list, more on this below

# We can join strings in a list using join
wustl_chr = [i for i in wustl] 
wustl_chr
'-'.join(wustl_chr) # the output is a string

#---------- Integers ----------#

# We can use all mathematical operators with them
# Integers are not rounded down in Python 3
3/2 # the result is a float
type(3)
type(3/2)

# But, we can round down using floor division //
whole = 5//3 # the result is an integer
type(whole)
whole
remainder = 5%3
print("Five divided by three is {} and {} fifths".format(whole, remainder)) # Or
print("Five divided by three is %d and %d fifths" % (whole, remainder)) 

# these two formats are similar, however, format is more flexible in many instances (it did not exist prior to python 2.5)
print('This will print both a string: {} and a number: {}'.format(name, whole))
print('This will print both a string: %s and a number %d' % (name, whole))
print('This will cause an error: %d, %d' % (name, whole))

# As with strings, the assignment is flexible
five = 5
five += 1
print(five)
five /= 3
print(five)
five -= 1
print(five)
five *= 2
print(five)
type(five)
#---------- Floats ----------#

# Real numbers
# Add decimal to integer
type(12) # integer
type(12.0) # float

# In Python 3, these are equal. But they are different in Python 2
12/5 == 12.0/5
12 == 12.0

# Ultimately, you will be using Python 3, but it is good to know these facts if you pick up someone else's Python 2 code or work with some who is more familar with Python 2 (just like differences between Base R and Tidy R)

#---------- Lists ----------#

# A list is a collection of objects which is ordered and mutable 
# Lists can be changed
# Lists can include multiple object types
# Lists will probably be your go-to storage in Python
# Similar to vectors in R, but more flexible

wustl_chr 
type(wustl_chr)

# We can add a new element to a list using the method append()
wustl_chr.append('P')
wustl_chr

# Lists can include multiple types of objects
wustl_chr.append(1)
wustl_chr.append(['1'])
wustl_chr

# We can index lists
wustl_chr[0]
wustl_chr[-1][0]
wustl_chr[:2]

# We can also replace objects in a list
wustl_chr[0] = 'X'
wustl_chr

# We can use len() to get the length of a list
len(wustl_chr)

# But, be careful because indexing starts at 0
print(wustl_chr[len(wustl_chr)]) # IndexError
print(wustl_chr[len(wustl_chr) - 1]) # Return the object at the last index

# We can insert into any position using the method inset()
wustl_chr.insert(15, "!")
wustl_chr

# We can also remove from any position
wustl_chr.pop(1)
wustl_chr

# We can remove the object at the last index using 
wustl_chr.pop()
wustl_chr

# We can also remove using a value with the method remove()
# but notice, this removes the first instance
wustl_chr.remove('n')
wustl_chr

# We can remove all instances from a list using list syntax
# More on this later
wustl_chr = [i for i in wustl_chr if i != 'i']

# We can check all the methods and attributes in a list using
dir(wustl_chr)

#---------- Tuples ----------#

l = [7, 'a', '6']


# Tuple: (), A tuple is a collection of objects which is ordered and immutable 
# Not very common, but useful occasionally and will appear from time to time

# We use () to create a tuple
tup = (1, 'a', 'a', 11, 6, 5, 'Apple', ['python', 'R'])

# We can index tuples
print(tup[1])

# But, we can't modify
tup[1] = 10000 ## !!!
tup.append(10000) ## !!

# Let's check the methods available for tuples
dir(tup)

# We can count the number of times that an element appears 
tup.count('a')

#---------- Dictionary ----------#

# A dictionary is a collection which is unordered, changeable and indexed 

# We use {} to create a dictionary
myInfo = {"name" : "ben", "age" : 30, "research" : ["presidency", "congress"]}

# We call elements using keys.
myInfo
myInfo.keys() # return the dictionary's key
myInfo.values() # return the dictionary's value

# We cannot use index
myInfo[0] ##!!!

# We can call entries by key
myInfo["research"]

# We can add new elements to a dictionary
myInfo["last_name"] = "noble"
myInfo

# We can modify elements
myInfo["name"] = 'benjamin'
myInfo["research"] = 'american politics'
myInfo

#---------- Booleans and Conditionals ----------#

# Perform an operation (or several) if condition is met (or not)
x = 1

if x == 1:
	print('x is one')
elif x == 2:
	print('x is two')
else:
	print('x is neither one nor two')

# Multiple lines of code:
# - Indentation matters!
# - Even an empty line with spaces can cause errors, 
#   Python is very picky about this
if x == 1:
	print('x is one')
elif x == 2:
	print('x is two')
else:
	print('x is neither one nor two') # IndentationError

# Can be conditions or boolean (True or False)
True == (1 == 1.0)
True == (1 != 1.0)
False == (1 != 1.0)

#---------- Loops ----------#

# Two types of loops: for and while
# for loop: loops over iterable objects
# while loop: runs until condition is met 

# A string is an iterable object
for i in wustl:
	print(i)

# We can iterate over a dictionary items in Python 3
for i in myInfo.items():
	print(i) # Tuples!

# And keys:
for i in myInfo.keys():
	print(i)

for i in myInfo.values():
	print(i)


# We can unpack the elements of a dictionary
for k, q in myInfo.items():
	print(k, '->', q)

# Sometimes is useful to write a short version of the for loop
sum([.05**i for i in range(1,10)]) # What is happening here?

mynum = [] # instantiate an empty list
for i in range(1,10):
	mynum.append(.05**i)
mynum
sum(mynum) # Sum the values in the list

sum(mynum) == sum([.05**i for i in range(1,10)])

# While loop: loops while condition is true
while len(wustl_chr)>1:
	wustl_chr.pop()
# What happened to wustl_chr?
wustl_chr 

# Be careful with while loops, they can go forever
# in ipython or terminal, stop with 'control + c'
while True:
	print(i)

# Useful statements when using loops:
# break: stop the loop and go to the previous level
for i in range(1, 10):
	if i == 5:
		break
	print(i)


for j in ['a', 'b', 'c']:
	print(j)
	for i in range(1, 10):
		if i == 5:
			break
		print(i)

# pass: continue the evaluation to the next level
for i in range(1, 10):
	if i == 5:
		pass
		print('I have a 5')
	print(i)

for i in range(1,10):
	if i == 5:
		print(i)
	else:
		pass


# continue: skip the evaluation and return to the same level
for i in range(1, 10):
	if i != 5:
		print(i)


#---------- Functions ----------#

# Use them to write cleaner code 
# keep them simple
# We can return any type of object
# Don't forget to add return for output


func <- function(x){
	doing stuff
}

# Input, output
def add_squares(x = 2, y = 2):
	return x**2 + y**2

add_squares()

# Now, without defaults
def add_squares_2(x, y):
	x += 1
	return x**2 + y**2

add_squares_2(1,2)

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
