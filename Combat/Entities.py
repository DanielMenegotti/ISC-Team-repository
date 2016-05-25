
class monster():
    
    def __init__(self, name = "Test", damage = 1, health = 1, armor = 0):
        self.name = name
        self.damage = damage
        self.health = health
        self.armor = armor
        
        
big_Rat = monster("Big rat", 1, 3, 0)
slime = monster("slime",1,5,0)
ogre = monster("ogre", 3, 8, 2)
        
        
earlyMonsters = [big_Rat,slime]
        