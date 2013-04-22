import random
import nltk
import urllib2
from bs4 import BeautifulSoup
import time

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
	#print(blankables)

	while howmanyblanks < totalblanks and howmanyblanks < blankables:
		wordtoblank = random.choice(inputstory_list)
		wordtoblank_index = inputstory_list.index(wordtoblank)
		wordtoblank_pos = tagged[wordtoblank_index][1]#nltk stuff
		if wordtoblank_pos in blankable_poslist and wordtoblank != blank:
			howmanyblanks = howmanyblanks + 1
			blank_dict[wordtoblank] = (wordtoblank_index,wordtoblank_pos) #look up the part of speech here
			inputstory_list[wordtoblank_index] = blank
	
	#print (blank_dict)

	return inputstory_list, blank_dict

def playage(madlib):
	print (madlib)
	#unpacking the madlib
	madlib_list = madlib[0]
	blank_dict = madlib[1]
	pos_dict= {'NN': 'Noun', 'VB': 'Verb', 'VBP': 'Verb', 'JJ': 'Adjective', 'RB': 'Adverb'}
	noun_insp = ['Acoustic', 'Curve', 'Custard', 'Hen', 'Jaw', 'Bladder', 'Detail', 'Output', 'Polo', 'Sideboard', 'Single', 'Tiger', 'Fahrenheit', 'Lettuce', 'Owner', 'Parsnip', 'Path', 'Resolution', 'Sardine', 'Scarecrow', 'Badger', 'Butter', 'Coast', 'Difference', 'Jam', 'Loaf', 'Methane', 'Sense', 'Stew', 'Apology', 'Carpenter', 'Eyeliner', 'Form', 'Sister', 'Handsaw', 'Save', 'Softdrink', 'Study', 'Tent', 'Bath', 'Cast', 'Creature', 'Freighter', 'Nail', 'Pie', 'Repair', 'Request', 'Throat', 'Wolf', 'Ornament', 'Pan', 'Supply', 'Uncle', 'Wallet']
	verb_insp = ['Elicit', 'Save', 'Solve', 'Draw', 'Forecast', 'Execute', 'Travel', 'Research', 'Assume', 'Compile', 'Upheld', 'Differentiate', 'Sustain', 'Code', 'Fix', 'Replace', 'Import', 'Coordinate', 'Undertook', 'Supply', 'Devote', 'Secure', 'Customize', 'Disseminate', 'Resolve', 'Institute', 'Assist', 'Intervene', 'Investigate', 'Address', 'Care', 'Correlate', 'Model', 'Enumerate', 'Discriminate', 'Outline', 'Diagnose', 'Cooperate', 'Search', 'Accomplish', 'Teach', 'Interpret', 'Verify', 'Explore', ' Pioneer', 'Prevent', 'Visualize', 'Check', 'Establish', 'Distribute', 'Unify', 'Foster', 'Bargain', 'Renew', 'Expand', 'Upgrade', 'Experiment', 'Monitor', 'Moderate']
	adj_insp = ['Dusty', 'Superb', 'Weak', 'Female', 'Internal', 'Nostalgic', 'Uptight', 'Habitual', 'Woozy', 'Quiet', 'Thirsty', 'Fearful', 'Gleaming', 'Happy', 'Vagabond', 'Ill', 'Many', 'Deeply', 'Luxuriant', 'Present', 'Tall', 'Swanky', 'Clear', 'Tired', 'Fluffy', 'Blue-eyed', 'Average', 'Obscene', 'Parched', 'Uninterested', 'Important', 'Wooden', 'Late', 'Scattered', 'Materialistic', 'Alluring', 'Square', 'Sweltering', 'Capable', 'Gruesome', 'Maniacal', 'Periodic', 'Dashing', 'Whimsical', 'Overwrought', 'Future', 'Aquatic', 'Protective', 'Polite', 'Undesirable', 'Orange', 'Useful', 'Rich']
	adv_insp = ['Richly', 'Honorably', 'Ably', 'Magically', 'Abundantly', 'Nondescriptly', 'Hotly', 'Deafeningly', 'Viciously', 'Ferociously', 'Furiously', 'Hilariously', 'Basically', 'Parsimoniously', 'Royally', 'Readily', 'Strangely', 'Jokingly', 'Facetiously', 'Encouragingly', 'Enviously', 'Earsplittingly', 'Peacefully', 'Inquisitively', 'Tastefully', 'Incredibly', 'Beneficially', 'Defiantly', 'Tensely', 'Greatly', 'Firstly', 'Strongly', 'Gregariously', 'Prettily', 'Interestingly', 'Simply', 'Distinctly', 'Swiftly']
	print("Reach deep down into your soul and tell me a...")

	for key in blank_dict:
		key_pos=pos_dict[blank_dict[key][1]]
		filled = False
		now = time.time()
		print (now)
		future = now + 15
		print (future)
		while not filled:
			fillintheblank=raw_input(key_pos + ': ')
			if time.time > future:
				print("Would you like some inspiration? Press 'i' and then enter for a word that we like.")
			if fillintheblank == 'i':
				if key_pos == 'Noun':
					print(noun_insp[random.choice()])
				elif key_pos == 'Verb':
					print(verb_insp[random.choice()])
				elif key_pos == 'Adjective':
					print(adj_insp[random.choice()])
				elif key_pos == 'Adverb':
					print(adv_insp[random.choice()])
			else:
				madlib_list[blank_dict[key][0]]=fillintheblank
				filled = True
	
	final_madlib = ''
	for word in madlib_list:
		final_madlib = final_madlib + word + ' '
	#print(final_madlib)
	#print(blank_dict)

def madlibbing():
	now = time.time()
	print (now)	
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
				req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
				con = urllib2.urlopen( req )
				#data = urllib2.urlopen(url).read()
				newdata= BeautifulSoup(con).get_text()
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
