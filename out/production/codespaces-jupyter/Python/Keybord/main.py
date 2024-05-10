import pygame

pygame.init()
pygame.mixer.set_num_channels(50)

timer = pygame.time.Clock()
fps = 60
WIDTH = 52 * 35
HEIGHT = 400
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Python Keybord')

run = True
while run:
    timer.tick(fps)
    screen.fill('gray')
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()
pygame.quit()