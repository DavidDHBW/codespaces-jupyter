from pygameSetup import pygameSetup
from gameStateHandler import GameStateHandler 


running = True

#initialize classes
gs = GameStateHandler()
print(gs.gameState)

while running:
    pygameSetup.pygameLoop()
    
    



