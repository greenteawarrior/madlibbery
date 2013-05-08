from swampy.Gui import *
import Tkinter
import sys
import random
import nltk
import urllib2
from bs4 import BeautifulSoup
from threading import Timer
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


def baking():
	forget()
	Undobutton= Tkinter.Button(text = "Undo", command = welcome)
	# pleasewait = Tkinter.Label(text = 'Please wait while we generate your madlib')
	# pack(Undobutton)
	# pack(pleasewait)
	# warning= Tkinter.Label(text = 'Only verbs, adjectives, adverbs, and nouns can be selected to be replaced')
	# pack (warning)
	# letsplay()


def letsplay(inputstory):
	inputstory_list = inputstory.split()
	#def blankage(inputstory_list):# copy and pasted nltk stuff need to adjust

	#print(blankables)
	def howtoblank(myinputnumber):
		blank = '_____' #this is a string of five underscores
		blank_dict = {}
		tagged = nltk.pos_tag(inputstory_list)

		blankable_poslist = ['NN', 'VB', 'VBP', 'JJ', 'RB']
		blankables = 0
		print("you are here #1")
		for i in tagged:
			if i[1] in blankable_poslist:
				blankables = blankables + 1
		howmanyblanks = 0 #counter for current amount of blanks in madlib in progress
		while howmanyblanks < myinputnumber and howmanyblanks < blankables:
			print("you are here #2")
			wordtoblank = random.choice(inputstory_list)
			wordtoblank_index = inputstory_list.index(wordtoblank)
			wordtoblank_pos = tagged[wordtoblank_index][1]#nltk stuff
			if wordtoblank_pos in blankable_poslist and wordtoblank != blank:
				print("you are here #3")
				howmanyblanks = howmanyblanks + 1
				blank_dict[wordtoblank] = (wordtoblank_index,wordtoblank_pos) #look up the part of speech here
				inputstory_list[wordtoblank_index] = blank
		#return inputstory_list, blank_dict


	def howtoblankbutton():
		myinputnumber = howmanyblanksentry.get()
		print(myinputnumber)
		howtoblank(myinputnumber)
			#return(myinputnumber)
	forget()
	howmanyblanksq = Tkinter.Label(text = 'How many blanks would you like in your madlib?')
	howmanyblanksentry= Tkinter.Entry()
	Undobutton= Tkinter.Button(text = "Restart", command = welcome)
	howmanyblanksbutton = Tkinter.Button(text = "Submit", command = howtoblankbutton)
	pack(Undobutton)
	pack(howmanyblanksq)
	pack(howmanyblanksentry)
	pack(howmanyblanksbutton)
	madlib=howtoblank(inputstory_list)# need to fix this line.
	playage(madlib)
		#return(howtoblankbutton())
	def timing():
		print("If you need some inspiration, press 'i' and hit enter for a word that we like. ")

	def playage(madlib): #copied madlib maker and nltk stuff so that I can use it to compare
		# unpacking the madlib
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
			while not filled:
				timeelapsed = Timer(15.0, timing)
				timeelapsed.start()
				# this is where we need labels and stuff!
				fillintheblank=raw_input(key_pos + ': ')
				if fillintheblank == 'i':
					if key_pos == 'Noun':
						print(random.choice(noun_insp))
					elif key_pos == 'Verb':
						print(random.choice(verb_insp))
					elif key_pos == 'Adjective':
						print(random.choice(adj_insp))
					elif key_pos == 'Adverb':
						print(random.choice(adv_insp))
					timeelapsed.cancel()
				else:
					madlib_list[blank_dict[key][0]]=fillintheblank
					filled = True
					timeelapsed.cancel()
		timeelapsed.cancel()
		return madlib_list


		playing = False
		while playing == False:
			playing = playage(madlib)
		complete= Tkinter.Label(text='Your madlib is complete!')
		readmadlib= Tkinter.Button(text= 'Click here to read your new Madlib!', command= Finished)
		pack(complete)
		pack(readmadlib)

		#end of copied stuff here
	def Finished():
		forget()
		Undobutton= Tkinter.Button(text = "Undo", command = randombaking)
		finishedmadlib = ''
		for word in playing:
			finishedmadlib += word + ' '
		finalproduct= Tkinter.Label(text=finishedmadlib)
		pack(Undobutton)
		pack(finalproduct)

