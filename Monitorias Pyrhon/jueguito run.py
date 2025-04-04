import pygame
import sys
import random
import time

pygame.init()

pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Evitar al negro')

blanco = (255, 255, 255)
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

#jugador
jugador_width = 50
jugador_heigth = 50
jugador_x = 375
jugador_y = 500
velocidad = 5

#enemigo
enemigo = []
enemigos_count = 1
enemigo_width = 50
enemigo_heigth = 50
enemigo_vel = 5

#disparos
disparos = []
disparo_vel = 7

#puntuacion
puntuacion = 0
fuente = pygame.font.SysFont("Arial", 30)

ultimo_tiempo = time.time()

def crear_enemigos(cantidad):
    global enemigos, enemigo_width, enemigo_heigth
    enemigos = []
    nuevo_tamano = max(10, 50 - (cantidad // 5))
    enemigo_width = nuevo_tamano
    enemigo_heigth = nuevo_tamano
    
    for _ in range(cantidad):
        enemigo_x = random.randint(0, 750)
        enemigo_y = random.randint(-150, -50)
        enemigos.append([enemigo_x, enemigo_y])

crear_enemigos(enemigos_count)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    tiempo_actual = time.time()
    if tiempo_actual - ultimo_tiempo > 15:
        enemigos_count *= 2
        crear_enemigos(enemigos_count)
        ultimo_tiempo = tiempo_actual

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT] and jugador_x > 0:
        jugador_x -= velocidad
    if teclas[pygame.K_RIGHT] and jugador_x < 750:
        jugador_x += velocidad
    if teclas[pygame.K_UP] and jugador_y > 0:
        jugador_y -= velocidad
    if teclas[pygame.K_DOWN] and jugador_y < 550:
        jugador_y += velocidad

    #disparos
    if teclas[pygame.K_SPACE]:
        disparos.append([jugador_x + jugador_width // 2 - 5, jugador_y])

    for enemigo in enemigos:
        enemigo[1] += enemigo_vel
        if enemigo[1] > 600:
            enemigo[1] = random.randint(-150, 50)
            enemigo[0] = random.randint(0, 750)
            puntuacion += 1


    for enemigo in enemigos:
        enemigo[1] += enemigo_vel
        if(jugador_x < enemigo[0] + enemigo_width and
           jugador_x + jugador_width > enemigo[0] and
           jugador_y < enemigo[1] + enemigo_heigth and
            jugador_y + jugador_heigth > enemigo[1]):
            texto_final = fuente.render("Perdio tonta >:c: ", str(puntuacion), True, (255, 0, 0))     
            pantalla.blit(texto_final, (255, 255))
            pygame.display.filp() 
            pygame.time.wait(2000)
            pygame.quit()
            sys.exit()

    pantalla.fill(blanco)

    pygame.draw.rect(pantalla, verde, (jugador_x, jugador_y, jugador_width, jugador_heigth))

    for enemigo in enemigos:
        pygame.draw.rect(pantalla, rojo, (enemigo[0], enemigo[1], enemigo_width, enemigo_heigth))
    
    texto_puntuacion = fuente.render(f"Puntuacion: {puntuacion}", True, azul)
    pantalla.blit(texto_puntuacion, (10, 10))

    pygame.display.flip()

    pygame.time.Clock().tick(60)
