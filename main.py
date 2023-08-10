import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.05)
musica = pygame.mixer.music.load("MUSICAS/01 BoxCat Games - Breaking In.mp3")
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound("smw_yoshi_swallow_no_coin.wav")
barulho_fase = pygame.mixer.Sound("smw_1-up.wav")

fonte = pygame.font.SysFont("arial", 40, False, False)

largura = 640
altura = 480

x_circle = randint(100, 150)
y_circle = 10

x_circle2 = randint(200, 250)
y_circle2 = 20

x_circle3 = randint(250, 550)
y_circle3 = 35

x_circle_big = randint(250, 420)
y_circle_big = randint(120, 420)
x_circle_big2 = randint(250, 420)
y_circle_big2 = randint(120, 420)
x_circle_big3 = randint(250, 420)
y_circle_big3 = randint(120, 420)

x = 10
y = int(altura/2)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pixel runner 1.0")

relogio = pygame.time.Clock()

fase = 19
mortes = 0

velocidade = 5

while 1:
    relogio.tick(120)
    tela.fill((0,0,0))

    text_fase = f"Fase: {fase}"
    text_morte = f"Mortes: {mortes}"
    texto = fonte.render(text_fase, False, (255,255,255))
    texto1 = fonte.render(text_morte, False, (255,255,255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    rect = pygame.draw.rect(tela, (255,0,0), (x,y,50,50))
    circle = pygame.draw.circle(tela, (0,0,255), (x_circle,y_circle), 25)

    if pygame.key.get_pressed()[K_a]:
        x -= velocidade

    if pygame.key.get_pressed()[K_d]:
        x += velocidade

    if pygame.key.get_pressed()[K_w]:
        y -= velocidade

    if pygame.key.get_pressed()[K_s]:
        y += velocidade

    if x > 640:
        x = 0
        fase += 1

        barulho_fase.play()

        y_circle = 10
        x_circle = randint(100, 450)

    if x < 0:
        x = 0

    if y < 0:
        y = 0

    if y > 480:
        y = 0

    if rect.colliderect(circle):
        x = 10
        y = largura/2
        mortes += 1

        barulho_colisao.play()

    y_circle += 1
    if y_circle >= altura:
        y_circle = 10
        x_circle = randint(100, 450)

    if fase >= 5:
        circle2 = pygame.draw.circle(tela, (65,115,65), (x_circle2,y_circle2), 25)

        y_circle2 += 1
        if y_circle2 >= altura:
            y_circle2 = 10
            x_circle2 = randint(100, 450)

        if rect.colliderect(circle2):
            x = 10
            y = largura / 2
            mortes += 1

            barulho_colisao.play()

        if circle2.colliderect(circle):
            x_circle2 += 10
            y_circle2 += 10

    if fase == 20:
        tela.fill((255,255,255))
        musica = pygame.mixer.music.load("MUSICAS/02 BoxCat Games - Mt Fox Shop.mp3")
        pygame.mixer.music.play(-1)

        rect = pygame.draw.rect(tela, (255, 0, 0), (x, y, 50, 50))
        circle = pygame.draw.circle(tela, (0, 0, 255), (x_circle, y_circle), 25)
        circle2 = pygame.draw.circle(tela, (65, 115, 65), (x_circle2, y_circle2), 25)

        texto = fonte.render(text_fase, False, (0,0,0))
        texto1 = fonte.render(text_morte, False, (0, 0, 0))

        if fase < 20:
            velocidade = 5

        elif fase == 20:
            velocidade = 8

        y_circle += 3
        y_circle2 += 3

    if fase > 20:
        musica = pygame.mixer.music.load("MUSICAS/03 BoxCat Games - Battle (Special).mp3")
        pygame.mixer.music.play(-1)

        circle = pygame.draw.circle(tela, (0, 0, 255), (x_circle, y_circle), 25)
        circle2 = pygame.draw.circle(tela, (65, 115, 204), (x_circle2, y_circle2), 25)
        circle3 = pygame.draw.circle(tela, (255, 255, 204), (x_circle3, y_circle3), 25)

        circle_big = pygame.draw.circle(tela, (255, 153, 204), (x_circle_big, y_circle_big), 35)
        circle_big2 = pygame.draw.circle(tela, (255, 153, 204), (x_circle_big2, y_circle_big2), 35)
        circle_big3 = pygame.draw.circle(tela, (255, 153, 204), (x_circle_big3, y_circle_big3), 35)

        y_circle3 += 2
        if y_circle3 >= altura:
            y_circle3 = 30
            x_circle3 = randint(300, 450)

        y_circle2 += 2
        y_circle += 2

        if circle2.colliderect(circle_big) or circle2.colliderect(circle_big2) or circle2.colliderect(circle_big3):
            x_circle2 = randint(150, 460)
            y_circle2 = 10

        if circle.colliderect(circle_big) or circle.colliderect(circle_big2) or circle.colliderect(circle_big3):
            x_circle = randint(150, 460)
            y_circle = 10

        if circle3.colliderect(circle_big) or circle3.colliderect(circle_big2) or circle3.colliderect(circle_big3):
            x_circle3 = randint(150, 460)
            y_circle3 = 10

        if rect.colliderect(circle3) or rect.colliderect(circle_big2) or rect.colliderect(circle_big3) or rect.colliderect(circle_big):
            x = 10
            y = largura / 2
            mortes += 1

            barulho_colisao.play()

        if x > 640:
            x = 0
            fase += 1

            barulho_fase.play()

            circle = pygame.draw.circle(tela, (0, 0, 255), (x_circle, y_circle), 25)
            circle2 = pygame.draw.circle(tela, (65, 115, 204), (x_circle2, y_circle2), 25)
            circle3 = pygame.draw.circle(tela, (255, 255, 204), (x_circle3, y_circle3), 25)

            circle_big = pygame.draw.circle(tela, (255, 153, 204), (x_circle_big, y_circle_big), 35)
            circle_big2 = pygame.draw.circle(tela, (255, 153, 204), (x_circle_big2, y_circle_big2), 35)
            circle_big3 = pygame.draw.circle(tela, (255, 153, 204), (x_circle_big3, y_circle_big3), 35)

            y_circle = 10
            x_circle = randint(100, 450)
            y_circle2 = 10
            x_circle2 = randint(150, 460)
            y_circle3 = 10
            x_circle3 = randint(150, 460)

            x_circle_big = randint(250, 420)
            y_circle_big = randint(120, 420)
            x_circle_big2 = randint(250, 420)
            y_circle_big2 = randint(120, 420)
            x_circle_big3 = randint(250, 420)
            y_circle_big3 = randint(250, 420)

    tela.blit(texto, (450,40))
    tela.blit(texto1, (20, 20))
    pygame.display.update()