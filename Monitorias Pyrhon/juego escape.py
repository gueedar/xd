import pygame
import random

pygame.init()

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)

ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Ecape del negro")

reloj = pygame.time.Clock()
speed_player = 5
speed_hunter = 3

fuente = pygame.font.SysFont(None, 36)

def mostrar_text(texto, x, y):
    superficie_texto = fuente.render(texto, True, ROJO)
    ancho_texto, alto_texto = fuente.size(texto)
    x = (ancho - ancho_texto) // 2 
    y = (alto - alto_texto) // 2
    pantalla.blit(superficie_texto, (x, y))

def colision_con_paredes(rect, paredes):
    for pared in paredes:
        if rect.colliderect(pared):
            return True
    return False

def generar_rect_fuera_de_paredes(ancho, alto, paredes, size=25):
    while True:
        rect = pygame.Rect(random.randint(0, ancho - size), random.randint(0, alto - size), size, size)
        if not colision_con_paredes(rect, paredes):
            return rect
        
def generar_paredes_aleatorias(num_paredes, ancho, alto, max_whit=200, max_height=50):
    paredes = []
    for _ in range(num_paredes):
        while True:
            x = random.randint(0, ancho - max_whit)
            y = random.randint(0, alto - max_height)
            width = random.randint(50, max_whit)
            height = random.randint(20, max_height)
            nueva_pared = pygame.Rect(x, y, width, height)
            if not colision_con_paredes(nueva_pared, paredes):
                paredes.append(nueva_pared)
                break
    return paredes

paredes = generar_paredes_aleatorias(5, ancho, alto)

player = generar_rect_fuera_de_paredes(ancho, alto, paredes)
hunter = generar_rect_fuera_de_paredes(ancho, alto, paredes)

game_over = False

while not game_over:
    pantalla.fill(BLANCO)

    for pared in paredes:
        pygame.draw.rect(pantalla, NEGRO, pared)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game_over = True

    teclas = pygame.key.get_pressed()
    movimiento_jugador = player.copy()
    if teclas[pygame.K_LEFT] and player.left > 0:
        movimiento_jugador.x += speed_player
        if not colision_con_paredes(movimiento_jugador, paredes):
            player.x -= speed_player
    if teclas[pygame.K_RIGHT] and player.right < ancho:
        movimiento_jugador.x += speed_player
        if not colision_con_paredes(movimiento_jugador, paredes):
            player.x += speed_player
    if teclas[pygame.K_UP] and player.top > 0:
        movimiento_jugador.y -= speed_player
        if not colision_con_paredes(movimiento_jugador, paredes):
            player.y -= speed_player
    if teclas[pygame.K_DOWN] and player.bottom < alto:
        movimiento_jugador.y += speed_player
        if not colision_con_paredes(movimiento_jugador, paredes):
            player.y += speed_player

    if colision_con_paredes(player, paredes):
        game_over = True
        mostrar_text("Game Over! Tocaste una pared", ancho // 2, alto // 2)
        pygame.display.update()
        pygame.time.delay(2000)
        break
    
    movimiento_cazador = hunter.copy()
    if hunter.x < player.x:
        movimiento_cazador.x += speed_hunter
        if not colision_con_paredes(movimiento_cazador, paredes):
            hunter.x += speed_hunter
    if hunter.x > player.x:
        movimiento_cazador.x -= speed_hunter
        if not colision_con_paredes(movimiento_cazador, paredes):
            hunter.x -= speed_hunter
    if hunter.y < player.y:
        movimiento_cazador.y += speed_hunter
        if not colision_con_paredes(movimiento_cazador, paredes):
            hunter.y += speed_hunter
    if hunter.y > player.y:
        movimiento_cazador.y -= speed_hunter
        if not colision_con_paredes(movimiento_cazador, paredes):
            hunter.y -= speed_hunter

    if player.colliderect(hunter):
        game_over = True
        mostrar_text("you was hunted!", ancho // 2, alto // 2)
        pygame.update()
        pygame.time.delay(2000)
        break

    pygame.draw.rect(pantalla, AZUL, player)
    pygame.draw.rect(pantalla, NEGRO, hunter)

    pygame.display.update()

    if game_over:
        pygame.time.delay(2000)

    reloj.tick(60)

    
pygame.quit()