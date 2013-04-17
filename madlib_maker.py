import random
import nltk

#emilywang, nicolerifkin, mauracosman
#softdes!
#madlib generator

#Next task: finish blankage. Should incorporate a blankedword dictionary...where the key is the blanked word and the value is the part of speech. #Also, a catch for particles/notmadlibfriendly words in the blankedword dictionary.

def blankage(inputstory_list):
	#make while loops later to make this program typo-proof o.o
	#user can decide either random or "every nth number" blankage
	howtoblank= False #initial value-ing
	while howtoblank == False:
		try_rand = raw_input("Do you want to have the madlib blanks spaced randomly throughout the text sample? Press 'y'/'n' and hit enter.")
		if str(try_rand) == 'y':
			howtoblank = 'random'
		elif try_rand == 'n':
			try_int = raw_input ("Would you rather have the madlib blanks placed every nth word? If so, how often? (specify a positive integer value) If not, press enter.")
			try:
				integer = int(try_int)
				howtoblank = integer	
			except:
				howtoblank = False
		
	blank = '_____' #this is a string of five underscores
	blankedoutwords_dict = {}
	tagged = nltk.pos_tag(inputstory_list)
	blankable_poslist = ['NN', 'VBD', 'VBP', 'JJ', 'RB']
	if howtoblank == 'random': #we'll blank randomly
		totalblanks = len(inputstory_list) / 5.0 #total amount of blanks desired
		howmanyblanks = 0 #counter for current amount of blanks in madlib in progress
		while howmanyblanks <= totalblanks:
			wordtoblank = random.choice(inputstory_list)
			wordtoblank_index = inputstory_list.index(wordtoblank)
			wordtoblank_pos = tagged[wordtoblank_index][1]#nltk stuff
			if wordtoblank_pos in blankable_poslist:
				howmanyblanks = howmanyblanks + 1
				blankedoutwords_dict[wordtoblank] = (wordtoblank_index,wordtoblank_pos) #look up the part of speech here
				inputstory_list[wordtoblank_index] = blank
		return inputstory_list, blankedoutwords_dict
			
	
	elif howtoblank != 'random' and type(howtoblank)==int: #if it's not random, we want to replace every nth word with a blank; n=howtoblank 
		wordtoblank_index = howtoblank #initialize
		howmanyblanks = 0
		while wordtoblank_index%howtoblank != len(inputstory_list)%howtoblank:
			wordtoblank = inputstory_list[wordtoblank_index]
			wordtoblank_pos = tagged[wordtoblank_index][1]
			if wordtoblank_pos in blankable_poslist:
				howmanyblanks = howmanyblanks + 1
				print (howmanyblanks)
				blankedoutwords_dict[wordtoblank] = (wordtoblank_index,wordtoblank_pos) #look up the part of speech here
				inputstory_list[wordtoblank_index] = blank
				#increment wordtoblank_index
		return inputstory_list, blankedoutwords_dict

	else:
	  	return False

def madlibbing():
	welcome = "Let's get down to business (to defeat the ___). Compose something and we'll turn it into a madlib. Results may vary (that's the point)."
	print (welcome)

	letsbegin = 0

	while letsbegin != 'y':
		letsbegin = raw_input("If you would like to proceed, press 'y' and then the enter key. ")

	#whether you compose it yourself or scrape the text from a URL, the inputstory should be a string of sorts
	#inputstory = str(input("Write stuff here: "))

	#our test inputstory, by maura
	inputstory = 'There was once a strange creature wandering around Olin. It had the head of a cat and the body of an octopus. I decided to call it Octocat.'

	#turn the inputstory into a list, where each element is a word. this isn't very friendly to spacebar typos.
	#we chose a list rather than a dictionary because even though dictionaries are faster, we need the elements to be sequential.

	inputstory_list = inputstory.split()

	x = blankage(inputstory_list)
	print(x)

	# while blanking == False:
	#  	blanking = blankage(inputstory, howtoblank)

	# return

madlibbing()
