from swampy.Gui import *
import Tkinter
import sys
import random
import nltk
import urllib2
from bs4 import BeautifulSoup
from threading import Timer
import re
#fix it so how many blanks is after, howmanyblanks only takes numbers, and all of our other loverly restrictions on inputs.
g = Tkinter.Tk()
g.title = ('MadlibMaker')

#canvas = Tkinter.Canvas(width = 500, height = 500)
#canvas.config(bg = 'cyan')
forgetlist = []

def forget():
	i = 0
	for var in forgetlist:
		var.pack_forget()
		i = i + 1
	del forgetlist[0: i + 1]
def pack(var):
	var.pack()
	forgetlist.append(var)


def makemadlib():
	forget()
	makemadlibtype = Tkinter.Label(text = "Would you like to use one of our Madlib stories, choose one from elsewhere, or create your own?")
	inputstoryyours = Tkinter.Button(text = 'Use one of your stories' , command = yours)
	inputstorymine = Tkinter.Button(text = 'Write or paste my own story', command = mine)
	inputstoryurl = Tkinter.Button(text = 'Take text from a random Wikipedia article', command = url)
	#urlinputbutton = Tkinter.Button(text = "Submit", command = urlbutton)
	pack(makemadlibtype)
	pack(inputstoryyours)
	pack(inputstorymine)
	pack(inputstoryurl)

def baking():
	forget()
	# pleasewait = Tkinter.Label(text = 'Please wait while we generate your madlib')
	# pack(pleasewait)
	# warning= Tkinter.Label(text = 'Only verbs, adjectives, adverbs, and nouns can be selected to be replaced')
	# pack (warning)
	# letsplay()
def inspiration():
	insp= ['Acoustic', 'Curve', 'Custard', 'Hen', 'Jaw', 'Bladder', 'Detail', 'Output', 'Polo', 'Sideboard', 'Single', 'Tiger', 'Fahrenheit', 'Lettuce', 'Owner', 'Parsnip', 'Path', 'Resolution', 'Sardine', 'Scarecrow', 'Badger', 'Butter', 'Coast', 'Difference', 'Jam', 'Loaf', 'Methane', 'Sense', 'Stew', 'Apology', 'Carpenter', 'Eyeliner', 'Form', 'Sister', 'Handsaw', 'Save', 'Softdrink', 'Study', 'Tent', 'Bath', 'Cast', 'Creature', 'Freighter', 'Nail', 'Pie', 'Repair', 'Request', 'Throat', 'Wolf', 'Ornament', 'Pan', 'Supply', 'Uncle', 'Wallet', 'Elicit', 'Save', 'Solve', 'Draw', 'Forecast', 'Execute', 'Travel', 'Research', 'Assume', 'Compile', 'Upheld', 'Differentiate', 'Sustain', 'Code', 'Fix', 'Replace', 'Import', 'Coordinate', 'Undertook', 'Supply', 'Devote', 'Secure', 'Customize', 'Disseminate', 'Resolve', 'Institute', 'Assist', 'Intervene', 'Investigate', 'Address', 'Care', 'Correlate', 'Model', 'Enumerate', 'Discriminate', 'Outline', 'Diagnose', 'Cooperate', 'Search', 'Accomplish', 'Teach', 'Interpret', 'Verify', 'Explore', ' Pioneer', 'Prevent', 'Visualize', 'Check', 'Establish', 'Distribute', 'Unify', 'Foster', 'Bargain', 'Renew', 'Expand', 'Upgrade', 'Experiment', 'Monitor', 'Moderate', 'Dusty', 'Superb', 'Weak', 'Female', 'Internal', 'Nostalgic', 'Uptight', 'Habitual', 'Woozy', 'Quiet', 'Thirsty', 'Fearful', 'Gleaming', 'Happy', 'Vagabond', 'Ill', 'Many', 'Deeply', 'Luxuriant', 'Present', 'Tall', 'Swanky', 'Clear', 'Tired', 'Fluffy', 'Blue-eyed', 'Average', 'Obscene', 'Parched', 'Uninterested', 'Important', 'Wooden', 'Late', 'Scattered', 'Materialistic', 'Alluring', 'Square', 'Sweltering', 'Capable', 'Gruesome', 'Maniacal', 'Periodic', 'Dashing', 'Whimsical', 'Overwrought', 'Future', 'Aquatic', 'Protective', 'Polite', 'Undesirable', 'Orange', 'Useful', 'Rich', 'Richly', 'Honorably', 'Ably', 'Magically', 'Abundantly', 'Nondescriptly', 'Hotly', 'Deafeningly', 'Viciously', 'Ferociously', 'Furiously', 'Hilariously', 'Basically', 'Parsimoniously', 'Royally', 'Readily', 'Strangely', 'Jokingly', 'Facetiously', 'Encouragingly', 'Enviously', 'Earsplittingly', 'Peacefully', 'Inquisitively', 'Tastefully', 'Incredibly', 'Beneficially', 'Defiantly', 'Tensely', 'Greatly', 'Firstly', 'Strongly', 'Gregariously', 'Prettily', 'Interestingly', 'Simply', 'Distinctly', 'Swiftly']
	inspirationlabel = Tkinter.Label(text = random.choice(insp))
	pack(inspirationlabel)
	timeelapsed.cancel()
