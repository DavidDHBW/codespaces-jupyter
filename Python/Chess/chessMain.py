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

sqSelected = () #last click of the user
playerClicks = []#player clicks

p.init()
drawgame.loadImages()
gs = chess.gameState()


    



running = True
while running:
    for e in p.event.get():
        if e.type == p.QUIT:
            running = False
        elif e.type == p.MOUSEBUTTONDOWN:
            mousePos = p.mouse.get_pos()
            col = mousePos[0]//SQUARE_SIZE
            row = mousePos[1]//SQUARE_SIZE
            if sqSelected == (row, col):
                sqSelected = ()
                playerClicks = []
            else:
                sqSelected = (row, col)
                playerClicks.append(sqSelected)
            if len(playerClicks) == 2:
                move = chess.Move(playerClicks[0], playerClicks[1], gs.board)
                print(move.getChessNotation())
                gs.makeMove(move)
                sqSelected = ()
                playerClicks = []
            

            

    drawgame.drawBoard()
    drawgame.drawImages(gs.board)
    
    clock.tick(MAX_FPS)
    p.display.flip()
p.quit()

