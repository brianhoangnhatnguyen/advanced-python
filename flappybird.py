import pygame, random, sys
from pygame.locals import *
fps = 32
screenwidth = 289
screenheight = 511
screen = pygame.display.set_mode((screenwidth, screenheight))
groundY = 0.8 * screenheight

game_sprites = {}
game_sound = {}
player = "gallery/sprites/bird.png"
background = "gallery/sprites/background.png"
obstacle = "gallery/sprites/pipe.png"

def welcomeScreen():
    playerX = int(screenwidth / 5)
    playerY = int((screenheight - game_sprites["player"].get_height()) / 2)
    messageX = int(screenwidth / 2)

if __name__ == "__main__":
    pygame.init()
    fpsClock = pygame.time.Clock
    pygame.display.set_caption("flappy bird clone")

    game_sprites["numbers"] = (
        pygame.image.load("gallery/0.png").convert_alpha(),
        pygame.image.load("gallery/1.png").convert_alpha(),
        pygame.image.load("gallery/2.png").convert_alpha(),
        pygame.image.load("gallery/3.png").convert_alpha(),
        pygame.image.load("gallery/4.png").convert_alpha(),
        pygame.image.load("gallery/5.png").convert_alpha(),
        pygame.image.load("gallery/6.png").convert_alpha(),
        pygame.image.load("gallery/7.png").convert_alpha(),
        pygame.image.load("gallery/8.png").convert_alpha(),
        pygame.image.load("gallery/9.png").convert_alpha()
    )

    game_sprites["background"] = (
        pygame.image.load(background).convert_alpha()
    )

    game_sprites["base"] = (
        pygame.image.load("gallery/base.png").convert_alpha()
    )

    game_sprites["bird"] = (
        pygame.image.load("gallery/bird.png").convert_alpha()
    )

    game_sprites["message"] = (
        pygame.image.load("gallery/message.png").convert_alpha()
    )

    game_sprites["pipe"] = (
        pygame.transform.rotate(obstacle).convert_alpha(), 180,
        pygame.image.load(obstacle).convert_alpha()
    )

    game_sound["die"] = pygame.mixer.Sound("gallery/audio/die.wav")
    game_sound["hit"] = pygame.mixer.Sound("gallery/audio/hit.wav")
    game_sound["point"] = pygame.mixer.Sound("gallery/audio/point.wav")
    game_sound["swoosh"] = pygame.mixer.Sound("gallery/audio/swoosh.wav")
    game_sound["wing"] = pygame.mixer.Sound("gallery/audio/wing.wav")

    game_sprites["player"] = (
        pygame.image.load(player).convert_alpha()
    )

    while True:
        welcomeScreen()
