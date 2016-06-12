class Entity():
    
    def __init__(self, name = "Test", damage = 1, health = 1, score = 0):
        self.name = name
        self.damage = damage
        self.health = health
        self.score = score
    
 
        
        
        
       
        
easybig_Rat = Entity("Big rat", 1, 3, 0)
easyslime = Entity("Slime", 2, 5, 0)
easyogre = Entity("Ogre", 3, 8, 2)

big_Rat = Entity("Big rat", 2, 5, 0)
slime = Entity("Slime", 1, 5, 0)
ogre = Entity("Ogre", 3, 8, 2)

hardbig_Rat = Entity("Big rat", 2, 3, 0)
hardslime = Entity("Slime", 3, 8, 0)
hardogre = Entity("Ogre", 4, 15, 2)

miniBossCyclops = Entity("Cyclops", 3, 16, 0)
miniBossFairy = Entity("Fairy",2 ,14, 0)

character = Entity("Character", 2, 10, 0)
        
        
earlyMonsters = [easybig_Rat,easyslime,easyogre]

mediumMonsters = [big_Rat,slime,ogre]

hardMonsters = [hardbig_Rat,hardslime,hardogre]