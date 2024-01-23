import pygame
import sys
import random

pygame.init()
clock = pygame.time.Clock()


def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time
    ball.x -= ball_speed_x
    ball.y -= ball_speed_y

    if ball.top <= 0 or ball.bottom >= game_height:
        ball_speed_y *= -1

    if ball.left <= 0:
        player_score += 1
        score_time = pygame.time.get_ticks()

    if ball.right >= game_width:
        opponent_score += 1
        score_time = pygame.time.get_ticks()

    # Determine the direction of the collision
    if ball.colliderect(player) or ball.colliderect(opponent):

        ball_speed_x *= -1


def playerAniamtion():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and player.top >= 0:
        player.top -= 7

    if keys[pygame.K_DOWN] and player.bottom <= game_height:
        player.top += 7


def opponentAI():
    if opponent.top < ball.y:
        opponent.top += 7
    if opponent.bottom > ball.y:
        opponent.bottom -= 7
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= game_height:
        opponent.bottom = game_height


def ball_restart():
    global ball_speed_x, ball_speed_y, score_time
    ball.center = (game_width/2-15, game_height/2-15)

    current_time = pygame.time.get_ticks()
    if current_time - score_time < 3000:
        ball_speed_x, ball_speed_y = 0, 0

    else:
        ball_speed_x = 7 * random.choice((1, -1))
        ball_speed_y = 7 * random.choice((1, -1))
        ball_speed_x += 3
        ball_speed_y += 3
        score_time = None


def opponentHuman():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and opponent.top >= 0:
        opponent.top -= 7

    if keys[pygame.K_s] and opponent.bottom <= game_height:
        opponent.top += 7


# setting up main window
game_width = 1000
game_height = 680
window = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption("Game")


# game rectangle
ball = pygame.Rect(game_width/2-15, game_height/2-15, 30, 30)
player = pygame.Rect(game_width-20, game_height/2-70, 10, 140)
opponent = pygame.Rect(10, game_height/2-70, 10, 140)
line = pygame.Rect(game_width/2-1, 0, 1, game_height)


bg_color = pygame.Color('grey12')
playerColor = pygame.Color("white")

ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))

# Text variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)
message_font = pygame.font.Font("freesansbold.ttf", 50)


# Timer variables
score_time = True
is_human = False
answer = False


def display_message(message, color, y_offset=0):
    text = message_font.render(message, True, color)
    text_rect = text.get_rect(
        center=(game_width // 2, game_height // 2 + y_offset))
    window.blit(text, text_rect)


padding = 50
while True:
    # handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                is_human = True
                answer = True
            elif event.key == pygame.K_2:
                is_human = False
                answer = True

    # visuals
    window.fill(bg_color)

    player_text = game_font.render(f"{player_score}", False, playerColor)
    opponent_text = game_font.render(f"{opponent_score}", False, playerColor)
    if not answer:
        display_message("Select Game Mode:", playerColor, -50-padding)
        display_message("1. Multiplayer", playerColor, -20)
        display_message("2. Play with AI", playerColor, 20+padding)
    else:
        window.blit(player_text, (game_width/2+5, game_height/2))
        window.blit(opponent_text, (game_width/2-25, game_height/2))
        pygame.draw.rect(window, playerColor, player)
        pygame.draw.rect(window, playerColor, opponent)
        pygame.draw.ellipse(window, playerColor, ball)
        pygame.draw.rect(window, playerColor, line)

        if is_human:
            playerAniamtion()
            ball_animation()
            opponentHuman()
        else:
            playerAniamtion()
            ball_animation()
            opponentAI()
        if score_time:
            ball_restart()

    # updating the window
    pygame.display.flip()
    clock.tick(60)
