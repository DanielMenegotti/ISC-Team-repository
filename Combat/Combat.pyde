# Imports for the other files in the program also random words
import random
from Word_List import *
from Entities import *
from Floors import *
randEasy = random.randint(0,len(easyWords))
randFloor = random.randint(0,len(floor_layouts) - 1)
randEarlyMonsters = random.randint(0,len(earlyMonsters) - 1)
word = (easyWords[randEasy])
# Setting up the global values that will be used in checking the word
baseAttack = character.damage
health = character.health
armor = character.armor
wordkey = ""
winner = 0
in_combat = 1
monster_setup = 0
current_Floor = floor_layouts[randFloor]
floor_level = 1
damage_dealt = 0
print(current_Floor)

def setup():
   size(1080,720)
   print("setup happened")

def draw():
   global monster_setup
   global monster
   fill(255)
   rect(0, 0, 1080, 720)
   forest_Background = loadImage("ForestBackground.png")
   image(forest_Background, 0, 0)
   if in_combat == 1 and monster_setup == 0:
       if floor_level <= 2:
        monster = earlyMonsters[randEarlyMonsters]
        if monster.name == "Slime":
            slimeImg = loadImage("Slime.png")
            image(slimeImg, 700, 400)
        if monster.name == "Big rat":
            ratImg = loadImage("BigRat.png")
            image(ratImg, 700, 400)
   textSize(35)
   fill(0)
   text(word, 200 , 200)
   text(wordkey, 500, 540)


def keyTyped():
     global wordkey
     global winner
     global monster
     global in_combat
     global damage_dealt
     if in_combat == 1:
        if key == ENTER:
            if wordkey == word:
                print ("you have dealt damage to the enemy")
                wordkey = ""
                damage_dealt += baseAttack
            else:
                print("You have failed your attack")
                wordkey = ""
        if damage_dealt >= monster.health:
            print(" you have defeated the enemy")
            in_combat = 0
        if key == BACKSPACE:
            if wordkey > 0:
                wordkey = wordkey[:len(wordkey) - 1]
                #wordkey = wordkey.replace(" ", "")
                print(wordkey)
        else:
            text = ""
            text += key
            wordkey += text
            print (text)

def mouseClicked():
    print(wordkey)