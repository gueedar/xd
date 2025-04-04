import pygame
import sys

pygame.init()

ANCHO, ALTO = 800, 600

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pong")

reloj = pygame.time.Clock()

PALETA_ANCHO, PALETA_ALTO = 20, 100
paleta_izquierda = pygame.Rect(30, ALTO // 2 - PALETA_ALTO // 2, PALETA_ANCHO, PALETA_ALTO)
paleta_derecha = pygame.Rect(ANCHO - 50, ALTO // 2 - PALETA_ALTO // 2, PALETA_ANCHO, PALETA_ALTO)
velocidad_paleta = 7

PELOTA_TAMANO = 20
pelota = pygame.Rect(ANCHO // 2 - PELOTA_TAMANO // 2, ALTO // 2 - PELOTA_TAMANO // 2, PELOTA_TAMANO, PELOTA_TAMANO)
velocidad_pelota_x = 5
velocidad_pelota_y = 5

puntuacion_izquierda = 0
puntuacion_derecha = 0
fuente = pygame.font.SysFont(None, 50)

def dibujar():
    pantalla.fill(NEGRO)
    pygame.draw.rect(pantalla, BLANCO, paleta_izquierda)
    pygame.draw.rect(pantalla, BLANCO, paleta_derecha)
    pygame.draw.ellipse(pantalla, BLANCO, pelota)
    pygame.draw.aaline(pantalla, BLANCO, (ANCHO // 2, 0), (ANCHO // 2, ALTO))
    texto_puntuacion = fuente.render(f"{puntuacion_izquierda}{puntuacion_derecha}", True, BLANCO)
    pantalla.blit(texto_puntuacion, (ANCHO // 2 - texto_puntuacion.get_width() // 2, 20))

def mover_paletas(modo):

    if modo == "Jugador_vs_Jugador":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and paleta_izquierda.top > 0:
            paleta_izquierda.y -= velocidad_paleta
        if keys[pygame.K_s] and paleta_izquierda.bottom < ALTO:
            paleta_izquierda.y += velocidad_paleta
        if keys[pygame.K_UP] and paleta_derecha.top > 0:
            paleta_derecha.y -= velocidad_paleta
        if keys[pygame.K_DOWN] and paleta_derecha.bottom < ALTO:
            paleta_derecha.y += velocidad_paleta

    elif modo == "Jugador_vs_Maquina":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and paleta_izquierda.top > 0:
            paleta_izquierda.y -= velocidad_paleta
        if keys[pygame.K_s] and paleta_izquierda.bottom < ALTO:
            paleta_izquierda.y += velocidad_paleta

        if pelota.centery < paleta_derecha.centery and paleta_derecha.top > 0:
            paleta_derecha.y -= velocidad_paleta
        if pelota.centery > paleta_derecha.centery and paleta_derecha.bottom < ALTO:
            paleta_derecha.y += velocidad_paleta

    elif modo == "Maquina_vs_Maquina":
        if pelota.centery < paleta_izquierda.centery and paleta_izquierda.top > 0:
            paleta_izquierda.y -= velocidad_paleta
        if pelota.centery > paleta_izquierda.centery and paleta_izquierda.bottom < ALTO:
            paleta_izquierda.y += velocidad_paleta

        if pelota.centery < paleta_derecha.centery and paleta_derecha.top > 0:
            paleta_derecha.y -= velocidad_paleta
        if pelota.centery > paleta_derecha.centery and paleta_derecha.bottom < ALTO:
            paleta_derecha.y += velocidad_paleta

def mover_pelota():
    global velocidad_pelota_x, velocidad_pelota_y, puntuacion_izquierda, puntuacion_derecha
    
    pelota.x += velocidad_pelota_x
    pelota.y += velocidad_pelota_y

    if pelota.top <= 0 or pelota.bottom >= ALTO:
        velocidad_pelota_y *= -1
    
    if pelota.colliderect(paleta_izquierda) or pelota.colliderect(paleta_derecha):
        velocidad_pelota_x *= -1

    if pelota.left <= 0:
        puntuacion_derecha += 1
        reiniciar_pelota()

    if pelota.right >= ANCHO:
        puntuacion_izquierda += 1
        reiniciar_pelota()

def reiniciar_pelota():
    global velocidad_pelota_x, velocidad_pelota_y
    pelota.center = (ANCHO // 2, ALTO // 2)
    velocidad_pelota_x *= -1
    velocidad_pelota_y *= -1

def mostrar_game_over():
    pantalla.fill(NEGRO)
    texto_game_over = fuente.render("GAME OVER", True, BLANCO)
    pantalla.blit(texto_game_over, (ANCHO // 2 - texto_game_over.get_width() // 2, ALTO //2 + 50))

    boton_reiniciar = pygame.Rect(ANCHO // 2 - 100, ALTO // 2 + 50, 200, 50)
    pygame.draw.rect(pantalla, BLANCO, boton_reiniciar)
    texto_reiniciar = fuente.render("Reiniciar", True, NEGRO)
    pantalla.blit(texto_reiniciar, (ANCHO // 2 - texto_reiniciar.get_width() // 2, ALTO // 2 + 60))
    
    pygame.display.flip()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_reiniciar.collidepoint(evento.pos):
                    reiniciar_juego()

def reiniciar_juego():
    global puntuacion_izquierda, puntuacion_derecha, velocidad_pelota_x, velocidad_pelota_y
    puntuacion_izquierda = 0
    puntuacion_derecha = 0
    reiniciar_pelota()
    main_loop()

def mostrar_menu():
    pantalla.fill(NEGRO)
    fuente_menu = pygame.font.SysFont(None, 60)

    titulo = fuente_menu.render("PONG", True, BLANCO)

    botones = [
        {"rect": pygame.Rect(ANCHO // 2 - 150, 200, 300, 50), "texto": "Jugador vs Jugador"},
        {"rect": pygame.Rect(ANCHO // 2 - 150, 300, 300, 50), "texto": "Jugador vs Maquina"},
        {"rect": pygame.Rect(ANCHO // 2 - 150, 400, 300, 50), "texto": "Maquina vs Maquina"},
    ]

    while True:
        pantalla.fill(NEGRO)
        pantalla.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 100))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                for boton in botones:
                    if boton["rect"].collidepoint(evento.pos):
                        return boton["texto"].replace(" ", "_")
        
        mouse_pos = pygame.mouse.get_pos()

        for boton in botones:
            if boton["rect"].collidepoint(mouse_pos):
                sombra_rect = boton["rect"].inflate(10, 10)
                pygame.draw.rect(pantalla, (50, 50, 50), sombra_rect, border_radius=15)

        for boton in botones:
            if boton["rect"].collidepoint(mouse_pos):
                boton_rect = boton["rect"].inflate(10, 10)
                pygame.draw.rect(pantalla, BLANCO, boton_rect, border_radius=15)
            else:
                pygame.draw.rect(pantalla, BLANCO, boton["rect"], border_radius=15)

            texto = fuente.render(boton["texto"], True, NEGRO)
            texto_x = boton["rect"].x + (boton["rect"].width - texto.get_width()) // 2
            texto_y = boton["rect"].y + (boton["rect"].height - texto.get_height()) // 2
            pantalla.blit(texto, (texto_x, texto_y))
        pygame.display.flip()


def main_loop(modo):
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        mover_paletas(modo)
        mover_pelota()
        dibujar()

        pygame.display.flip()
        reloj.tick(60)

if __name__ == "__main__":
    modo = mostrar_menu()
    main_loop(modo)