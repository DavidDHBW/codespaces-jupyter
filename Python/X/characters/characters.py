from damageCalculation import DamageCalculation
from weapon import Weapon


class Character:
    def __init__(self, name, health,enemy, level, warriorType, weaponType, hasMove, armor):
        self.name = name #display name
        self.health = health 
        self.enemy = enemy #bool 
        self.level = level # from 1-10
        self.warriorType = warriorType #wizzard , rangedFighter, meleeFighter
        self.weapon = Weapon(weaponType) #depends also on the worrior type
        self.hasMove = hasMove
        self.armor = armor #from 1-5
    

           
    def getDamage(self,damage):
        self.health -= damage
        
    def attack(self, target):
        dc = DamageCalculation(self, target)
        damage = dc.damage
        print(damage)
        
    
char = Character("char", 50,False,4,"meleeFighter", "spear",True,10)
target = Character("char", 50,False,4,"meleeFighter", "sword",True,10)
char.attack(target)
