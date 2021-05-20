import pygame
from pygame.constants import K_BACKSPACE

pygame.init()

screen = pygame.display.set_mode((1280, 720))

#Background
background_image = pygame.image.load('background.png')
screen.fill((200, 200, 200))
screen.blit(background_image, (0, 0))

#Título e ícone
pygame.display.set_caption("PyPaint")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#Mouse
isPressed = False
right_click = False
draw_size = 5

#Botões
text_font = pygame.font.Font('freesansbold.ttf', 20)
color_text = text_font.render("Cor atual", True, (40, 40, 40))
screen.blit(color_text, (1171, 50))

colour = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 165, 0), (255, 255, 0)]
b_posx = 1200
b_posy = 200

buttons = []
for i in range(6):
    button = pygame.draw.rect(screen, colour[i], (b_posx, b_posy, 30, 30))
    buttons.append(button)
    b_posy += 32

#Cor
cor = (0, 0, 0)

#Se o botão esquerdo do mouse é pressionado
def click(x, y, cor):
    if x >= 1150:
        pass
    else:
        pygame.draw.circle(screen, cor, (x, y), draw_size)

#Se o botão direito do mose é pressionado
def erase(x, y):
    pygame.draw.circle(screen, (255, 255, 255), (x, y), draw_size)

#Loop principal
running = True
while running:
    posx, posy = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Verifica os botões do mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                isPressed = True
            if event.button == 3:
                right_click = True
            if event.button == 4:
                draw_size += 1
            if event.button == 5:
                draw_size -= 1
        if event.type == pygame.MOUSEBUTTONUP:
            isPressed = False
            right_click = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen.blit(background_image, (0, 0))   

    if isPressed:
        if posx >= 1200 and posx <= 1230:
            if posy >= 200 and posy <= 230:
                cor = colour[0]
            elif posy >= 232 and posy <= 262:
                cor = colour[1]
            elif posy >= 264 and posy <= 294:
                cor = colour[2]
            elif posy >= 296 and posy <= 326:
                cor = colour[3]
            elif posy >= 328 and posy <= 358:
                cor = colour[4]
            elif posy >= 360 and posy <= 390:
                cor = colour[5]        
        click(posx, posy, cor)
    
    if right_click:
        erase(posx, posy)

    active_color_box = pygame.draw.rect(screen, cor, (1177, 80, 80, 40))
    pygame.display.update()