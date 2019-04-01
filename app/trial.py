import pygame
import random

#intializing pygame

pygame.init()

#game-window config

window_height = 624
window_width = 287
window = pygame.display.set_mode([window_width, window_height])
bg = pygame.image.load("background.png")

#intializing different variables

Clock = pygame.time.Clock()
high_score = 0
pipe_x = window_width
base1 = pygame.image.load("base.png")
base2 = pygame.image.load("base.png")
redbird_mid = pygame.image.load("redbird-midflap.png")
#redbird_down = pygame.image.load("redbird-downflap.png")
play_button = pygame.image.load("play.png")
play_button = pygame.transform.scale(play_button, (80, 100))
quit_button = pygame.image.load("quit.png")
quit_button = pygame.transform.scale(quit_button, (80, 100))
img_width = 32
#definitions of colours

light_green = (0, 255, 0)
red = (255, 0, 0)
green = (0, 102, 0)
blue = (0, 0, 255)
black = (255, 255, 255)
orange = (239, 118, 19)
#functions
def crash(x, count, high_score):
    while x == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 45 < mouse[0] < 125 and 400 < mouse[1] < 500:
            if click[0] == 1:
                game_loop()
                x = 2
        if 150 < mouse[0] < 230 and 400 < mouse[1] < 500:
            if click[0] == 1:
                pygame.quit()
                quit()
        window.blit(bg, (0, 0))
        font_game_over = pygame.font.SysFont("gunplay", 40, False, False)
        print_game_over = font_game_over.render("GAME OVER", True, orange)
        window.blit(print_game_over, (50, 80))
        window.blit(play_button, (45, 400))
        window.blit(quit_button, (150, 400))
        font_score = pygame.font.SysFont("fixedsys", 30, False, False)
        print_current_score = font_score.render("YOUR SCORE: ", True, black)
        window.blit(print_current_score, (50, 175))
        print_current_score_1 = font_score.render(str(count), True, black)
        window.blit(print_current_score_1, (192, 175))
        print_current_score_2 = font_score.render("HIGH SCORE: ", True, black)
        window.blit(print_current_score_2, (50, 215))
        print_current_score_3 = font_score.render(str(high_score), True, black)
        window.blit(print_current_score_3, (190, 215))
        pygame.display.update()
        Clock.tick()
def display_count(count):
    font = pygame.font.SysFont("Impact", 25, True, False)
    score = font.render(str(count), True, green)
    window.blit(score, (143, 100))
#basic game-loop

def game_loop():
    global high_score,pipe_x
    x = 2
    #pipe_x = window_width
    base_x1 = 0
    base_x2 = window_width
    bird_x = 57
    bird_y = 225
    bird_g = 3
    pipe_uh = random.randrange(0, int(0.65 * 512))
    pipe_lh = pipe_uh + 90 + 38
    lower_pipe_upper = pygame.image.load("lower_pipe_upper.jpeg")
    lower_pipe_lower = pygame.image.load("lower_pipe_lower.jpeg")
    upper_pipe_upper = pygame.image.load("upper_pipe_upper.jpeg")
    upper_pipe_lower = pygame.image.load("upper_pipe_lower.jpeg")
    upper_pipe_upper = pygame.transform.scale(upper_pipe_upper, (52, pipe_uh))
    lower_pipe_lower = pygame.transform.scale(lower_pipe_lower, (52, 512 - pipe_lh - 38))
    count = 0
    #high_score = 0
#basic never-ending loop
    while x == 2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_g = 4.5
#bird collision mechanism

        if bird_y < pipe_uh + 38:
            if bird_x + img_width == pipe_x or bird_x > pipe_x and bird_x < pipe_x + 52:
                crash(1, count, high_score)
        if bird_y + 24 > pipe_uh + 90 + 38:
            if bird_x + img_width == pipe_x or bird_x > pipe_x and bird_x < pipe_x + 52:
                crash(1, count, high_score)

        if bird_y + 24 > 512 or bird_y < 0:
            crash(1, count, high_score)
        if bird_x == pipe_x:
            count += 1
#for drawing grass continously

        if base_x2 == 0:
            base_x1 = 286
        if base_x1 == 0:
            base_x2 = 286

#for making backgound a custom png
        window.blit(bg, (0, 0))

#for moving the grass

        window.blit(base1, (base_x1, 512))
        base_x1 -= 2
        window.blit(base2, (base_x2, 512))
        base_x2 -= 2

#pipes drawing and moving them

        window.blit(upper_pipe_upper, (pipe_x, 0))
        window.blit(upper_pipe_lower, (pipe_x, pipe_uh))
        window.blit(lower_pipe_upper, (pipe_x, pipe_lh))
        window.blit(lower_pipe_lower, (pipe_x, pipe_lh + 38))
        pipe_x -= 2
        if pipe_x + 53 < 0:
            pipe_x = window_width
            pipe_uh = random.randrange(0, int(0.65 * 512))
            pipe_lh = pipe_uh + 90 + 38
            upper_pipe_upper = pygame.transform.scale(upper_pipe_upper, (52, pipe_uh))
            lower_pipe_lower = pygame.transform.scale(lower_pipe_lower, (52, 512 - pipe_lh - 38))

#drawing bird and moving it in x-direction
        bird_g -= 0.32
        bird_y -= bird_g
        #window.blit(redbird_down, (bird_x, bird_y))
        window.blit(redbird_mid, (bird_x, bird_y))

#
        if count > high_score:
            high_score = count

#this is usd to refresh the display
        display_count(count)
        pygame.display.update()
        Clock.tick(60)

#function calls and quitting the application
game_loop()
pygame.quit()
quit()