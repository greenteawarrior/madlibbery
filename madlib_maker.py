import random
import nltk
import urllib2
from bs4 import BeautifulSoup

#emilywang, nicolerifkin, mauracosman
#softdes!
#madlib generator

#If they don't want to play, let them say no. (i.e. letsmake and letsbegin)
#make sure they can't ask for more madlibs than possible
def blankage(inputstory_list):
	#make while loops later to make this program typo-proof o.o
	howtoblank= False #initial value-ing
	while howtoblank == False:
		totalblanks = raw_input("How many blanks would you like in your madlib?")
		try:
			totalblanks = int(totalblanks)
			howtoblank = True	
		except:
			howtoblank = False
		
	blank = '_____' #this is a string of five underscores
	blank_dict = {}
	tagged = nltk.pos_tag(inputstory_list)

	blankable_poslist = ['NN', 'VB', 'VBP', 'JJ', 'RB']
	howmanyblanks = 0 #counter for current amount of blanks in madlib in progress
	
	while howmanyblanks < totalblanks:
		wordtoblank = random.choice(inputstory_list)
		wordtoblank_index = inputstory_list.index(wordtoblank)
		wordtoblank_pos = tagged[wordtoblank_index][1]#nltk stuff
		if wordtoblank_pos in blankable_poslist and wordtoblank != blank:
			howmanyblanks = howmanyblanks + 1
			blank_dict[wordtoblank] = (wordtoblank_index,wordtoblank_pos) #look up the part of speech here
			inputstory_list[wordtoblank_index] = blank
	return inputstory_list, blank_dict

def playage(madlib):
	#unpacking the madlib
	madlib_list = madlib[0]
	blank_dict = madlib[1]
	pos_dict= {'NN': 'Noun', 'VB': 'Verb', 'VBP': 'Present Tense Verb', 'JJ': 'Adjective', 'RB': 'Adverb'}
	print("Reach deep down into your soul and tell me a...")
	for key in blank_dict:
		key_pos=pos_dict[blank_dict[key][1]]
		fillintheblank=raw_input(key_pos + ': ')
		madlib_list[blank_dict[key][0]]=fillintheblank
	print(madlib_list)
	print(blank_dict)

def madlibbing():
	make_welcome = "Let's get down to business (to defeat the ___). Compose something and we'll turn it into a madlib. Results may vary (that's the point)."
	print (make_welcome)

	letsmake = 0

	while letsmake != 'y':
		letsmake = raw_input("If you would like to proceed, press 'y' and then the enter key. ")

	print("Would you like to use one of our Madlib stories, choose one from elsewhere, or create your own?")
	inputstory = False
	while inputstory == False:
		inputstorytype = raw_input("Type 'yours' to use a story we've written. Type 'mine' to write or paste a story yourself. Type 'url' to turn the text from a website URL into a madlib")
		if inputstorytype == 'yours':
			inputstory = 'There was a strange creature wandering around Olin. It had the head of a cat and the body of an octopus. I decided to call it Octocat.'
			print(inputstory)
		elif inputstorytype == 'mine':
			inputstory = raw_input("Type or paste your story here") #check to make sure that entry is valid
			print(inputstory)
		elif inputstorytype == 'url':
			url = raw_input("Paste a valid url here")
			try:
				data = urllib2.urlopen(url).read()
				newdata= BeautifulSoup(data).get_text()
				a = newdata.strip('\n')
				inputstory = a.strip('')
				print(inputstory) 
			except:
				print("That is not a valid url.")
				inputstory = False

	inputstory_list = inputstory.split() 
	#turn the inputstory into a list, where each element is a word. this isn't very friendly to spacebar typos.
	#we chose a list rather than a dictionary because even though dictionaries are faster, we need the elements to be sequential.

	madlib = False
	while madlib == False:
		madlib = blankage(inputstory_list)

	print("Your madlib is now complete (freshly out of the oven and smells ______, if I might add). Would you like to play?")

	letsplay = 0

	while letsplay != 'y':
		letsplay = raw_input("If you would like to proceed, press 'y' and then the enter key. ")

	playing = False
	while playing == False:
		playing = playage(madlib)


madlibbing()
