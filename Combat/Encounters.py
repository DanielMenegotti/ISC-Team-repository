from Entities import *

class Utility():
    
    def __init__(self,words):
        self.words = words
        
    def heal_hurt(self,health,heal_or_hurt):
        health += heal_or_hurt
        
        return health
        
cleric_passes = Utility("A cleric passes by, along the way he heals you")