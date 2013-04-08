import random

#emilywang, nicolerifkin, mauracosman
#softdes!
#madlib generator

#Next task: finish blankage. Should incorporate a blankedword dictionary...where the key is the blanked word and the value is the part of speech. #Also, a catch for particles/notmadlibfriendly words in the blankedword dictionary.

def blankage(inputstory_str):
	#make while loops later to make this program typo-proof o.o
	#user can decide either random or "every nth number" blankage
	howtoblank= False #initial value-ing
	while howtoblank == False:
		try_rand = input("Do you want to have the madlib blanks spaced randomly throughout the text sample? Press 'y'/'n' and hit enter.")
		if try_rand == 'y':
			howtoblank = 'random'
		elif try_rand == 'n':
			try_int = input ("Would you rather have the madlib blanks placed every nth word? If so, how often? (specify a positive integer value) If not, press enter.")
			try:
				integer = int(try_int)
				howtoblank = integer	
			except:
				howtoblank = False
		
	# if howtoblank == 'random': #we'll blank randomly
	# if howtoblank != 'random' and type(howtoblank)==int: 
	# #we'll replace every nth word with a blank
	# else:
	# 	return False

def madlibbing():
	welcome = "Let's get down to business (to defeat the ___). Compose something and we'll turn it into a madlib. Results may vary (that's the point)."
	print (welcome)

	letsbegin = 0

	while letsbegin != 'y':
		letsbegin = input("If you would like to proceed, press 'y' and then the enter key. ")

	#whether you compose it yourself or scrape the text from a URL, the inputstory should be a string of sorts
	#inputstory = str(input("Write stuff here: "))

	#our test inputstory, by maura
	inputstory = 'There was once a strange creature wandering around Olin. It had the head of a cat and the body of an octopus. I decided to call it Octocat.'

	#turn the inputstory into a list, where each element is a word. this isn't very friendly to spacebar typos.
	#we chose a list rather than a dictionary because even though dictionaries are faster, we need the elements to be sequential.

	inputstory = inputstory.split()
	print (inputstory)

	blankage(inputstory)

	# while blanking == False:
	#  	blanking = blankage(inputstory, howtoblank)

	# return

madlibbing()
