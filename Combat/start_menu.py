#def setup():
    #size(1080,720)
    #background(250)
    
def draw():
    background(250) #Have a drawn thing instead.
    rect(340,10,370,45) #For title
    rect(340,120,370,100) #For start button
    rect(340,330,370,100) #Options
    rect(340,540,370,100) #Quit
    #Also something for a high score list
    
    #Buttons
    start_button = loadImage("StartButton.png")
    options_button = loadImage("OptionsButton.png")
    quit_button = loadImage("QuitButton.png")
    image(start_button,340,120)
    image(options_button,340,330)
    image(quit_button,340,540)
    
def mouseClicked():
    global value
    
    if mouseX > 340 and mouseX < 710 and mouseY > 120 and mouseY < 220:
        print "Start Game"
    
    elif mouseX > 340 and mouseX < 710 and mouseY > 330 and mouseY < 440:
        print "Options"
   
    elif mouseX > 340 and mouseX < 710 and mouseY > 540 and mouseY < 640:
        print "Quit"