import cv2
import cvzone
import time
from cvzone.HandTrackingModule import HandDetector
import mediapipe
import random
import pygame
import time
import sys
import BirdClass


global well_shot
global start_ticks
global isFirstPos
global timer
global score_text
running = True

# Here we get the video stream from our webcam
cap = cv2.VideoCapture(0)
cap.set(3,1288)
cap.set(4,728)
detector = HandDetector( detectionCon=0.8 )


well_shot=0
random_pos_x=random.randint( 100, 1000 )
random_pos_y=random.randint( 100, 400 )
isFirstPos = True

# Color consts
BLACK = (0, 0, 0)
RED = (255, 0, 0)


pygame.init()
myfont = pygame.font.SysFont("Comic Sans MS", 30)
# apply it to text on a label
score_text = myfont.render( "Score:" + str( well_shot ), 1, BLACK )

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode( size )
pygame.display.set_caption( "Bird Shooting CvZone" )

# Let's declare our image files to be used in the game.
bg = pygame.image.load("resources/bg.png")
aim = pygame.image.load("resources/aim2.png")
aim = pygame.transform.scale(aim, (25, 25))
birdImg = pygame.image.load("resources/birdImgTrans.jfif")
birdImg = pygame.transform.scale(birdImg, (50, 50))

bird_pos_x_init = random.randint( 10, 600 )
bird_pos_y_inti = random.randint( 20, 100 )
bird = BirdClass.Bird( bird_pos_x_init, bird_pos_y_inti, 1 )
pygame.display.flip()
start_ticks=pygame.time.get_ticks() #starter tick


def aim_handle(hands, detector):
    if hands:
        lmList = hands[0]['lmList']
        cursor = lmList[8]

        screen.blit( aim, (cursor[0] - 10, cursor[1] - 10) )

        # pygame.display.flip()
        length, info, = detector.findDistance( lmList[8], lmList[12], )

        if length < 60:
            pygame.draw.circle( screen, RED, (cursor[0], cursor[1]), 10 )

            check_shot( cursor, )

def check_shot(cursor, ):
    global score_text
    global start_ticks
    global well_shot
    global isFirstPos
    dist = ((bird.posx - cursor[0])**2 + (bird.posy - cursor[1])**2)**0.5 # Distance between our shot and the bird.

    restart_pos_x = screen.get_width()/2-235
    restart_pos_y =  screen.get_height()/2+50
    dist_to_restart = ((restart_pos_x - cursor[0])**2 + (restart_pos_y - cursor[1])**2)**0.5 # Distance between the restart button and the our shot

    if seconds>=10: # If the time is up.
        if dist_to_restart<=100:
            start_ticks = pygame.time.get_ticks()  # starter tick
            well_shot = 0
            pygame.display.flip()

    if dist<50:
        well_shot = well_shot +1
        score_text = myfont.render( "Score:" + str( well_shot ), 1, BLACK )
        isFirstPos = True

while running :

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    success, img = cap.read()
    img = cv2.flip( img, 1 )

    hands, img = detector.findHands( img, flipType=False )
    global seconds
    seconds = int( (pygame.time.get_ticks() - start_ticks) / 1000 )  # calculate how many seconds
    screen.blit(bg,(0,0))
    screen.blit( score_text, (550, 400) )
    if seconds>=10: # We have the time limit of 10 secs. This condition cheks if the time is up.

        game_over = myfont.render( "Game Over!", 1, (255,0,0) )
        restart = myfont.render( "Click Here To Restart The Game!", 1, (0,0,0) )

        screen.blit( game_over, (screen.get_width()/2-100, screen.get_height()/2-50) )
        screen.blit( restart, (screen.get_width()/2-235, screen.get_height()/2+50))

        time_left = myfont.render( "Süre Bitti :(", 1, BLACK )

        screen.blit( time_left, (20, 20) )
        aim_handle(hands,detector)

        pygame.display.flip()
    else: #Checking if the game is continuing.
        time_left = myfont.render( "Kalan Süre:" + str( 10 - seconds ), 1, BLACK )
        screen.blit( time_left, (20, 20) )

        if isFirstPos:
            bird.posx = random.randint(25,600)
            bird.posy = random.randint(20,350)
            screen.blit( birdImg, (bird_pos_x_init, bird_pos_y_inti) )
            isFirstPos = False

        bird.fly()
        screen.blit( birdImg, (bird.posx, bird.posy) )
        aim_handle(hands,detector)
        pygame.display.flip()

    cv2.imshow('Problem Shooting',img) # How we detect hand and measure distance in the background
    cv2.waitKey(1)
pygame.quit()