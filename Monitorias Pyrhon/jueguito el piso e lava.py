import pygame
import random
import time

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
colors = [red, green, blue]

screen_wwidth = 600
screen_height = 400

screen = pygame.display.set_mode((screen_wwidth, screen_height))
pygame.display.set_caption("colors game")

clock = pygame.time.Clock()

player_width = 50
player_height = 50
player_x = screen_wwidth // 2 - player_width // 2
player_y = screen_height - player_height - 10

player_speed = 5

font = pygame.font.SysFont(None, 36)

def draw_player(x, y):
    pygame.draw.rect(screen, white, (x, y, player_width, player_height))

def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def game_loop():
    running = True
    score = 0
    suggested_color = random.choice(colors)
    ground_color = random.choice(colors)

    global player_x, player_y

    while running:
        screen.fill(black)
        pygame.draw.rect(screen, ground_color, (0, screen_height - 50, screen_wwidth, 50))
        draw_text(f"Color sugerido: {suggested_color}", white, 20, 20)
        draw_text(f"Puntaje: {score}", black, screen_wwidth - 150, 20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < screen_wwidth - player_width:
            player_x += player_speed

        if ground_color == suggested_color and player_y + player_height >= screen_height - 10:
            score += 1
            suggested_color = random.choice(colors)
            ground_color = random.choice(colors)
        elif ground_color != suggested_color:
            draw_text("Game over!", red, screen_wwidth // 2 - 80, screen_height // 2)
            pygame.display.update()
            time.sleep(2)

            waiting_for_key = True
            while waiting_for_key:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        waiting_for_key = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            game_loop()
                            waiting_for_key = False
                        elif event.key == pygame.K_ESCAPE:
                            running = False
                            waiting_for_key = False
            break

        draw_player(player_x, player_y)

        pygame.display.update()
        clock.tick(60)
    
game_loop()
pygame.quit()
