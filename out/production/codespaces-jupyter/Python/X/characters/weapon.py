
class Weapon:
    def __init__(self,weaponType):
        self.weaponType = weaponType
        self.damage, self.defense = self.getDamage()
    
    def getDamage(self):
        #melee Fighter
        if self.weaponType == "sword":
            damage = 5
            defense = 9
        if self.weaponType == "axe":
            damage = 9
            defense = 5
        if self.weaponType == "spear":
            damage = 7
            defense = 7
        
        #wizzard
        if self.weaponType == "wand":
            damage = 1
            defense = 0
        
        #range Fighter
        if self.weaponType == "bow":
            damage = 3
            defense = 5
        if self.weaponType == "crossbow":
            damage = 4
            defense = 2
        try: 
            return damage, defense
        except:
            return 0
    
            

       
        