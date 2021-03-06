import Tkinter
import sys
import random
import nltk
import urllib2
from bs4 import BeautifulSoup
from threading import Timer
import re


g = Tkinter.Tk() #initialize TKinter
g.title = ('MadlibMaker')


forgetlist = []
def forget(): 
	"""clears screen except for permanents"""
	i = 0
	for var in forgetlist:
		var.pack_forget()
		i = i + 1
	del forgetlist[0: i + 1]
def pack(var):
	"""Adds items to screen and makes a list to clear them later"""
	var.pack()
	forgetlist.append(var)


def makemadlib():
	"""determine source of madlib text, call appropriate function (yours, mine, or URL)"""
	forget()
	makemadlibtype = Tkinter.Label(text = "Would you like to use one of our Madlib stories, choose one from elsewhere, or create your own?")
	inputstoryyours = Tkinter.Button(text = 'Use one of your stories' , command = yours)
	inputstorymine = Tkinter.Button(text = 'Write or paste my own story', command = mine)
	inputstoryurl = Tkinter.Button(text = 'Take text from a random Wikipedia article', command = url)
	pack(makemadlibtype)
	pack(inputstoryyours)
	pack(inputstorymine)
	pack(inputstoryurl)

def playage(inputstory_list, blank_dict):
	"""Has the player fill in the blanks by taking list of words in story with blanks and 
	a dictionary where the key is blanked words and the value is their part of speech, and their index. 
	It ultimately displays the result  """
	def inspiration():
		"""Displays random word for inspiration"""
		insp= ['Acoustic', 'Curve', 'Custard', 'Hen', 'Jaw', 'Bladder', 'Detail', 'Output', 'Polo', 'Sideboard', 'Single', 'Tiger', 'Fahrenheit', 'Lettuce', 'Owner', 'Parsnip', 'Path', 'Resolution', 'Sardine', 'Scarecrow', 'Badger', 'Butter', 'Coast', 'Difference', 'Jam', 'Loaf', 'Methane', 'Sense', 'Stew', 'Apology', 'Carpenter', 'Eyeliner', 'Form', 'Sister', 'Handsaw', 'Save', 'Softdrink', 'Study', 'Tent', 'Bath', 'Cast', 'Creature', 'Freighter', 'Nail', 'Pie', 'Repair', 'Request', 'Throat', 'Wolf', 'Ornament', 'Pan', 'Supply', 'Uncle', 'Wallet', 'Elicit', 'Save', 'Solve', 'Draw', 'Forecast', 'Execute', 'Travel', 'Research', 'Assume', 'Compile', 'Upheld', 'Differentiate', 'Sustain', 'Code', 'Fix', 'Replace', 'Import', 'Coordinate', 'Undertook', 'Supply', 'Devote', 'Secure', 'Customize', 'Disseminate', 'Resolve', 'Institute', 'Assist', 'Intervene', 'Investigate', 'Address', 'Care', 'Correlate', 'Model', 'Enumerate', 'Discriminate', 'Outline', 'Diagnose', 'Cooperate', 'Search', 'Accomplish', 'Teach', 'Interpret', 'Verify', 'Explore', ' Pioneer', 'Prevent', 'Visualize', 'Check', 'Establish', 'Distribute', 'Unify', 'Foster', 'Bargain', 'Renew', 'Expand', 'Upgrade', 'Experiment', 'Monitor', 'Moderate', 'Dusty', 'Superb', 'Weak', 'Female', 'Internal', 'Nostalgic', 'Uptight', 'Habitual', 'Woozy', 'Quiet', 'Thirsty', 'Fearful', 'Gleaming', 'Happy', 'Vagabond', 'Ill', 'Many', 'Deeply', 'Luxuriant', 'Present', 'Tall', 'Swanky', 'Clear', 'Tired', 'Fluffy', 'Blue-eyed', 'Average', 'Obscene', 'Parched', 'Uninterested', 'Important', 'Wooden', 'Late', 'Scattered', 'Materialistic', 'Alluring', 'Square', 'Sweltering', 'Capable', 'Gruesome', 'Maniacal', 'Periodic', 'Dashing', 'Whimsical', 'Overwrought', 'Future', 'Aquatic', 'Protective', 'Polite', 'Undesirable', 'Orange', 'Useful', 'Rich', 'Richly', 'Honorably', 'Ably', 'Magically', 'Abundantly', 'Nondescriptly', 'Hotly', 'Deafeningly', 'Viciously', 'Ferociously', 'Furiously', 'Hilariously', 'Basically', 'Parsimoniously', 'Royally', 'Readily', 'Strangely', 'Jokingly', 'Facetiously', 'Encouragingly', 'Enviously', 'Earsplittingly', 'Peacefully', 'Inquisitively', 'Tastefully', 'Incredibly', 'Beneficially', 'Defiantly', 'Tensely', 'Greatly', 'Firstly', 'Strongly', 'Gregariously', 'Prettily', 'Interestingly', 'Simply', 'Distinctly', 'Swiftly']
		inspirationlabel = Tkinter.Label(text = random.choice(insp))
		pack(inspirationlabel)
	forget()
	pos_dict= {'NN': 'Noun',
	 'VB': 'Verb', 'VBP': 'Verb', 'JJ': 'Adjective', 'RB': 'Adverb'}
	soul = Tkinter.Label(text = "Reach deep down into your soul and tell me a...")
	pack(soul)
	
	keyslist = blank_dict.keys()
	posentrylist = []
	inspirationbutton = Tkinter.Button(text = "If you need some inspiration, press for a word that we like. ", command = inspiration)
	for key in blank_dict:
		key_pos=pos_dict[blank_dict[key][1]]
		partofspeech = Tkinter.Label(text = key_pos + ':')
		partofspeechentry = Tkinter.Entry()
		posentrylist.append(partofspeechentry)
		pack(partofspeech)
		pack(partofspeechentry)
	def submitword():
		"""Replaces blanks with new words"""
		for element in posentrylist:
			index = posentrylist.index(element)
			fillintheblank = element.get()
			inputstory_list[blank_dict[keyslist[index]][0]]= fillintheblank
		forget()
		def Finished():
			"""displays final result"""
			forget()
			finishedmadlib = ''
			wordwraps = (len(inputstory_list)/10) + 1
			for wrapindex in range(1, wordwraps):
				inputstory_list.insert(wrapindex*10, '\n')
			for word in inputstory_list:
				finishedmadlib += word + ' '
			finalproduct= Tkinter.Label(text=finishedmadlib)
			pack(finalproduct)		
		complete= Tkinter.Label(text='Ding! Your madlib is complete!')
		readmadlib= Tkinter.Button(text= 'Click here to read your new Madlib!', command= Finished)
		pack(complete)
		pack(readmadlib)

	fillintheblankbutton = Tkinter.Button(text = 'submit', command = submitword )
	pack(fillintheblankbutton)
	pack(inspirationbutton)

