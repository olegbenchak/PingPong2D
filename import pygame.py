import pygame
import time
import random
from pathlib import Path

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
dis_x=1000
dis_y=500
font = pygame.font.Font(None, 50)
p_width = 15
p_height = 100
p_speed = 15
dis = pygame.display.set_mode((dis_x, dis_y))
ball_R=10
ball_speed=6
ball_D=ball_R*2

point_l=0
point_r=0
ball_start_x = dis_x/2 -ball_R
ball_start_y = dis_y/2 -ball_R 

dx= 1
dy= -1




fps = 80
screen = pygame.display.set_mode((dis_x, dis_y))
platform_r = pygame.Rect(dis_x - p_width - 5, dis_y/2 - p_height/2, p_width, p_height )
platform_l = pygame.Rect(5,dis_y/2 - p_height/2, p_width, p_height )
ball = pygame.Rect(ball_start_x,ball_start_y,ball_D,ball_D) 
font_style = pygame.font.SysFont("bahnschrift", 25)

clock = pygame.time.Clock()
pygame.display.set_caption("Ping-Pong 2-D Game")
game = False
pong_sound = pygame.mixer.Sound(
    str(Path.cwd() / "pygame" / "sounds" / "sound.mp3")
)
def message1(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [400, 150])
def message2(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [400, 250])


menu=True
while menu:
    screen.fill(green)
    message1("Press S to start", red)
    message2("Press R to restart", red)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    key = pygame.key.get_pressed()
    if (key[pygame.K_s] and platform_r.top >0):

        game=True
        menu=False


pause = False
while game:
    screen.fill(green)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    key = pygame.key.get_pressed()
    if (key[pygame.K_UP] and platform_r.top >0):
        platform_r.top -= p_speed
    elif (key[pygame.K_DOWN] and platform_r.bottom < dis_y):
        platform_r.bottom += p_speed
    elif (key[pygame.K_w] and platform_l.top > 0):
        platform_l.top -= p_speed
    elif (key[pygame.K_s] and platform_l.bottom < dis_y):
        platform_l.bottom += p_speed
    elif (key[pygame.K_r]):
       point_l = 0
       point_r = 0

    pygame.draw.rect(screen, pygame.Color("white"), platform_r)
    pygame.draw.rect(screen, pygame.Color("white"), platform_l)
  
    pygame.draw.circle(screen, pygame.Color("White"), ball.center, ball_R)
    ball.x += ball_speed * dx
    ball.y += ball_speed * dy


    if ball.centery < ball_R or ball.centery > dis_y - ball_R:
        dy = -dy
        pygame.mixer.Sound.play(pong_sound)
    elif ball.colliderect(platform_l) or ball.colliderect(platform_r):
        dx = -dx
        pygame.mixer.Sound.play(pong_sound)
    if ball.centerx > dis_x:
        point_r += 1
        ball.x = ball_start_x
        ball.y = ball_start_y
        dx = 0
        dy = 0
        goal_time = pygame.time.get_ticks()
        pause = True
    elif ball.centerx < 0:
        point_l += 1
        ball.x = ball_start_x
        ball.y = ball_start_y
        dx = 0
        dy = 0
        goal_time = pygame.time.get_ticks()
        pause = True
    if pause:
        #milliseconds
        current_time = pygame.time.get_ticks()
        if current_time - goal_time > 30000:
            dx = random.choice((1, -1))
            dy = random.choice((1, -1))
            pause = False
        elif (key[pygame.K_p]):
            dx = random.choice((1, -1))
            dy = random.choice((1, -1))
            pause = False
        
    right_text = font.render(f"{point_l}", True, pygame.Color("White"))
    screen.blit(right_text, (dis_x - 40, 20))

    left_text = font.render(f"{point_r}", True, pygame.Color("White"))
    screen.blit(left_text, (20, 20))


    pygame.display.flip()
    clock.tick(fps)
pygame.quit()