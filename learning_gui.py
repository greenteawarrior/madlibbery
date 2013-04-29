from swampy.Gui import *
import Tkinter
import sys
import random
import nltk
import urllib2
from bs4 import BeautifulSoup
from threading import Timer

g = Tkinter.Tk()
g.title = ('MadlibMaker')

canvas = Tkinter.Canvas(width = 500, height = 500)
canvas.config(bg = 'cyan')
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
	#copy and paste NLTK stuff here
def submitbutton():
	inputstory = entry.get()
	forget()
	baking()
def howtoblank():
	def howtoblankbutton():
		myinput = howmanyblanks.get()
		forget()
		makemadlib()
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
	forget()
	entry = Tkinter.Entry()
	myinputstory = Tkinter.Button(text = "Submit", command = submitbutton)
	pack(entry)#.pack()
	pack(myinputbutton)#.pack()
	# inputstoryyours.pack_forget()
	# inputstorymine.pack_forget()
	# inputstoryurl.pack_forget()
	# makemadlibtype.pack_forget()
	#return(myinput)
def yours():
	inputstory = 'There was a strange creature wandering around Olin. It had the head of a cat and the body of an octopus. I decided to call it Octocat.'
	forget()
	baking()
	# inputstoryyours.pack_forget()
	# inputstorymine.pack_forget()
	# inputstoryurl.pack_forget()
	# makemadlibtype.pack_forget()
def url():
	try:
		req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
		con = urllib2.urlopen( req )
		newdata= BeautifulSoup(con).get_text()
		a = newdata.strip('\n')
		inputstory = a.strip('')
		inputstoryyours.pack_forget()
		inputstorymine.pack_forget()
		inputstoryurl.pack_forget() 
		makemadlibtype.pack_forget()
		urlinputbutton.pack()
	except:
		error = Tkinter.Label(text = "That is not a valid url.")
		inputstoryurl = Tkinter.Button(text = 'Take text from a URL', command = submitbutton)			



def makemadlib():
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
