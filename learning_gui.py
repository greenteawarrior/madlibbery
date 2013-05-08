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
	pleasewait = Tkinter.Label(text = 'Please wait while we generate your madlib')
	pack(pleasewait)
	#copy and paste NLTK stuff here

#def playage(madlib): copied madlib maker and nltk stuff so that I can use it to compare
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
		while not filled:
			timeelapsed = Timer(15.0, timing)
			timeelapsed.start()
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

	#end of copied stuff





def howtoblank():
	def howtoblankbutton():
		myinput = howmanyblanks.get()
		forget()
		makemadlib()
	forget()
	howmanyblanksq = Tkinter.Label(text = 'How many blanks would you like in your madlib?')
	howmanyblanks= Tkinter.Entry()
	howmanyblanksbutton = Tkinter.Button(text = "Submit", command = howtoblankbutton)
	pack(howmanyblanksq)	
	pack(howmanyblanks)
	pack(howmanyblanksbutton)
def welcome():
	def yesmake():
		forget()
		howtoblank()
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
		inputstory = mystory.get()
		forget()
		baking()
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
	baking()
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
		baking()

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
	makemadlibtype = Tkinter.Label(text = "Would you like to use one of our Madlib stories, choose one from elsewhere, or create your own?")
	Undobutton= Tkinter.Button(text = "Undo", command = howtoblank)
	inputstoryyours = Tkinter.Button(text = 'Use one of your stories' , command = yours)
	inputstorymine = Tkinter.Button(text = 'Write or paste my own story', command = mine)
	inputstoryurl = Tkinter.Button(text = 'Take text from a URL', command = url)
	#urlinputbutton = Tkinter.Button(text = "Submit", command = urlbutton)
	pack(Undobutton)
	pack(makemadlibtype)
	pack(inputstoryyours)
	pack(inputstorymine)
	pack(inputstoryurl)



#decorator
#radio buttons tkinter

g.mainloop()
