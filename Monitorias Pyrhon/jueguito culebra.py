import pygame
import time
import random

pygame.init()

blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

ancho = 600
alto = 600

pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('Juego de la Culebra')

reloj = pygame.time.Clock()

tamaño_culebra = 10
velocidad_culebra = 15

fuente = pygame.font.SysFont("bahnschrift", 25)

def mostrar_puntaje(puntaje):
    valor = fuente.render("Puntaje: " + str(puntaje), True, blanco)
    pantalla.blit(valor, [0, 0])

def juego():
    x1 = ancho / 2
    y1 = alto / 2

    x1_cambio = 0
    y1_cambio = 0

    culebra_lista = []
    longitud_culebra = 1

    comida_x = round(random.randrange(0, ancho - tamaño_culebra) / 10.0) * 10.0
    comida_y = round(random.randrange(0, alto - tamaño_culebra) / 10.0) * 10.0

    fin_juego = False
    while not fin_juego:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fin_juego = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x1_cambio = -tamaño_culebra
                    y1_cambio = 0
                elif evento.key == pygame.K_RIGHT:
                    x1_cambio = tamaño_culebra
                    y1_cambio = 0
                elif evento.key == pygame.K_UP:
                    y1_cambio = -tamaño_culebra
                    x1_cambio = 0
                elif evento.key == pygame.K_DOWN:
                    y1_cambio = tamaño_culebra
                    x1_cambio = 0

        if x1 >= ancho or x1 < 0 or y1 >= alto or y1 < 0:
            fin_juego = True
        x1 += x1_cambio
        y1 += y1_cambio
        pantalla.fill(azul)
        pygame.draw.rect(pantalla, verde, [comida_x, comida_y, tamaño_culebra, tamaño_culebra])
        culebra_cabeza = []
        culebra_cabeza.append(x1)
        culebra_cabeza.append(y1)
        culebra_lista.append(culebra_cabeza)

        if len(culebra_lista) > longitud_culebra:
            del culebra_lista[0]

        for segmento in culebra_lista[:-1]:
            if segmento == culebra_cabeza:
                fin_juego = True

        for segmento in culebra_lista:
            pygame.draw.rect(pantalla, negro, [segmento[0], segmento[1], tamaño_culebra, tamaño_culebra])

        mostrar_puntaje(longitud_culebra - 1)

        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, ancho - tamaño_culebra) / 10.0) * 10.0
            comida_y = round(random.randrange(0, alto - tamaño_culebra) / 10.0) * 10.0
            longitud_culebra += 1

        reloj.tick(velocidad_culebra)

    pygame.quit()
    quit()

juego()