def timing():
	inspirationbutton = Tkinter.Button(text = "If you need some inspiration, press for a word that we like. ", command = inspiration)
	pack(inspirationbutton)
def playage(inputstory_list, blank_dict):
	forget()
 	pos_dict= {'NN': 'Noun', 'VB': 'Verb', 'VBP': 'Verb', 'JJ': 'Adjective', 'RB': 'Adverb'}
 	soul = Tkinter.Label(text = "Reach deep down into your soul and tell me a...")
 	pack(soul)
 	
 	keyslist = blank_dict.keys()
 	posentrylist = []
 	timeelapsed = Timer(15.0, timing)
	timeelapsed.start()
	for key in blank_dict:
		key_pos=pos_dict[blank_dict[key][1]]
		partofspeech = Tkinter.Label(text = key_pos + ':')
		partofspeechentry = Tkinter.Entry()
		posentrylist.append(partofspeechentry)
		pack(partofspeech)
		pack(partofspeechentry)
	def submitword():
		timeelapsed.cancel()
		for element in posentrylist:
			index = posentrylist.index(element)
			fillintheblank = element.get()
			inputstory_list[blank_dict[keyslist[index]][0]]= fillintheblank
		forget()
		def Finished():
			forget()
			finishedmadlib = ''
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
	timeelapsed.cancel()

def letsplay(inputstory):
	inputstory_list = inputstory.split()
	def howtoblank(myinputnumber):
		blank = '_____' #this is a string of five underscores
		blank_dict = {}
		tagged = nltk.pos_tag(inputstory_list)
		blankable_poslist = ['NN', 'VB', 'VBP', 'JJ', 'RB']
		blankables = 0
		for i in tagged:
			if i[1] in blankable_poslist:
				blankables = blankables + 1
		#howmanyblanks = 0 #counter for current amount of blanks in madlib in progress
		while len(blank_dict) < int(myinputnumber) and len(blank_dict) < int(blankables):
			wordtoblank = random.choice(inputstory_list)
			wordtoblank_index = inputstory_list.index(wordtoblank)
			wordtoblank_pos = tagged[wordtoblank_index][1]#nltk stuff
			if wordtoblank_pos in blankable_poslist and wordtoblank != blank:
				blank_dict[wordtoblank] = (wordtoblank_index,wordtoblank_pos) #look up the part of speech here
				inputstory_list[wordtoblank_index] = blank
		playage(inputstory_list, blank_dict)
		#return inputstory_list, blank_dict

	def howtoblankbutton():
		myinputnumber = howmanyblanksentry.get()
		howtoblank(myinputnumber)
			#return(myinputnumber)
	forget()
	howmanyblanksq = Tkinter.Label(text = 'How many blanks would you like in your madlib?')
	howmanyblanksentry= Tkinter.Entry()
	howmanyblanksbutton = Tkinter.Button(text = "Submit", command = howtoblankbutton)
	pack(howmanyblanksq)
	pack(howmanyblanksentry)
	pack(howmanyblanksbutton)

		#return(howtoblankbutton())