def blankage(inputstory):
	"""takes in text to be used as madlib, randomly chooses words and replaces them with blanks, calls playage"""
	inputstory_list = inputstory.split() #split it into list of words to be tagged
	def howtoblank(myinputnumber):
		blank = '_____' #this is a string of five underscores
		blank_dict = {}
		tagged = nltk.pos_tag(inputstory_list)
		blankable_poslist = ['NN', 'VB', 'VBP', 'JJ', 'RB']
		blankables = 0
		for i in tagged:
			if i[1] in blankable_poslist:
				blankables = blankables + 1
		while len(blank_dict) < int(myinputnumber) and len(blank_dict) < int(blankables):
			wordtoblank = random.choice(inputstory_list)
			wordtoblank_index = inputstory_list.index(wordtoblank)
			wordtoblank_pos = tagged[wordtoblank_index][1]#nltk stuff
			if wordtoblank_pos in blankable_poslist and wordtoblank != blank:
				blank_dict[wordtoblank] = (wordtoblank_index,wordtoblank_pos) #look up the part of speech here
				inputstory_list[wordtoblank_index] = blank
		playage(inputstory_list, blank_dict)

	def howtoblankbutton():
		myinputnumber = howmanyblanksentry.get()
		howtoblank(myinputnumber)
	howmanyblanksq = Tkinter.Label(text = 'How many blanks would you like in your madlib? (Choose a number between 1 and 15)')
	howmanyblanksentry= Tkinter.Entry()
	howmanyblanksbutton = Tkinter.Button(text = "Submit", command = howtoblankbutton)
	pack(howmanyblanksq)
	pack(howmanyblanksentry)
	pack(howmanyblanksbutton)
