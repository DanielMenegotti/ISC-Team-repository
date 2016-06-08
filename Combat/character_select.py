
def draw():   
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

def mouseClicked():
    global value
    if mouseX > 140 and mouseX < 440 and mouseY > 120 and mouseY < 420: #Selects character #1
        character_select = 1
        print character_select
    elif mouseX > 640 and mouseX < 940 and mouseY > 120 and mouseY < 420: #Selects character #2
        character_select = 2
        print character_select
    #if character_select > 0:
        # Exits
   