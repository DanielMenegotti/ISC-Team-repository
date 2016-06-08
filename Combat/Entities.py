class Entity():
    
    def __init__(self, name = "Test", damage = 1, health = 1, armor = 0):
        self.name = name
        self.damage = damage
        self.health = health
        self.armor = armor
    
 
        
        
big_Rat = Entity("Big rat", 1, 3, 0)
ratImg = loadImage("BigRat.png")
slime = Entity("Slime", 1, 5, 0)
slimeImg = loadImage("Slime.png")
ogre = Entity("ogre", 3, 8, 2)
character = Entity("Character", 2, 10, 0)
        
        
earlyMonsters = [big_Rat,slime]