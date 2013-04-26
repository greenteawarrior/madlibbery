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


def welcome():
	def yesmake():
		forget(make_welcome)
		forget(continuebutton)
		#return(True) #(continuebutton, quitbutton)
		makemadlib()
	def quit():
		sys.exit()
	def forget(var):
		var.pack_forget()
	#def welcome():
	make_welcome = Tkinter.Label(text = "Let's get down to business (to defeat the ___). Compose something and we'll turn it into a madlib. Results may vary (that's the point).")
	make_welcome.pack()
	continuebutton = Tkinter.Button(text = "Continue", command = yesmake)
	continuebutton.pack()
	quitbutton = Tkinter.Button(text = "Quit", command = quit )
	quitbutton.pack()
welcome()

def makemadlib():
	makemadlibtype = Tkinter.Label(text = "Would you like to use one of our Madlib stories, choose one from elsewhere, or create your own?")
	makemadlibtype.pack()
	def mine():
		myinput = Tkinter.Entry()
		myinput.pack()
		myinputbutton.pack()
	def minebutton():
		inputstory = myinput.get()
		inputstoryyours.pack_forget()
		inputstorymine.pack_forget()
		inputstoryurl.pack_forget()
		makemadlibtype.pack_forget()
	def yours():
		inputstory = 'There was a strange creature wandering around Olin. It had the head of a cat and the body of an octopus. I decided to call it Octocat.'
		inputstoryyours.pack_forget()
		inputstorymine.pack_forget()
		inputstoryurl.pack_forget()
		makemadlibtype.pack_forget()
	def url():
		try:
			req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
			con = urllib2.urlopen( req )
			#data = urllib2.urlopen(url).read()
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
			inputstoryurl = Tkinter.Button(text = 'Take text from a URL', command = url)			

	def urlbutton():
		inputstory = myinput.get()
		inputstoryyours.pack_forget()
		inputstorymine.pack_forget()
		inputstoryurl.pack_forget()
		makemadlibtype.pack_forget()
	inputstoryyours = Tkinter.Button(text = 'Use one of your stories' , command = yours)
	inputstorymine = Tkinter.Button(text = 'Write or paste my own story', command = mine)
	inputstoryurl = Tkinter.Button(text = 'Take text from a URL', command = url)
	urlinputbutton = Tkinter.Button(text = "Submit", command = urlbutton)
	myinputbutton = Tkinter.Button(text = "Submit", command = minebutton)
	inputstoryyours.pack()
	inputstorymine.pack()
	inputstoryurl.pack()
	howmanyblanks = Tkinter.Label(text = 'How many blanks would you like in your madlib?')





g.mainloop()