# # <<<<<<< HEAD
# # =======
# 	madlib=howtoblank(inputstory_list)# need to fix this line.
# 	playage(madlib)
# 		#return(howtoblankbutton())
# 	def timing():
# 		print("If you need some inspiration, press 'i' and hit enter for a word that we like. ")

# 	def playage(madlib): #copied madlib maker and nltk stuff so that I can use it to compare
# 		# unpacking the madlib
# 		madlib_list = madlib[0]
# 		blank_dict = madlib[1]
# 		pos_dict= {'NN': 'Noun', 'VB': 'Verb', 'VBP': 'Verb', 'JJ': 'Adjective', 'RB': 'Adverb'}
# 		noun_insp = ['Acoustic', 'Curve', 'Custard', 'Hen', 'Jaw', 'Bladder', 'Detail', 'Output', 'Polo', 'Sideboard', 'Single', 'Tiger', 'Fahrenheit', 'Lettuce', 'Owner', 'Parsnip', 'Path', 'Resolution', 'Sardine', 'Scarecrow', 'Badger', 'Butter', 'Coast', 'Difference', 'Jam', 'Loaf', 'Methane', 'Sense', 'Stew', 'Apology', 'Carpenter', 'Eyeliner', 'Form', 'Sister', 'Handsaw', 'Save', 'Softdrink', 'Study', 'Tent', 'Bath', 'Cast', 'Creature', 'Freighter', 'Nail', 'Pie', 'Repair', 'Request', 'Throat', 'Wolf', 'Ornament', 'Pan', 'Supply', 'Uncle', 'Wallet']
# 		verb_insp = ['Elicit', 'Save', 'Solve', 'Draw', 'Forecast', 'Execute', 'Travel', 'Research', 'Assume', 'Compile', 'Upheld', 'Differentiate', 'Sustain', 'Code', 'Fix', 'Replace', 'Import', 'Coordinate', 'Undertook', 'Supply', 'Devote', 'Secure', 'Customize', 'Disseminate', 'Resolve', 'Institute', 'Assist', 'Intervene', 'Investigate', 'Address', 'Care', 'Correlate', 'Model', 'Enumerate', 'Discriminate', 'Outline', 'Diagnose', 'Cooperate', 'Search', 'Accomplish', 'Teach', 'Interpret', 'Verify', 'Explore', ' Pioneer', 'Prevent', 'Visualize', 'Check', 'Establish', 'Distribute', 'Unify', 'Foster', 'Bargain', 'Renew', 'Expand', 'Upgrade', 'Experiment', 'Monitor', 'Moderate']
# 		adj_insp = ['Dusty', 'Superb', 'Weak', 'Female', 'Internal', 'Nostalgic', 'Uptight', 'Habitual', 'Woozy', 'Quiet', 'Thirsty', 'Fearful', 'Gleaming', 'Happy', 'Vagabond', 'Ill', 'Many', 'Deeply', 'Luxuriant', 'Present', 'Tall', 'Swanky', 'Clear', 'Tired', 'Fluffy', 'Blue-eyed', 'Average', 'Obscene', 'Parched', 'Uninterested', 'Important', 'Wooden', 'Late', 'Scattered', 'Materialistic', 'Alluring', 'Square', 'Sweltering', 'Capable', 'Gruesome', 'Maniacal', 'Periodic', 'Dashing', 'Whimsical', 'Overwrought', 'Future', 'Aquatic', 'Protective', 'Polite', 'Undesirable', 'Orange', 'Useful', 'Rich']
# 		adv_insp = ['Richly', 'Honorably', 'Ably', 'Magically', 'Abundantly', 'Nondescriptly', 'Hotly', 'Deafeningly', 'Viciously', 'Ferociously', 'Furiously', 'Hilariously', 'Basically', 'Parsimoniously', 'Royally', 'Readily', 'Strangely', 'Jokingly', 'Facetiously', 'Encouragingly', 'Enviously', 'Earsplittingly', 'Peacefully', 'Inquisitively', 'Tastefully', 'Incredibly', 'Beneficially', 'Defiantly', 'Tensely', 'Greatly', 'Firstly', 'Strongly', 'Gregariously', 'Prettily', 'Interestingly', 'Simply', 'Distinctly', 'Swiftly']
# 		print("Reach deep down into your soul and tell me a...")

