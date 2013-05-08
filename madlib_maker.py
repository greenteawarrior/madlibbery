import random
import nltk
import urllib2
from bs4 import BeautifulSoup
from threading import Timer
import re
import sys
from termcolor import colored, cprint

#emilywang, nicolerifkin, mauracosman
#softdes!
#madlib generator

#If they don't want to play, let them say no. (i.e. letsmake and letsbegin)
#Manual Override Pos
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
	#print (tagged)

	blankable_poslist = ['NN', 'VB', 'VBP', 'JJ', 'RB']
	howmanyblanks = 0 #counter for current amount of blanks in madlib in progress

	blankables = 0
	for i in tagged:
		if i[1] in blankable_poslist:
			blankables = blankables + 1
	if blankables <= 2:
		print("We don't think that this text will make a good madlib. Please try again.")
		madlibbing()

	#print(blankables)

	while howmanyblanks < totalblanks and howmanyblanks < blankables:
		wordtoblank = random.choice(inputstory_list)
		wordtoblank_index = inputstory_list.index(wordtoblank)
		wordtoblank_pos = tagged[wordtoblank_index][1]#nltk stuff
		if wordtoblank_pos in blankable_poslist and wordtoblank != blank:
			howmanyblanks = howmanyblanks + 1
			blank_dict[wordtoblank] = (wordtoblank_index,wordtoblank_pos) #look up the part of speech here
			inputstory_list[wordtoblank_index] = blank
	return inputstory_list, blank_dict


def timing():
	print("If you need some inspiration, press 'i' and hit enter for a word that we like. ")

def playage(madlib):
	#unpacking the madlib
	madlib_list = madlib[0]
	blank_dict = madlib[1]
	pos_dict= {'NN': 'Noun', 'VB': 'Verb', 'VBP': 'Verb', 'JJ': 'Adjective', 'RB': 'Adverb'}
	noun_insp = ['Acoustic', 'Curve', 'Custard', 'Hen', 'Jaw', 'Bladder', 'Detail', 'Output', 'Polo', 'Sideboard', 'Single', 'Tiger', 'Fahrenheit', 'Lettuce', 'Owner', 'Parsnip', 'Path', 'Resolution', 'Sardine', 'Scarecrow', 'Badger', 'Butter', 'Coast', 'Difference', 'Jam', 'Loaf', 'Methane', 'Sense', 'Stew', 'Apology', 'Carpenter', 'Eyeliner', 'Form', 'Sister', 'Handsaw', 'Save', 'Softdrink', 'Study', 'Tent', 'Bath', 'Cast', 'Creature', 'Freighter', 'Nail', 'Pie', 'Repair', 'Request', 'Throat', 'Wolf', 'Ornament', 'Pan', 'Supply', 'Uncle', 'Wallet']
	verb_insp = ['Elicit', 'Save', 'Solve', 'Draw', 'Forecast', 'Execute', 'Travel', 'Research', 'Assume', 'Compile', 'Upheld', 'Differentiate', 'Sustain', 'Code', 'Fix', 'Replace', 'Import', 'Coordinate', 'Undertook', 'Supply', 'Devote', 'Secure', 'Customize', 'Disseminate', 'Resolve', 'Institute', 'Assist', 'Intervene', 'Investigate', 'Address', 'Care', 'Correlate', 'Model', 'Enumerate', 'Discriminate', 'Outline', 'Diagnose', 'Cooperate', 'Search', 'Accomplish', 'Teach', 'Interpret', 'Verify', 'Explore', ' Pioneer', 'Prevent', 'Visualize', 'Check', 'Establish', 'Distribute', 'Unify', 'Foster', 'Bargain', 'Renew', 'Expand', 'Upgrade', 'Experiment', 'Monitor', 'Moderate']
	adj_insp = ['Dusty', 'Superb', 'Weak', 'Female', 'Internal', 'Nostalgic', 'Uptight', 'Habitual', 'Woozy', 'Quiet', 'Thirsty', 'Fearful', 'Gleaming', 'Happy', 'Vagabond', 'Ill', 'Many', 'Deeply', 'Luxuriant', 'Present', 'Tall', 'Swanky', 'Clear', 'Tired', 'Fluffy', 'Blue-eyed', 'Average', 'Obscene', 'Parched', 'Uninterested', 'Important', 'Wooden', 'Late', 'Scattered', 'Materialistic', 'Alluring', 'Square', 'Sweltering', 'Capable', 'Gruesome', 'Maniacal', 'Periodic', 'Dashing', 'Whimsical', 'Overwrought', 'Future', 'Aquatic', 'Protective', 'Polite', 'Undesirable', 'Orange', 'Useful', 'Rich']
	adv_insp = ['Richly', 'Honorably', 'Ably', 'Magically', 'Abundantly', 'Nondescriptly', 'Hotly', 'Deafeningly', 'Viciously', 'Ferociously', 'Furiously', 'Hilariously', 'Basically', 'Parsimoniously', 'Royally', 'Readily', 'Strangely', 'Jokingly', 'Facetiously', 'Encouragingly', 'Enviously', 'Earsplittingly', 'Peacefully', 'Inquisitively', 'Tastefully', 'Incredibly', 'Beneficially', 'Defiantly', 'Tensely', 'Greatly', 'Firstly', 'Strongly', 'Gregariously', 'Prettily', 'Interestingly', 'Simply', 'Distinctly', 'Swiftly']
	print("Reach deep down into your soul and tell me a...")




	keyslist = blank_dict.keys()
	x = 0
	def inspiration():
