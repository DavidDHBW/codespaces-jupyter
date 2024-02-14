import random
import characterLists
enemies = characterLists.selectedEnemyCharacters

class DamageCalculation:
    def DamageCalculation(self, character, target):
        ranLow = 0.8
        globals
        ranFactor = random.uniform(ranLow,1.1)
        ranFactorDif -= self.onFieldEnemy(target)
        ranFactorDif += self.weaponAdv(character, target)
        
    def onFieldEnemy(self, target): # calc disatvantage of the enemies on field (if melee fighter is there wizzard is protectet)

        if target.warriorType == "meleeFighter":
            return 0
        
        for enemy in enemies:
            if enemy.warriorType == "meleeFighter":
                isMeleeFighter = True
            if enemy.warriorType == "rangedFighter":
                isRangedFighter = True 
        
        if target.warriorType == "rangedFighter":
            if isMeleeFighter: return 0.4
            else: return 0
        
        if target.warriorType == "wizzard":
            if not isMeleeFighter and not isRangedFighter:
                return 0
            else:
                if isMeleeFighter:
                    return 0.7
                if isRangedFighter:
                    return 0.5
        else: return 0
        
            
    
        #wizzard , rangedFighter, meleeFighter
    def weaponAdv(self, characte, target):
        pass
        