# Imports for the other files in the program also random words
import random
from Word_List import *
from Entities import *
from Floors import *
PImage (bigratImg)
bigratImg = loadImage("BigRat.png")
rand = random.randint(0,len(easyWords))
word = (easyWords[rand])
# How long the word is
length = len(word)
# Setting up the global values that will be used in checking the word
wordkey = ""
cycle = 0
baseAttack = 10
winner = 0
in_combat = 0

def setup():
  size(1080,720)
  wordkey = ""

def draw():
  fill(255)
  rect(0, 0, 400, 400)
  textSize(35)
  fill(0)
  text(word, 200 , 200)


def keyTyped():
    global wordkey
    global cycle
    global baseAttack
    global winner
    image(bigratImg, 500, 400)
    compar = ""
    compar = key
    if in_combat == 1:
        if key == ENTER:
            if wordkey == word:
                print ("you have dealt damage to the enemy")
                winner = 1
            else:
                print("You have failed your attack")
        elif cycle == length:
            print("You exceed the words length, -2 to damage")
            baseAttack -= 2    
        if winner == 0:
            if key != word[cycle]:
                baseAttack -= 2
                print("BAD")
                cycle += 1
            else:
                cycle += 1
        text = ""
        text += key
        wordkey += text
        print (text)

def mouseClicked():
    print(wordkey)        
        
    
    
    
  
    