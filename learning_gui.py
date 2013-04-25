from swampy.Gui import *
import Tkinter
import sys

g = Tkinter.Tk()
g.title = ('MadlibMaker')

canvas = Tkinter.Canvas()#width = 500, height = 500
canvas.config(bg = 'cyan')


def welcome():
	def yesmake():
		forget(make_welcome)
		forget(continuebutton)
		return(True) #(continuebutton, quitbutton)
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
		myinput = Tkinter.Text()
		inputstory = myinput.get()
		inputstoryyours.pack_forget()
		inputstorymine.pack_forget()
		inputstoryurl.pack_forget()
	def yours():
		inputstory = 'There was a strange creature wandering around Olin. It had the head of a cat and the body of an octopus. I decided to call it Octocat.'
		inputstoryyours.pack_forget()
		inputstorymine.pack_forget()
		inputstoryurl.pack_forget()
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
		except:
			error = Tkinter.Label(text = "That is not a valid url.")
			inputstoryurl = Tkinter.Button(text = 'Take text from a URL', command = url)			
			#inputstory = False
		#inputstory =


	inputstoryyours = Tkinter.Button(text = 'Use one of our stories', command = yours)
	inputstorymine = Tkinter.Button(text = 'Write or paste your own story', command = mine)
	inputstoryurl = Tkinter.Button(text = 'Take text from a URL', command = url)
	inputstoryyours.pack()
	inputstorymine.pack()
	inputstoryurl.pack()

if welcome() == True
	makemadlib()
#if yes.get == 'yes':
#	g.delete(make_welcome)
#	g.delete(yesent)

#def nicejob():
	#nicejob = g.la(text = 'Nice Job')


#def button2():
#	button2 = g.bu(text = 'press me!', command = nicejob)

#button = g.bu(text = 'press me!', command = button2)


#button = g.bu(text = )



g.mainloop()