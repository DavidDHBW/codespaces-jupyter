#inputs output file
import pygame as p
import chess



WIDTH = HEIGHT = 512
DIMENSION = 8 #chess board is 8x8
SQUARE_SIZE = WIDTH/DIMENSION
MAX_FPS = 15 #if I want to add animations later
IMAGES ={}

def loadImages():
    
    
    pieces = ['wp','wR','wN','wB','wQ','wK','bp','bR','bN','bB','bQ','bK']
    for piece in pieces:
        IMAGES[piece] = p.transform(p.image.load("images/"+piece+".png"),[SQUARE_SIZE,SQUARE_SIZE])  
#get the image for the white pawn by 'IMAGES['wp']'    
#to adjust the image size to the square size i used p.transform()

def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    loadImages()
    gs = chess.gameState()
    print(gs.board)
main()

        

