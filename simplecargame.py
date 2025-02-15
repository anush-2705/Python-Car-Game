import pygame
from pygame.locals import *
import random

# shape parameters
size = width, height = (800, 800)
road_w = int(width/1.6)
roadmark_w = int(width/80)
# location parameters
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4
# animation parameters
speed = 1
score = 0

# initialize the app
pygame.init()
running = True

# set window size
screen = pygame.display.set_mode(size)
# set window title
pygame.display.set_caption("Simple Car Game")
# set background colour
screen.fill((60, 120, 0))
# apply changes
pygame.display.update()

# load player vehicle
car = pygame.image.load("car.png")
car_loc = car.get_rect()
car_loc.center = right_lane, height*0.8

# load enemy vehicle
car2 = pygame.image.load("otherCar.png")
car2_loc = car2.get_rect()
car2_loc.center = left_lane, height*0.2

# load tree image
tree = pygame.image.load("tress.png")
tree = pygame.transform.scale(tree, (100, 100))

counter = 0
font = pygame.font.Font(None, 36)

# game loop
while running:
    counter += 1
    score += 1

    # increase game difficulty over time
    if counter == 5000:
        speed += 0.15
        counter = 0
        print("level is up for you", speed)

    # animate enemy vehicle
    car2_loc[1] += speed
    if car2_loc[1] > height:
        # randomly select lane
        if random.randint(0,1) == 0:
            car2_loc.center = right_lane, -200
        else:
            car2_loc.center = left_lane, -200

    # end game logic
    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 250:
        print("GAME OVER! YOU LOST!")
        break

    # event listeners
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_w/2), 0])
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_w/2), 0])
    
    # draw road
    pygame.draw.rect(screen, (50, 50, 50), (width/2-road_w/2, 0, road_w, height))
    # draw centre line
    pygame.draw.rect(screen, (255, 240, 60), (width/2 - roadmark_w/2, 0, roadmark_w, height))
    # draw left road marking
    pygame.draw.rect(screen, (255, 255, 255), (width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height))
    # draw right road marking
    pygame.draw.rect(screen, (255, 255, 255), (width/2 + road_w/2 - roadmark_w*3, 0, roadmark_w, height))
    
    # draw trees on the side
    for i in range(0, height, 200):
        screen.blit(tree, (50, i))
        screen.blit(tree, (width - 150, i))
    
    # display score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    # place car images on the screen
    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)
    
    # apply changes
    pygame.display.update()

# collapse application window
pygame.quit()
