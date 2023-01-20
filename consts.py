import cv2
import pygame
pygame.init()
pygame.mixer.init()


GUN_SOUND = pygame.mixer.Sound("resources/gunshot.wav")

BLACK = (0, 0, 0)
RED = (255, 0, 0)
SIZE = (700, 500)

GAME_NAME = "Bird Shooting CvZone"
BG = pygame.image.load("resources/bg.png")
RESTART_IMG = pygame.image.load("resources/restart.jpg")
RESTART_IMG = pygame.transform.scale(RESTART_IMG, (200, 100))

AIM = pygame.image.load("resources/aim2.png")
AIM = pygame.transform.scale(AIM, (25, 25))
BIRD_IMG = pygame.image.load("resources/flappy_bird.gif")
BIRD_IMG = pygame.transform.scale(BIRD_IMG, (50, 50))
FONT = pygame.font.SysFont("Comic Sans MS", 30)
GAME_OVER = FONT.render("Game Over!", 1, (255, 0, 0))
TIME_IS_UP = FONT.render("Time is up :(", 1, BLACK)
