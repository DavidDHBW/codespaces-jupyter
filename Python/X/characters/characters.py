global selectedEnemyCharacters
selectedPlayerCharacters = [3]
selectedEnemyCharacters = [3]

class Character:
    def __init__(self, name, health,enemy, level, warriorType, weapon, hasMove, armor):
        self.name = name #display name
        self.health = health 
        self.enemy = enemy #bool 
        self.level = level # from 1-10
        self.warriorType = warriorType #wizzard , rangedFighter, meleeFighter
        self.weapon = weapon #depends also on the worrior type
        self.hasMove = hasMove
        self.armor = armor #from 1-5
    
    def damageCalculation(self, target):
        pass
           
    def getDamage(self,damage):
        self.health -= damage
        
    def attack(self, target):
        self.damageCalculation( target)
        
    