# 		for key in blank_dict:
# 			key_pos=pos_dict[blank_dict[key][1]]
# 			filled = False
# 			while not filled:
# 				timeelapsed = Timer(15.0, timing)
# 				timeelapsed.start()
# 				# this is where we need labels and stuff!
# 				fillintheblank=raw_input(key_pos + ': ')
# 				if fillintheblank == 'i':
# 					if key_pos == 'Noun':
# 						print(random.choice(noun_insp))
# 					elif key_pos == 'Verb':
# 						print(random.choice(verb_insp))
# 					elif key_pos == 'Adjective':
# 						print(random.choice(adj_insp))
# 					elif key_pos == 'Adverb':
# 						print(random.choice(adv_insp))
# 					timeelapsed.cancel()
# 				else:
# 					madlib_list[blank_dict[key][0]]=fillintheblank
# 					filled = True
# 					timeelapsed.cancel()
# 		timeelapsed.cancel()
# 		return madlib_list


# 		playing = False
# 		while playing == False:
# 			playing = playage(madlib)
# 		complete= Tkinter.Label(text='Your madlib is complete!')
# 		readmadlib= Tkinter.Button(text= 'Click here to read your new Madlib!', command= Finished)
# 		pack(complete)
# 		pack(readmadlib)

# 		#end of copied stuff here
# 	def Finished():
# 		forget()
# 		Undobutton= Tkinter.Button(text = "Undo", command = randombaking)
# 		finishedmadlib = ''
# 		for word in playing:
# 			finishedmadlib += word + ' '
# 		finalproduct= Tkinter.Label(text=finishedmadlib)
# 		pack(Undobutton)
# 		pack(finalproduct)
# #>>>>>>> a808e9ba7c887c5890aae45898f80529fdb8dbb4

def welcome():
	"""start here, display welcome message, and call makemadlib"""
	forget()
	def quit():
		sys.exit() 

	make_welcome = Tkinter.Label(text = "Let's get down to business (to defeat the ___). Compose something and we'll turn it into a madlib. Results may vary (that's the point).")
	pack(make_welcome)
	continuebutton = Tkinter.Button(text = "Continue", command = makemadlib)
	pack(continuebutton)
def permanents():
	"""buttons that don't get forgotten (quit and restart)"""
	quitbutton = Tkinter.Button(text = "Quit", command = quit )
	quitbutton.pack()
	Undobutton= Tkinter.Button(text = "Restart", command = welcome)
	Undobutton.pack()
permanents()
welcome()

def mine():
	"""lets the user write their own story, calls blankage"""
	def submitbutton():
		inputstory = mystory.get()
		if len(inputstory.split()) <= 10: #make sure story is long enough
			forget()
			redolabel = Tkinter.Label(text = inputstory)
			short = Tkinter.Label(text = "We don't think that story is long enough to produce a fun madlib. Please extend it or make another." )
			pack(redolabel)
			pack(short)
			pack(mystory)
			pack(myinputstory)
		else:
			blankage(inputstory)
	forget()
	mystory = Tkinter.Entry()
	myinputstory = Tkinter.Button(text = "Submit", command = submitbutton)
	pack(mystory)
	pack(myinputstory)
def yours():
	"""Gives the user our story, calls blankage"""
	inputstory = 'There was a strange creature wandering around Olin. It had the head of a cat and the body of an octopus. I decided to call it Octocat.'
	forget()
	blankage(inputstory)
def url():
	"""Scrapes text from the first blurb of a random wikipedia article, calls blankage"""
	url = 'http://www.wikipedia.org/wiki/Special:random'
	req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) #this makes it so that wikipedia recognizes the app as a web-browser
	con = urllib2.urlopen( req ).read()
	results = re.findall('<p>(.*)</p>', con) #the first time a paragraph appears in an article, we use that text
	wikipediatxt = results[0]
	inputstory = BeautifulSoup(wikipediatxt).get_text() #clear HTML formatting from text using Beautifulsoup
	titlehtml = re.findall('<title>(.*)- Wikipedia', con) #find title of madlib
	titleis = Tkinter.Label(text = 'The title of your madlib is: ')
	title = Tkinter.Label(text = str(titlehtml)[2:-2])
	forget()
	pack(titleis)
	pack(title)
	blankage(inputstory)
g.mainloop()
