
class GameStateHandler:
    def __init__(self):
        self.gameState = [] #initaliaze as list to ensure menu and fight can both be opened the same time
        self.gameState.append(startMenu)
        
    def addGameState(self, gsAdd):
        self.gameState.append(gsAdd)
        
    def removeGameState(self,gsRmv):
        self.gameState.remove(gsRmv)
        
#Menu lists       
startMenu = "startMenu"
escapeMenu = "escapeMenu"
inGame = "inGame"
inFight = "inFight"