def welcome():
	def yesmake():
		forget()
		Randombakingbutton= Tkinter.Button(text = "Click here if you wish for the words to be madlibbed in your paragraph to be selected randomly", command = makemadlib)
		pack(Randombakingbutton)
		Bakingbutton= Tkinter.Button(text= "Click here if you wish to manually select the words to be madlibbed", command = baking)
		pack(Bakingbutton)
	def quit():
		sys.exit()
	make_welcome = Tkinter.Label(text = "Let's get down to business (to defeat the ___). Compose something and we'll turn it into a madlib. Results may vary (that's the point).")
	pack(make_welcome)
	#make_welcome.pack()
	continuebutton = Tkinter.Button(text = "Continue", command = yesmake)
	pack(continuebutton)
	#continuebutton.pack()
	quitbutton = Tkinter.Button(text = "Quit", command = quit )
	quitbutton.pack()
welcome()

def mine():
	def submitbutton():
		forget()
		inputstory = mystory.get()
		letsplay(inputstory)
		# Randombakingbutton= Tkinter.Button(text = "Click here if you wish for the words to be madlibbed in your paragraph to be selected randomly", command = howtoblan
		# pack(Randombakingbutton)
		# Bakingbutton= Tkinter.Button(text= "Click here if you wish to manually select the words to be madlibbed", command = baking)
		# pack(Bakingbutton)
	forget()
	mystory = Tkinter.Entry()
	Undobutton= Tkinter.Button(text = "Undo", command = makemadlib)
	myinputstory = Tkinter.Button(text = "Submit", command = submitbutton)
	pack(mystory)#.pack()
	pack(myinputstory)#.pack()
	pack(Undobutton)
	# inputstoryyours.pack_forget()
	# inputstorymine.pack_forget()
	# inputstoryurl.pack_forget()
	# makemadlibtype.pack_forget()
	#return(myinput)
def yours():
	inputstory = 'There was a strange creature wandering around Olin. It had the head of a cat and the body of an octopus. I decided to call it Octocat.'
	forget()
	Undobutton= Tkinter.Button(text = "Undo", command = makemadlib)
	pack(Undobutton)
	letsplay(inputstory)
	# inputstoryyours.pack_forget()
	# inputstorymine.pack_forget()
	# inputstoryurl.pack_forget()
	# makemadlibtype.pack_forget()
def url():
	def submitbutton():
		inputstory = mystory.get()
		forget()
		Undobutton= Tkinter.Button(text = "Undo", command = makemadlib)
		pack(Undobutton)
		Randombakingbutton= Tkinter.Button(text = "Click here if you wish for the words to be madlibbed in your paragraph to be selected randomly", command = howtoblank)
		pack(Randombakingbutton)
		Bakingbutton= Tkinter.Button(text= "Click here if you wish to manually select the words to be madlibbed", command = baking)
		pack(Bakingbutton)

	try:
		req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
		con = urllib2.urlopen( req )
		newdata= BeautifulSoup(con).get_text()
		a = newdata.strip('\n')
		inputstory = a.strip('')
		#inputstoryyours.pack_forget()
		#inputstorymine.pack_forget()
		#inputstoryurl.pack_forget() 
		#makemadlibtype.pack_forget()
		#urlinputbutton.pack()
	except:
		error = Tkinter.Label(text = "That is not a valid url.")
		inputstoryurl = Tkinter.Button(text = 'Take text from a URL', command = submitbutton)			



def makemadlib():
	forget()
	Undobutton= Tkinter.Button(text = "Undo", command = welcome)
	pack(Undobutton)
	makemadlibtype = Tkinter.Label(text = "Would you like to use one of our Madlib stories, choose one from elsewhere, or create your own?")
	inputstoryyours = Tkinter.Button(text = 'Use one of your stories' , command = yours)
	inputstorymine = Tkinter.Button(text = 'Write or paste my own story', command = mine)
	inputstoryurl = Tkinter.Button(text = 'Take text from a URL', command = url)
	#urlinputbutton = Tkinter.Button(text = "Submit", command = urlbutton)
	pack(makemadlibtype)
	pack(inputstoryyours)
	pack(inputstorymine)
	pack(inputstoryurl)



#decorator
#radio buttons tkinter

g.mainloop()
