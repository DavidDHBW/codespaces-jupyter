import pygame as p
import chess
import os
from drawGameState import DrawGameState

os.environ['SDL_AUDIODRIVER'] = 'directx' #fix for the alsa lib error

WIDTH = HEIGHT = 512
DIMENSION = 8  #chess board is 8x8
SQUARE_SIZE = WIDTH/DIMENSION
MAX_FPS = 15 #if I want to add animations later
IMAGES ={}

screen = p.display.set_mode((WIDTH,HEIGHT))
drawgame = DrawGameState(screen,SQUARE_SIZE,DIMENSION)
clock = p.time.Clock()

p.init()

#loadImages()
gs = chess.gameState()
print(gs.board)

running = True
while running:
    for e in p.event.get():
        if e.type == p.QUIT:
            running = False

    drawgame.drawBoard()
    #drawgame.loadImages()
    clock.tick(MAX_FPS)
    p.display.flip()
p.quit()