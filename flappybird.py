import pygame, random, sys
from pygame import event
from pygame.locals import *
fps = 32
screenwidth = 289
screenheight = 511
screen = pygame.display.set_mode((screenwidth, screenheight))
groundY = 0.8 * screenheight

game_sprites = {}
game_sound = {}
player = "gallery/gallery/sprites/bird.png"
background = "gallery/gallery/sprites/background.png"
obstacle = "gallery/gallery/sprites/pipe.png"

def welcomeScreen():
    playerX = int(screenwidth / 5)
    playerY = int((screenheight - game_sprites["player"].get_height()) / 2)
    messageX = int((screenwidth - game_sprites["message"].get_width()) / 2)
    messageY = int(screenheight * 0.13)
    baseX = 0

    while True:
        for event in pygame.event.get():

            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return

            else:
                screen.blit(game_sprites["background"], (0,0))
                screen.blit(game_sprites["player"], (playerX, playerY))
                screen.blit(game_sprites["base"], (baseX, groundY))
                screen.blit(game_sprites["message"], (messageX, messageY))
                pygame.display.update()
                FPSClock.tick(fps)
def mainGame():
    score = 0
    playerX = int(screenwidth / 5)
    playerY = int(screenwidth / 2)
    baseX = 0
    pipe1 = getrandompipe()
    pipe2 = getrandompipe()
    upperpipe = [
        {"x": screenwidth + 200, "y": pipe1[0]["y"]},
        {"x": screenwidth + 200 + (screenwidth / 2), "y": pipe2[0]["y"]}
    ]

    lowerpipe = [
        {"x": screenwidth + 200, "y": pipe1[1]["y"]},
        {"x": screenwidth + 200 + (screenwidth / 2), "y": pipe2[1]["y"]}
    ]

    playervelY = -9
    playermaxY = 10
    playerminY = -8
    playeraccY = 1
    playerflappedaccv = -8
    playerflap = False
    pipevelX = -4

    while True:
        for event in pygame.event.get():

            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN and (event.key == K_SPACE or K_UP):
                if playerY > 0:
                    playervelY = playerflappedaccv
                    playerflap = True
                    game_sound["wing"].play()

        crash = isCollide(playerX, playerY, upperpipe, lowerpipe)

        if crash:
            return

        playermidpos = playerX + game_sprites["player"].get_width() / 2

        for pipe in upperpipe:
            pipemidpos = pipe["x"] + game_sprites["pipe"][0].get_width() / 2
            if pipemidpos <= playermidpos < pipemidpos + 4:
                score += 1
                print(f"Your score is: {score}!!!")
                game_sound["point"].play()

        if playervelY < playermaxY and not playerflap:
            playervelY += playeraccY

        if playerflappedaccv:
            playerflap = False

        playerheight = game_sprites["bird"].get_height()
        playerY = playerY + min(playervelY, groundY - playerY - playerheight)

        for up, lp in zip(upperpipe, lowerpipe):
            up["x"] += pipevelX
            lp["x"] += pipevelX

        if 0 < upperpipe[0]["x"] < 5:
            newpipe = getrandompipe()
            upperpipe.append(newpipe[0])
            lowerpipe.append(newpipe[1])

        if upperpipe[0]["x"] < -game_sprites["pipe"][0].get_width():
            upperpipe.pop(0)
            lowerpipe.pop(0)

        screen.blit(game_sprites["background"], (0, 0))
        for up, lp in zip(upperpipe, lowerpipe):
            screen.blit(game_sprites["pipe"][0], (up['x'], up['y']))
            screen.blit(game_sprites["pipe"][1], (lp['x'], lp['y']))

        screen.blit(game_sprites["base"], (baseX, groundY))
        screen.blit(game_sprites["bird"], (playerX, playerY))
        digits = [int(x) for x in list(str(score))]
        width = 0

        for digit in digits:
            width += game_sprites["numbers"][digit].get_width()

        xoffset = (screenwidth - width) / 2

        for digit in digits:
            screen.blit(game_sprites["numbers"][digit], (xoffset, screenheight * 0.12))
            xoffset += game_sprites["numbers"][digit].get_width()

        pygame.display.update()
        FPSClock.tick(fps)

def isCollide(playerX, playerY, upperpipe, lowerpipe):
    if playerY > groundY - 25 or playerY < 0:
        game_sound["hit"].play()
        return True

    for pipe in upperpipe:
        pipeheight = game_sprites["pipe"][0].get_height()\

        if (playerY < pipeheight + pipe['y'] and abs(playerX - pipe['x']) < game_sprites["pipe"][0].get_width()):
            game_sound["hit"].play()
            return True

    for pipe in lowerpipe:
        if (playerY + game_sprites["bird"].get_height() > pipe['y']) and abs(playerX - pipe['x']) < \
               game_sprites["pipe"][0].get_width():
            game_sound["hit"].play()
            return True

    return False

def getrandompipe():
    pipeheight = game_sprites["pipe"][0].get_height()
    offset = screenheight / 3
    y2 = offset + random.randint(0, int(screenheight - game_sprites["base"].get_height() - 1.2 * offset))
    y1 = pipeheight - y2 + offset
    pipeX = screenwidth + 10
    pipe = [{'x': pipeX, 'y': -y1}, {'x': pipeX, 'y': y2}]
    return pipe

if __name__ == "__main__":
    pygame.init()
    FPSClock = pygame.time.Clock()
    pygame.display.set_caption("flappy bird clone")

    game_sprites["numbers"] = (
        pygame.image.load("gallery/gallery/sprites/0.png").convert_alpha(),
        pygame.image.load("gallery/gallery/sprites/1.png").convert_alpha(),
        pygame.image.load("gallery/gallery/sprites/2.png").convert_alpha(),
        pygame.image.load("gallery/gallery/sprites/3.png").convert_alpha(),
        pygame.image.load("gallery/gallery/sprites/4.png").convert_alpha(),
        pygame.image.load("gallery/gallery/sprites/5.png").convert_alpha(),
        pygame.image.load("gallery/gallery/sprites/6.png").convert_alpha(),
        pygame.image.load("gallery/gallery/sprites/7.png").convert_alpha(),
        pygame.image.load("gallery/gallery/sprites/8.png").convert_alpha(),
        pygame.image.load("gallery/gallery/sprites/9.png").convert_alpha(),
    )

    game_sprites["background"] = (
        pygame.image.load(background).convert_alpha()
    )

    game_sprites["base"] = (
        pygame.image.load("gallery/gallery/sprites/base.png").convert_alpha()
    )

    game_sprites["bird"] = (
        pygame.image.load("gallery/gallery/sprites/bird.png").convert_alpha()
    )

    game_sprites["message"] = (
        pygame.image.load("gallery/gallery/sprites/message.jpg").convert_alpha()
    )

    game_sprites["pipe"] = (
        pygame.transform.rotate(pygame.image.load(obstacle).convert_alpha(), 180),
        pygame.image.load(obstacle).convert_alpha()
    )

    game_sound["die"] = pygame.mixer.Sound("gallery/gallery/audio/die.wav")
    game_sound["hit"] = pygame.mixer.Sound("gallery/gallery/audio/hit.wav")
    game_sound["point"] = pygame.mixer.Sound("gallery/gallery/audio/point.wav")
    game_sound["swoosh"] = pygame.mixer.Sound("gallery/gallery/audio/swoosh.wav")
    game_sound["wing"] = pygame.mixer.Sound("gallery/gallery/audio/wing.wav")

    game_sprites["player"] =  pygame.image.load(player).convert_alpha()


    while True:
        welcomeScreen()
        mainGame()