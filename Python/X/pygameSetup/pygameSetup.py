import pygame as p
import sys

p.init()
#Window Settings
baseWidth, baseHeight = 1800,900
windowWidth, windowHeight = 700,500
windowWidth, windowHeight = p.display.Info().current_w,p.display.Info().current_h
window = p.display.set_mode((windowWidth,windowHeight))
screen = p.Surface((baseWidth,baseHeight))

#pygame Settings
maxFps = 60
p.display.set_caption("X")
clock = p.time.Clock()
dt = clock.tick(maxFps)/1000

def pygameLoop():
    #GET INPUT
    for event in p.event.get():
        keys = p.key.get_pressed()
        if event.type == p.QUIT:
            running = False
            p.quit()
            sys.exit()
            
        

        #DRAW THE GAME
        #screen.blit(background,(0,0))   |||replace background with png
    scaled_surface = p.transform.scale(screen, (windowWidth, windowHeight))
    window.blit(scaled_surface,(0,0))
    p.display.flip()


    dt = clock.tick(maxFps)/1000  