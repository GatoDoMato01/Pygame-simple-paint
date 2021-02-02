import pygame

pygame.init()

width, height = (800, 600)
screen = pygame.display.set_mode((width, height))
background = (0, 0, 0)
screen.fill(background)

color = (255, 255, 255)

colour = [(0,255,0),(0,0,255),(255,0,0),(255,255,255)]
posx = [50,90,130,170]
posy = 550

buttons = []

for i in range(0,4):
    button = pygame.draw.rect(screen, colour[i], (posx[i], posy, 30, 30))
    buttons.append(button)

def click(x, y, color):
    if event.type == pygame.MOUSEBUTTONUP:
        return pygame.draw.circle(screen, color, pygame.mouse.get_pos(), 5, 0)
    
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    buttons

    pos = pygame.mouse.get_pos()
    x, y = pos

    if event.type == pygame.MOUSEBUTTONUP:
        if x >= posx[0] and y >= posy and x <= posx[0]+30 and y <= posy+30:
            color = colour[0]
        elif x >= posx[1] and y >= posy and x <= posx[1]+30 and y <= posy+30:
            color = colour[1]
        elif x >= posx[2] and y >= posy and x <= posx[2]+30 and y <= posy+30:
            color = colour[2]
        elif x >= posx[3] and y >= posy and x <= posx[3]+30 and y <= posy+30:
            color = colour[3]

    click(x, y, color)
    
    pygame.display.flip()