import pygame
import random
 
# Inicializar pygame
pygame.init()
 
# Definir colores
NEGRO = (0, 0, 0)  
BLANCO = (255, 255, 255)
AZUL = (50, 153, 213)
VERDE = (0, 255, 0)
ROJO = (213, 50, 80)
 
# Tamaño de la pantalla
ANCHO = 600
ALTO = 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Flappy Bird con Pantalla Móvil')
 
# Parámetros del pájaro
pajaro_x = 50
pajaro_y = ALTO // 2
pajaro_radio = 10  # Radio más pequeño
pajaro_velocidad_y = 0
gravedad = 0.5
salto = -6  # Salto más corto
 
# Obstáculos
obstaculo_ancho = 40
obstaculo_espacio = 100
obstaculos = []
 
# Velocidad de desplazamiento de la pantalla
velocidad_pantalla = 3
 
# Función para generar nuevos obstáculos
def generar_obstaculos():
    altura_obstaculo = random.randint(100, 300)
    obstaculo = pygame.Rect(ANCHO, 0, obstaculo_ancho, altura_obstaculo)  # Parte superior
    obstaculo_inferior = pygame.Rect(ANCHO, altura_obstaculo + obstaculo_espacio, obstaculo_ancho, ALTO - altura_obstaculo - obstaculo_espacio)  # Parte inferior
    return obstaculo, obstaculo_inferior
 
# Función para dibujar el pájaro
def dibujar_pajaro():
    pygame.draw.circle(pantalla, ROJO, (pajaro_x, pajaro_y), pajaro_radio)
 
# Función para mover los obstáculos y la pantalla
def mover_obstaculos():
    global obstaculos
    for obstaculo, obstaculo_inferior in obstaculos:
        obstaculo.x -= velocidad_pantalla
        obstaculo_inferior.x -= velocidad_pantalla
 
    # Eliminar obstáculos fuera de la pantalla
    obstaculos = [ (obstaculo, obstaculo_inferior) for obstaculo, obstaculo_inferior in obstaculos if obstaculo.x > -obstaculo_ancho]
 
    # Generar nuevos obstáculos
    if len(obstaculos) == 0 or obstaculos[-1][0].x < ANCHO - 200:
        obstaculos.append(generar_obstaculos())
 
# Función para verificar las colisiones
def verificar_colisiones():
    global pajaro_y
    pajaro_rect = pygame.Rect(pajaro_x - pajaro_radio, pajaro_y - pajaro_radio, pajaro_radio * 2, pajaro_radio * 2)
 
    # Colisión con los bordes superior e inferior de la pantalla
    if pajaro_rect.top <= 0 or pajaro_rect.bottom >= ALTO:
        return True
 
    # Colisión con los obstáculos
    for obstaculo, obstaculo_inferior in obstaculos:
        if pajaro_rect.colliderect(obstaculo) or pajaro_rect.colliderect(obstaculo_inferior):
            return True
 
    return False
 
# Función principal del juego
def juego():
    global pajaro_y, pajaro_velocidad_y
    corriendo = True
    puntuacion = 0
    clock = pygame.time.Clock()
 
    while corriendo:
        pantalla.fill(AZUL)
 
        # Procesar eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:  # El pájaro salta
                    pajaro_velocidad_y = salto
 
        # Actualizar posición del pájaro
        pajaro_velocidad_y += gravedad
        pajaro_y += pajaro_velocidad_y
 
        # Mover obstáculos y la pantalla
        mover_obstaculos()
 
        # Verificar colisiones
        if verificar_colisiones():
            corriendo = False
 
        # Dibujar obstáculos
        for obstaculo, obstaculo_inferior in obstaculos:
            pygame.draw.rect(pantalla, VERDE, obstaculo)
            pygame.draw.rect(pantalla, VERDE, obstaculo_inferior)
 
        # Dibujar el pájaro
        dibujar_pajaro()
 
        # Mostrar puntuación
        puntuacion += 1
        fuente = pygame.font.SysFont('arial', 20)
        texto = fuente.render(f"Puntaje: {puntuacion}", True, BLANCO)
        pantalla.blit(texto, (10, 10))
 
        # Actualizar la pantalla
        pygame.display.update()
 
        # Controlar la velocidad del juego
        clock.tick(60)
 
    # Final del juego
    pygame.quit()
 
# Iniciar el juego
juego()
 