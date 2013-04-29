from flask import Flask,render_template, request
import nltk
import random
app = Flask(__name__)

@app.route('/index', methods=['GET', 'POST'])

def index():
    def blankage(inputstory_list, totalblanks):
        blank = '_____' #this is a string of five underscores
        blank_dict = {}
        tagged = nltk.pos_tag(inputstory_list)

        blankable_poslist = ['NN', 'VB', 'VBP', 'JJ', 'RB']
        howmanyblanks = 0 #counter for current amount of blanks in madlib in progress

        blankables = 0
        for i in tagged:
            if i[1] in blankable_poslist:
                blankables = blankables + 1

        while howmanyblanks < totalblanks and howmanyblanks < blankables:
            wordtoblank = random.choice(inputstory_list)
            wordtoblank_index = inputstory_list.index(wordtoblank)
            wordtoblank_pos = tagged[wordtoblank_index][1]#nltk stuff
            if wordtoblank_pos in blankable_poslist and wordtoblank != blank:
                howmanyblanks = howmanyblanks + 1
                blank_dict[wordtoblank] = (wordtoblank_index,wordtoblank_pos) #look up the part of speech here
                inputstory_list[wordtoblank_index] = blank
        return inputstory_list, blank_dict
    
    if request.method=='GET':
        return render_template('start.html')
    else:
        inputstory = str(request.form['inputstory'])
        inputstory_list = inputstory.split()
        totalblanks = int(request.form['totalblanks'])
        madlib = blankage(inputstory_list, totalblanks)
        print (madlib)
        return render_template('middle.html')

if __name__ == "__main__":
    app.run(debug=True)