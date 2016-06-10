# Imports for the other files in the program also random words
import random
from Word_List import *
from Entities import *
from Floors import *
from Encounters import *
randEasy = random.randint(0,len(easyWords) - 1)
randFloor = random.randint(0,len(floor_layouts) - 1)
#randEarlyMonsters = random.randint(0,len(earlyMonsters) - 1)
word = (easyWords[randEasy])
# Setting up the global values that will be used in checking the word
baseAttack = character.damage
health = character.health
armor = character.armor
wordkey = ""
winner = 0
in_combat = 0
monster_setup = 0
current_Floor = floor_layouts[randFloor]
floor_level = 1
floor_room = 0
damage_dealt = 0
start_menu = 1
character_Select_start_menu = 0
character_Select = 0
options_start_menu = 0
game = 0
print(current_Floor)

def setup():
   size(1080,720)
   print("setup happened")

def draw():
   global monster_setup
   global monster
   global in_combat
   global floor_room
   global health
   fill(255)
   rect(0, 0, 1080, 720)
   forest_Background = loadImage("ForestBackground.png")
   image(forest_Background, 0, 0)
   if current_Floor[floor_room] == "m" and game == 1:
       in_combat = 1
    
   if in_combat == 1:
       if floor_level <= 2:
           if monster_setup == 0:
            randEarlyMonsters = random.randint(0,len(earlyMonsters) - 1)
            monster = earlyMonsters[randEarlyMonsters]
            monster_setup = 1
           if monster.name == "Slime":
                slime_Image = loadImage("SlimeEasy.png")
                image(slime_Image, 700, 400)
           if monster.name == "Big rat":
                rat_Image = loadImage("BigRatEasy.png")
                image(rat_Image, 700, 400)
           if monster.name == "Ogre":
               ogre_Image = loadImage("OgreEasy.png")
               image(ogre_Image, 700, 400)
       textSize(35)
       fill(0)
       text("Health: ", 50, 50)
       text(health, 200, 50)
       text(word, 200 , 200)
       text(wordkey, 500, 540)
   if character_Select_start_menu == 1:
        fill(255)
        backdrop = loadImage("SelectBackground.png")
        background(backdrop)
        head_1 = loadImage("choice1.png") #Guy Face
        head_2 = loadImage("choice2.png") #Girl Face
        head_3 = loadImage("choice1.2.png") #Excited Guy Face
        head_4 = loadImage("choice2.2.png") #Excited Girl Face
        rect(140,120,300,300)
        rect(640,120,300,300)
        #Default faces
        image(head_1,140,120)
        image(head_2,640,120)
        
        #Animations for when the mouse goes over a character head
        if mouseX > 140 and mouseX < 440 and mouseY > 120 and mouseY < 420:
            image(head_3,140,120)
        
        elif mouseX > 640 and mouseX < 940 and mouseY > 120 and mouseY < 420: 
            image(head_4,640,120)
   if start_menu == 1:
        background(250) #Have a drawn thing instead.
        fill(255)
        rect(340,10,370,45) #For title
        rect(340,120,370,100) #For start button
        rect(340,330,370,100) #options_start_menu
        rect(340,540,370,100) #Quit
        #Also something for a high score list
        
        #Buttons
        start_button = loadImage("StartButton.png")
        options_start_menu_button = loadImage("options_start_menuButton.png")
        quit_button = loadImage("QuitButton.png")
        image(start_button,340,120)
        image(options_start_menu_button,340,330)
        image(quit_button,340,540)
   if current_Floor[floor_room] == "u" and game == 1:
       fill(0)
       textSize(20)
       text(cleric_passes.words, 500, 500)
       health = cleric_passes.heal_hurt(health,2)
       print (health)
       floor_room += 1
       delay(5000)
        


def keyTyped():
     global wordkey
     global winner
     global monster
     global in_combat
     global damage_dealt
     global floor_room
     if in_combat == 1:
        if key == ENTER:
            if wordkey == word:
                print ("You have dealt damage to the enemy")
                wordkey = ""
                damage_dealt += baseAttack
            else:
                print("You have failed your attack")
                wordkey = ""
        if damage_dealt >= monster.health:
            print("You have defeated the enemy")
            in_combat = 0
            floor_room += 1
            damage_dealt = 0
        if key == BACKSPACE:
            if wordkey > 0:
                wordkey = wordkey[:len(wordkey) - 1]
                #wordkey = wordkey.replace(" ", "")
                print(wordkey)
        elif key != BACKSPACE and key != ENTER:
            text = ""
            text += key
            wordkey += text
            print (text)

def mouseClicked():
   global start_menu
   global character_Select_start_menu
   global in_combat
   global options_start_menu
   global game
   print(wordkey)
   if start_menu == 1:
        if mouseX > 340 and mouseX < 710 and mouseY > 120 and mouseY < 220:
            print "Start Game"
            start_menu = 0
            character_Select_start_menu = 1
        
        elif mouseX > 340 and mouseX < 710 and mouseY > 330 and mouseY < 440:
            print "options_start_menu"
    
        elif mouseX > 340 and mouseX < 710 and mouseY > 540 and mouseY < 640:
            print "Quit"
            exit()
   elif character_Select_start_menu == 1:
        if mouseX > 140 and mouseX < 440 and mouseY > 120 and mouseY < 420:
            character_Select = 1
            character_Select_start_menu = 0
            game = 1
            print("1")
        elif mouseX > 640 and mouseX < 940 and mouseY > 120 and mouseY < 420:
            character_Select = 2
            character_Select_start_menu = 0
            game = 1