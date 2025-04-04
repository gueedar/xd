import pygame
import sys
import random

pygame.init()

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)

ANCHO, ALTO = 600, 600
TAM_CELDA = ANCHO // 3

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Triki")

fuente = pygame.font.SysFont(None, 72)

tablero = [[" " for _ in range(3)] for _ in range(3)]
jugador_actual = "X"

def mostrar_menu():
    pantalla.fill(BLANCO)
    titulo = fuente.render("Triki", True, NEGRO)
    opcion_ia = fuente.render("1. Jugar contra la IA", True, AZUL)
    opcion_jugador = fuente.render("2. Jugar contra otro jugador", True, ROJO)

    pantalla.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 100))
    pantalla.blit(opcion_ia, (ANCHO // 2 - opcion_ia.get_width() // 2, 200))
    pantalla.blit(opcion_jugador, (ANCHO // 2 - opcion_jugador.get_width() // 2, 300))

    pygame.display.flip()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    return "IA"
                if evento.key == pygame.K_2:
                    return "Jugador"

def dibujar_tablero():
    pantalla.fill(BLANCO)
    for i in range(1, 3):
        pygame.draw.line(pantalla, NEGRO, (0, i * TAM_CELDA), (ANCHO, i * TAM_CELDA), 5)
    for i in range(1, 3):        
        pygame.draw.line(pantalla, NEGRO, (TAM_CELDA * i, 0), (TAM_CELDA * i, ALTO), 5)
    
    for fila in range(3):
        for col in range(3):
            if tablero[fila][col] == "X":
                texto = fuente.render("X", True, AZUL)
                pantalla.blit(texto, (col * TAM_CELDA + 50, fila * TAM_CELDA + 30))
            elif tablero[fila][col] == "O":
                texto = fuente.render("O", True, ROJO)
                pantalla.blit(texto, (col * TAM_CELDA + 50, fila * TAM_CELDA + 30)) 

def minimax(tablero, profundidad, es_maximizador):
    if verificar_ganador("O"):
        return 10 - profundidad
    if verificar_ganador("X"):
        return profundidad - 10
    if tablero_lleno():
        return 0
    
    if es_maximizador:
        mejor_puntaje = float('inf')
        for fila in range(3):
            for col in range(3):
                if tablero[fila][col] == " ":
                    tablero[fila][col] = "O"
                    puntaje = minimax(tablero, profundidad + 1, False)
                    tablero[fila][col] = " "
                    mejor_puntaje = max(mejor_puntaje, puntaje)
        return mejor_puntaje
    else:
        mejor_puntaje = float('inf')
        for fila in range(3):
            for col in range(3):
                if tablero[fila][col] == " ":
                    tablero[fila][col] = "X"
                    puntaje = minimax(tablero, profundidad + 1, True)
                    tablero[fila][col] = " "
                    mejor_puntaje = min(mejor_puntaje, puntaje)
        return mejor_puntaje
    
def ia_jugar():
    print("IA esta pensado...")
    mejor_puntaje = float("-inf")
    mejor_movimiento = None

    for fila in range(3):
        for col in range(3):
            if tablero[fila][col] == " ":
                tablero[fila][col] = "O"
                puntaje = minimax(tablero, 0, False)
                tablero[fila][col] = " "
                print(f"Evaluando movimiento({fila}, {col}): puntaje = {puntaje}")
                if puntaje > mejor_puntaje:
                    mejor_puntaje = puntaje
                    mejor_movimiento = (fila, col)

    print(f"Mejor movimiento: {mejor_movimiento}, puntaje: {mejor_puntaje}")
    return mejor_movimiento

def verificar_ganador (jugador):
    for fila in tablero:
        if all(celda == jugador for celda in fila):
            return True
        
    for col in range(3):
        if all(tablero[fila][col] == jugador for fila in range(3)):
            return True
        
    if all(tablero[i][i] == jugador for i in range(3)):
        return True
    if all(tablero[i][2 - i] == jugador for i in range(3)):

        return True
    
    return False

def tablero_lleno():
    return all(celda != " " for fila in tablero for celda in fila)

def mostrar_mensaje(texto):
    pantalla.fill(BLANCO)
    mensaje = fuente.render(texto, True, NEGRO)
    rect = mensaje.get_rect(center=(ANCHO // 2, ALTO // 2))
    pantalla.blit(mensaje, rect)
    pygame.display.flip()
    pygame.time.wait(3000)

def jugar_triki(modo):
    global jugador_actual
    corriendo = True

    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if jugador_actual == "X" and evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                fila = y // TAM_CELDA
                col = x // TAM_CELDA

                if tablero[fila][col] == " ":
                    tablero[fila][col] = jugador_actual

                    if verificar_ganador(jugador_actual):
                        dibujar_tablero()
                        pygame.display.flip()
                        mostrar_mensaje(f"¡{jugador_actual} ha ganado!")
                        corriendo = False
                        break

                    if tablero_lleno():
                        dibujar_tablero()
                        pygame.display.flip()
                        mostrar_mensaje("¡es un empate!")
                        corriendo = False
                        break
                    if modo == "Jugador":
                        jugador_actual = "O" if jugador_actual == "X" else "X"


        if modo == "IA" and jugador_actual == "O" and corriendo:
            pygame.time.wait(500)
            movimiento = ia_jugar()
            if movimiento:
                fila, col = movimiento
                tablero[fila][col] = jugador_actual

                if verificar_ganador (jugador_actual):
                    dibujar_tablero()
                    pygame.display.flip()
                    mostrar_mensaje(f"¡{jugador_actual} ha ganado!")
                    corriendo = False
                    break

                if tablero_lleno():
                    dibujar_tablero()
                    pygame.display.flip()
                    mostrar_mensaje("¡Es un empate!")
                    corriendo = False
                    break
                jugador_actual = "X" 

        dibujar_tablero()
        pygame.display.flip()

if __name__ == "__main__":
    modo_juego = mostrar_menu()
    jugar_triki(modo_juego)

