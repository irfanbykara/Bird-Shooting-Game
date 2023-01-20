import cv2
from cvzone.HandTrackingModule import HandDetector
import pygame
import sys
from bird_class import Bird
import consts
from game_logic import GameLogic

def main():

    running = True
    # Here we get the video stream from our webcam
    cap = cv2.VideoCapture(0)
    cap.set(3, 1288)
    cap.set(4, 728)
    detector = HandDetector(detectionCon=0.8)

    pygame.init()
    # apply it to text on a label
    score_text = consts.FONT.render("Score: 0", 1, consts.BLACK)

    # Set the width and height of the screen [width, height]
    screen = pygame.display.set_mode(consts.SIZE)
    pygame.display.set_caption(consts.GAME_NAME)

    # Let's declare our image files to be used in the game.

    bird = Bird(1)
    pygame.display.flip()
    game_logic = GameLogic(score_text, bird, screen)

    while running :

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        success, img = cap.read()
        img = cv2.flip(img, 1)
        hands, img = detector.findHands(img, flipType=False)
        game_logic.set_seconds()
        seconds = game_logic.get_seconds()  # calculate how many seconds
        screen.blit(consts.BG,(0,0))
        screen.blit(game_logic.get_score_text(), (550, 400))

        if seconds >= 10: # We have the time limit of 10 secs. This condition checks if the time is up.

            screen.blit(consts.GAME_OVER, (screen.get_width()/2-100, screen.get_height()/2-50))
            screen.blit(consts.RESTART_IMG, (screen.get_width()/2-100, screen.get_height()/2+50))
            time_left = consts.TIME_IS_UP
            screen.blit(time_left, (20, 20))
            game_logic.aim_handle(hands,detector,screen)
            pygame.display.flip()

        else: #Checking if the game is continuing.
            time_left = consts.FONT.render( "Time Left:" + str( 10 - seconds ), 1, consts.RED)
            screen.blit(time_left, (20, 20))
            bird.fly()
            screen.blit(consts.BIRD_IMG, (bird.posx, bird.posy))
            game_logic.aim_handle(hands,detector,screen)
            pygame.display.flip()

        cv2.imshow(consts.GAME_NAME,img) # How we detect hand and measure distance in the background
        cv2.waitKey(1)

if __name__ == "__main__":

    main()
    pygame.quit()