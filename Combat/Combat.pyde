# Imports for the other files in the program also random words
print("combat")
import random
from Word_list import *
from Entities import *
from Floors import *
rand = random.randint(0,len(easyWords))
randFloor = random.randint(0,len(floor_layouts) - 1)
word = (easyWords[rand])
# Setting up the global values that will be used in checking the word
baseAttack = character.damage
health = character.health
armor = character.armor
wordkey = ""
winner = 0
in_combat = 1
current_Floor = floor_layouts[randFloor]
print("current_floor")

def setup():
   size(1080,720)
   print("setup happened")

def draw():
   fill(255)
   rect(0, 0, 1080, 720)
   textSize(35)
   fill(0)
   text(word, 200 , 200)
   bigratImg = loadImage("BigRat.png")
   image(bigratImg, 500, 400)


def keyTyped():
     global wordkey
     global winner
     if in_combat == 1:
        if key == ENTER:
            if wordkey == word:
                print ("you have dealt damage to the enemy")
                wordkey = ""
            else:
                print("You have failed your attack")
        if key == BACKSPACE:
            if wordkey > 0:
                wordkey = wordkey[:len(wordkey) - 1]
                wordkey = wordkey.replace(" ", "")
                print(wordkey)
        else:
            text = ""
            text += key
            wordkey += text
            print (text)

def mouseClicked():
    print(wordkey)