#		if fillintheblank == 'i':
			if key_pos == 'Noun':
				print(random.choice(noun_insp))
			elif key_pos == 'Verb':
				print(random.choice(verb_insp))
			elif key_pos == 'Adjective':
				print(random.choice(adj_insp))
			elif key_pos == 'Adverb':
				print(random.choice(adv_insp))
	for key in blank_dict:
		key_pos=pos_dict[blank_dict[key][1]]
		filled = False
		while not filled:
			timeelapsed = Timer(15.0, timing)
			timeelapsed.start()
			fillintheblank=raw_input(key_pos + ': ')
			if x == 0:
				print
				print("To change your previous answer, press 'u' and hit enter")
				print
			if fillintheblank == 'i':
				inspiration()
				timeelapsed.cancel()
			elif fillintheblank == 'u' and x > 0:
				key_pos=pos_dict[blank_dict[keyslist[x-1]][1]]
				fillintheblank=raw_input(key_pos + ': ')
				timeelapsed.cancel()
				if fillintheblank == 'i':
					inspiration()
				else:
					madlib_list[blank_dict[keyslist[x-1]][0]]=colored(fillintheblank, 'red', attrs = ['reverse', 'blink'])
			else:
				madlib_list[blank_dict[key][0]]=colored(fillintheblank, 'red', attrs = ['reverse', 'blink'])
				filled = True
				timeelapsed.cancel()
		x += 1
	timeelapsed.cancel()
	return madlib_list

def madlibbing():
	print	
	make_welcome = "Let's get down to business (to defeat the ___). Compose something and we'll turn it into a madlib. Results may vary (that's the point)."
	print (make_welcome)
	letsmake = 0

	while letsmake != 'y':
		letsmake = raw_input("If you would like to proceed, press 'y' and then the enter key. ")

	print
	print("Would you like to use one of our Madlib stories, or create your own, or use a random wikipedia article?")
	print
	inputstory = False
	while inputstory == False:
		inputstorytype = raw_input("Type 'yours' to use a story we've written. Type 'mine' to write or paste a story yourself. Type 'wiki' to turn the text from a random wikipedia article into a madlib ")
		if inputstorytype == 'yours':
			inputstory = 'There was a strange creature wandering around Olin. It had the head of a cat and the body of an octopus. I decided to call it Octocat.'
		elif inputstorytype == 'mine':
			inputstory = raw_input("Type or paste your story here ") #check to make sure that entry is valid
			while len(inputstory.split()) <= 10:
				print(inputstory)
				print ("We don't think that story is long enough to produce a fun madlib. Please extend it or write another.")
				inputstory = raw_input("Type or paste your story here ")
		elif inputstorytype == 'wiki':
			url = 'http://www.wikipedia.org/wiki/Special:random'
			req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
			con = urllib2.urlopen( req ).read()
			results = re.findall('<p>(.*)</p>', con)
			wikipediatxt = results[0]
			inputstory = BeautifulSoup(wikipediatxt).get_text()
			print
			titlehtml = re.findall('<title>(.*)- Wikipedia', con)
			print
			print('The title of your madlib is: ' + str(titlehtml)[2:-2])
			# print(newdata)
			# a = newdata.strip('\n')
			# inputstory = a.strip('')

	inputstory_list = inputstory.split() 
	#turn the inputstory into a list, where each element is a word. this isn't very friendly to spacebar typos.
	#we chose a list rather than a dictionary because even though dictionaries are faster, we need the elements to be sequential.

	madlib = False
	while madlib == False:
		madlib = blankage(inputstory_list)

	print("Your madlib is now ready (freshly out of the oven and smells ______, if I might add). Would you like to play? ")
	print
	letsplay = 0
	while letsplay != 'y':
		letsplay = raw_input("If you would like to proceed, press 'y' and then the enter key. ")

	playing = False
	while playing == False:
		playing = playage(madlib)

	print
	print ("Hurray, madlib complete!")

	finishedmadlib = ''
	for word in playing:
		finishedmadlib += word + ' '

	showme = 0
	while showme != 'y':
		showme = raw_input("Press y to read the _____ly finished product.")

	print
	print (finishedmadlib)

madlibbing()
