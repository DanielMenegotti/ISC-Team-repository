# Import for the wordlist will go here instead of a base word
import random
from Word_List import *
from Entities import *
rand = random.randint(0,len(easyWords))
word = (easyWords[rand])
# How long the word is
length = len(word)
# Setting up the global values that will be used in checking the word
wordkey = ""
cycle = 0
baseAttack = 10
winner = 0

def setup():
  size(400,400)
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
    compar = ""
    compar = key
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
        
    
    
    
  
    