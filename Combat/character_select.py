def draw():
    background(250)
    rect(140,120,300,300)
    rect(640,120,300,300)

def mouseClicked():
    global value
    character_select = 0
    if mouseX > 140 and mouseX < 440 and mouseY > 120 and mouseY < 420: #Selects character #1
        character_select = 1
        print character_select
    elif mouseX > 640 and mouseX < 940 and mouseY > 120 and mouseY < 420: #Selects character #2
        character_select = 2
        print character_select
    if character_select > 0:
        # Exits