#def playage(madlib): #copied madlib maker and nltk stuff so that I can use it to compare
	# unpacking the madlib
	#madlib = blankage(inputstory_list)
	







def welcome():
	forget()
	# def yesmake():
	# 	forget()
	# 	Randombakingbutton= Tkinter.Button(text = "Click here if you wish for the words to be madlibbed in your paragraph to be selected randomly", command = makemadlib)
	# 	pack(Randombakingbutton)
	# 	Bakingbutton= Tkinter.Button(text= "Click here if you wish to manually select the words to be madlibbed", command = baking)
	# 	pack(Bakingbutton)
	def quit():
		sys.exit()

	make_welcome = Tkinter.Label(text = "Let's get down to business (to defeat the ___). Compose something and we'll turn it into a madlib. Results may vary (that's the point).")
	pack(make_welcome)
	continuebutton = Tkinter.Button(text = "Continue", command = makemadlib)
	pack(continuebutton)
def permanents():
	quitbutton = Tkinter.Button(text = "Quit", command = quit )
	quitbutton.pack()
	Undobutton= Tkinter.Button(text = "Restart", command = welcome)
	Undobutton.pack()
permanents()
welcome()

def mine():
	def submitbutton():
		inputstory = mystory.get()
		if len(inputstory.split()) <= 10:
			forget()
			redolabel = Tkinter.Label(text = inputstory)
			short = Tkinter.Label(text = "We don't think that story is long enough to produce a fun madlib. Please extend it or make another." )
			pack(redolabel)
			pack(short)
			pack(mystory)#.pack()
			pack(myinputstory)#.pack()
		else:
			letsplay(inputstory)
		# Randombakingbutton= Tkinter.Button(text = "Click here if you wish for the words to be madlibbed in your paragraph to be selected randomly", command = howtoblan
		# pack(Randombakingbutton)
		# Bakingbutton= Tkinter.Button(text= "Click here if you wish to manually select the words to be madlibbed", command = baking)
		# pack(Bakingbutton)
	forget()
	mystory = Tkinter.Entry()
	myinputstory = Tkinter.Button(text = "Submit", command = submitbutton)
	pack(mystory)
	pack(myinputstory)
	# inputstoryyours.pack_forget()
	# inputstorymine.pack_forget()
	# inputstoryurl.pack_forget()
	# makemadlibtype.pack_forget()
	#return(myinput)
def yours():
	inputstory = 'There was a strange creature wandering around Olin. It had the head of a cat and the body of an octopus. I decided to call it Octocat.'
	forget()
	letsplay(inputstory)
def url():
	# def submitbutton():
	# 	inputstory = mystory.get()
	# 	forget()
	try:
		url = 'http://www.wikipedia.org/wiki/Special:random'
		req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
		con = urllib2.urlopen( req ).read()
		results = re.findall('<p>(.*)</p>', con)
		wikipediatxt = results[0]
		inputstory = BeautifulSoup(wikipediatxt).get_text()
		titlehtml = re.findall('<title>(.*)- Wikipedia', con)
		title = Tkinter.Label(text = 'The title of your madlib is: ' + str(titlehtml)[2:-2])
		forget()
		pack(title)
		letsplay(inputstory)
	except:
		url = 'http://en.wikipedia.org/wiki/Software_development'
		req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
		con = urllib2.urlopen( req ).read()
		results = re.findall('<p>(.*)</p>', con)
		wikipediatxt = results[0]
		inputstory = BeautifulSoup(wikipediatxt).get_text()
		titlehtml = re.findall('<title>(.*)- Wikipedia', con)
		title = Tkinter.Label(text = 'The title of your madlib is: ' + str(titlehtml)[2:-2])
		forget()
		pack(title)
		letsplay(inputstory)	





#decorator
#radio buttons tkinter

g.mainloop()
