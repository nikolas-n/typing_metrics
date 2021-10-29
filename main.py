#!/bin/python3

# for timing
import time 
# for accepting one character at a time
import readchar
# for tokenizing
from nltk import word_tokenize 

text = ''
character = ''

start = time.time()

# end when enter is pressed (for now)
while character != readchar.key.ENTER:
	character = readchar.readkey()
	end = time.time()
	# catch backspace
	if character == readchar.key.BACKSPACE: 
		text = text[:-1]
	else:
		text += character
	if len(text) > 1:
		#print('       '+text,end='\r',flush=True)
		print('     '+text)
		print(str(round(len(word_tokenize(text))*60/(end-start)))+' wpm',end = '\r', flush=True)

print(text)

print('Averaged '+str(round(len(word_tokenize(text))*60/(end-start)))+' wpm')
