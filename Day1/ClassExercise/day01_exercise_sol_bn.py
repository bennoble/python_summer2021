# Fibonacci sequence
# X_[i] = X_[i-1] + X_[i-2], where X_1 = 1, X_2 = 1
# 1,1,2,3,5,8,....

# Write a for loop, while loop, or function (or all three!) to create a
# list of the first 10 numbers of the fibonacci sequence

def fib(n):
	fib = [1,1]
	first = fib[0]
	second = fib[1]
	n -=2
	for i in range(n):
		x = first + second
		fib.append(x)
		first = second
		second = x
	return(fib)

fib(10)

"""return true if there is no e in 'word', else false"""
def has_no_e(word):
	for w in word:
		if w == 'e':
			return False
	return True

has_no_e('rate')
has_no_e('rat')


"""return true if there is e in 'word', else false"""
def has_e(word):
	if has_no_e(word) == True:
		return False
	else: return True

has_e('rate')
has_e('rat')

"""return true if word1 contains only letters from word2, else false"""
def uses_only(word1, word2):
	for w in word1:
		if w not in word2:
			return False
	else: return True

uses_only('rat', 'rate')
uses_only('block', 'rate')


"""return true if word1 uses all the letters in word2, else false"""
def uses_all(word1, word2):
	w1_letters = [w for w in word1]
	w2_letters = [w for w in word2]
	for i in w2_letters:
		if i not in w1_letters:
			return False
	else: return True

uses_all('rat', 'rate')
uses_all('rate', 'rat')  

"""true/false is the word in alphabetical order?"""
# Hint: check the methods for lists
def is_abecedarian(word):
	if word == ''.join(sorted([w for w in word])):
		return True
	else: return False

is_abecedarian('rate')
is_abecedarian('abe')


