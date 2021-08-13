import string

# Raising errors is more common when developing ------------------------

## These functions all take a single string as an argument.
## Presumably your code won't work for an int
## raise a built-in (or custom!) exception if fed an int

## 1. then code for the following functions
## 2. write one test for each function and run it in the script

## make all characters capitalized
def shout(txt):
	txt_u = ''.join([i for i in txt.upper()])
	return txt_u

shout('hi')

## reverse all characters in string
def reverse(txt):
	txt_r = txt[::-1]
	return txt_r

reverse('hello')  

## reverse word order in string and return as one string
def reversewords(txt):
	return ' '.join(txt.split()[::-1])

reversewords('one two three')

## reverses letters in each word but not word order
def reversewordletters(txt):
	return reversewords(reverse(txt))

reversewordletters('one two three')


import unittest

class Test_funcs(unittest.TestCase):
    
    def test_shout(self): 
        self.assertEqual(shout('foo'), 'FOO')
    
    def test_reverse(self):
        self.assertEqual(reverse('hello'), 'olleh') 

    def test_reversewords(self):
    	self.assertEqual(reversewords('hello there'), 'there hello') 
    
    def test_reversewordletters(self):
    	self.assertEqual(reversewordletters('hello there'), 'olleh ereht') 

if __name__ == '__main__': 
    unittest.main()



## Try/catch is more common when using
## someone else's code, scraping, etc. -----------------------------------

## Loop over this string and apply the reverse() function.
## Should throw errors if your exceptions are being raised!
## Write a try/catch to handle this.
 
string_list = ["hi", "hello there", 5, "hope this works", 100, "will it?"]


reversed_list = []
for i in range(len(string_list)):
	try:
		reversed_list.append(reverse(string_list[i]))
	except TypeError:
		print('TypeError at ' + str(i))

print(reversed_list)


		
			
			
			
			
			
			

