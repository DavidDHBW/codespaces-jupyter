from damageCalculation import DamageCalculation
from weapon import Weapon
from characterLists import *


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
        print(dc.damage)
        damage = target.attackArmor(dc.damage)
        
        target.getDamage(damage)
        print(damage)        
        print(target.health)
        
    def attackArmor(self, damage): # return the total damage
        if self.armor <= 0:
            return damage
        damageDif = self.armor - damage
        if damageDif < 0:
            self.armor = 0
            return -damageDif
        if damageDif == 0:
            self.armor = 0
            return 0
        if damageDif > 0:
            self.armor = damageDif
            return 0
            
        
#Tests
        
e2=Character("char", 50,False,4,"rangedFighter", "bow",True,10)
e3=Character("char", 50,False,4,"meleeFighter", "spear",True,1)
selectedEnemyCharacters.append(e2)
selectedEnemyCharacters.append(e3)
char = Character("char", 50,False,4,"meleeFighter", "sword",True,10)

char.attack(e3)
