import random
import characterLists
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from rangedInteger import RangedInt 
enemies = characterLists.selectedEnemyCharacters

advantages = []
disadvantages = []
class DamageCalculation:
    def __init__(self, character, target):
        self.ranFactorDif = self.getRanFactorDiff(character, target)
        self.ranFactor = self.getRanFactor()
        self.damage =  int(character.weapon.damage * self.ranFactor)

        
    def getRanFactor(self):
        ranLow = 0.8
        ranHigh = 1.2
        ranLow += self.ranFactorDif
        ranHigh += self.ranFactorDif
        ranFactor = random.uniform(ranLow,ranHigh)
        return ranFactor    
    def getRanFactorDiff(self, character, target):
        ranFactorDiff = 0.0
        ranFactorDiff -= self.onFieldEnemy(target)
        ranFactorDiff -= self.weaponAdv(character, target)
        ranFactorDiff -= self.weaponDeffenseDiff(target)
        return ranFactorDiff    
    def onFieldEnemy(self, target): # calc disatvantage of the enemies on field (if melee fighter is there wizzard is protectet)

        if target.warriorType == "meleeFighter":
            return 0
        print(enemies)
        isMeleeFighter = False
        isRangedFighter = False 
        for enemy in enemies:
            if enemy.warriorType == "meleeFighter":
                isMeleeFighter = True
            if enemy.warriorType == "rangedFighter":
                isRangedFighter = True 
        
        if target.warriorType == "rangedFighter":
            if isMeleeFighter: return 0.5
            else: return 0
        
        if target.warriorType == "wizzard":
            if isMeleeFighter:
                return 0.9
            if isRangedFighter:
                return 0.7
        return 0
        
        #wizzard , rangedFighter, meleeFighter
    def weaponAdv(self, character, target):
        #character is meleeFighter
        if character.warriorType ==  "meleeFighter":
            if target.warriorType == "meleeFighter":
                weapons = ["sword","axe","spear"]
                for t in range(0,3):
                    i = RangedInt(startValue=t,minValue=0,maxValue=2) # self createt limited int to have the triangle advantage/disadvantage
                    if character.weapon.weaponType == weapons[i.number]:
                        if target.weapon.weaponType ==weapons[i.number]:
                            return 0
                        if target.weapon.weaponType == weapons[i.raiseInt()]:
                            return -0.2
                        if target.weapon.weaponType == weapons[i.raiseInt()]:
                            return 0.2
        return 0
        #character is rangedFighter || no impact
        #character is wizzard || no impact
    def weaponDeffenseDiff(self,target):
        defense = target.weapon.defense
        return defense/25 # bei 5 defense Punkten disatvantage von 0.2
        
  
 