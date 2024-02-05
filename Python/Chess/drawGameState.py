import os
import pygame as p

class DrawGameState():
    def __init__(self,screen,square_size,dimension) -> None:
        self.screen = screen
        self.square_size = square_size
        self.dimension = dimension
        self.images = {}

    def drawBoard(self):
        colors = [p.Color("white"), p.Color("gray")]
        for i in range(self.dimension):
            for t in range(self.dimension):
                color = colors[((i+t)%2)]
                p.draw.rect(self.screen, color,p.Rect(t* self.square_size, i*self.square_size,self.square_size,self.square_size))
            
    def loadImages(self):
        pieces = ['wp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bp', 'bR', 'bN', 'bB', 'bQ', 'bK']
        for piece in pieces:
            image = str(piece) + ".png"
            self.images[piece] = p.transform(p.image.load(os.path.join('images', image)), [self.square_size,self.square_size])

    def drawImages(self):
        pass
            


