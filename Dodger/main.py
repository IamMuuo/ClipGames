import pygame, random, sys
from pygame.locals import *

WINHEIGHT = 600
WINWIDTH = 600
TEXTCOLOR = (0,0,0) # black
BACKGROUNDCOLOR = (255,255, 255) # white
FPS = 60

BADDIEMINSIZE = 10
BADDIEMAXSIZE = 40
BADDIEMINSPEED = 1
BADDIEMAXSPEED = 8
ADDNEWBADDIERATE = 6
PLAYERMOVERATE = 5

def terminate():
    '''Exit the game'''
    pygame.quit()
    sys.exit()


def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate() #exit the game
            if event.type == KEYDOWN:
                if event.type == K_ESCAPE:
                    terminate()# exit the game
                return

def playerHasHitBaddie(playerRect, baddies):
    #check if the player has collided with a baddie
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            return True

    return False

def drawText(text, font, surface, x, y):
    '''Draws some given text to the screen'''
    textobj = font.render(text,1,TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# setup  pygame, the window and mouse cursor
pygame.init()

mainClock = pygame.time.Clock()

window_surface = pygame.display.set_mode((WINHEIGHT,WINWIDTH))
pygame.display.set_caption('Dodger!')
pygame.mouse.set_visible(False)


# setup the fonts
font = pygame.font.SysFont(None, 48)


# setup sounds
gameOverSound = pygame.mixer.Sound('Assets/gameover.wav')
pygame.mixer.music.load('Assets/background.wav')

pygame.mixer.music.play()


# setup textures
playerTexture = pygame.image.load('Assets/player.png')
playerRect = playerTexture.get_rect()
playerTexture = pygame.transform.scale(playerTexture, (20,20))
baddieTexture = pygame.image.load('Assets/baddie.png')


# show the start screen

window_surface.fill(BACKGROUNDCOLOR)

drawText('Dodger', font, window_surface, WINWIDTH/3, WINHEIGHT/3)
drawText('Press any key to start', font, window_surface, (WINHEIGHT/30) - 30, (WINWIDTH/30) - 50)

pygame.display.update()
waitForPlayerToPressKey()


topscore = 0


while True:
    # set up start of the game
    baddies = []

    score = 0
    playerRect.topleft = (WINHEIGHT / 2, WINWIDTH - 50)
    moveLeft = moveRight = moveUp = moveDown = False

    reverseCheat = slowCheat = False

    baddieAddCounter = 0

    pygame.mixer.music.play(-1,0,0)

    while True:
        score += 1  # increase score


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate() # exit the game

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()

                if event.key == pygame.K_z:
                    reverseCheat = True

                if event.key == pygame.K_x:
                    slowCheat = True

                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    moveRight = False
                    moveLeft = True

                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    moveRight = True
                    moveLeft = False

                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    moveUp = True
                    moveDown = False


                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    moveUp = False
                    moveDown = True



            # key up movements

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    terminate()
                    
                if event.key == pygame.K_z:
                    reverseCheat = False

                if event.key == pygame.K_x:
                    slowCheat = False

                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    moveLeft = False

                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    moveRight = False

                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    moveUp = False
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    moveDown = False

            if event.type == MOUSEMOTION:
                playerRect.centerx = event.pos[0]
                playerRect.centery = event.pos[1]


            # add new baddies at the top of screen if needed

        if not reverseCheat and not slowCheat:
            baddieAddCounter += 1

        if baddieAddCounter == ADDNEWBADDIERATE:
            baddieAddCounter = 0

            baddieSize = random.randint(BADDIEMINSIZE, BADDIEMAXSIZE)

            newBaddie = {'rect':pygame.Rect(random.randint(0, WINHEIGHT - baddieSize), 0 - baddieSize,baddieSize , baddieSize),
                'speed':random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                'surface':pygame.transform.scale(baddieTexture, (baddieSize, baddieSize))}

            baddies.append(newBaddie)


                # move the player around
            if moveLeft and playerRect.left > 0:
                playerRect.move_ip(-1*PLAYERMOVERATE,0 )

            if moveRight and playerRect.right < WINWIDTH:
                playerRect.move_ip(PLAYERMOVERATE, 0)

            if moveUp and playerRect.top > 0:
                playerRect.move_ip(0, -1 * PLAYERMOVERATE)

            if moveDown and playerRect.top < WINHEIGHT:
                playerRect.move_ip(0, PLAYERMOVERATE)


            # move all the baddies doen

        for b in baddies:
            if not reverseCheat and not slowCheat:
                b['rect'].move_ip(0, b['speed'])

            elif reverseCheat:
                b['rect'].move_ip(0, -5)

            elif slowCheat:
                b['rect'].move_ip(0, 1)

            # delete baddies that have fallen beyond the screen
        for b in baddies:
            if b['rect'].top > WINHEIGHT:
                baddies.remove(b)


            # draw the game world on a window
        window_surface.fill(BACKGROUNDCOLOR)


            # Draw the HUD
        drawText('Score %s'%(score), font, window_surface, 10, 0)
        drawText('Topscore %s' %(score), font, window_surface, 10, 40)

        # Draw player rect
        window_surface.blit(playerTexture, playerRect)

        # draw each baddie
        for b in baddies:
            window_surface.blit(b['surface'], b['rect'])

        pygame.display.update()


        # check if any of the baddies has hit the player

        if playerHasHitBaddie(playerRect, baddies):
            if score > topscore:
                topscore = score
            break

        mainClock.tick(FPS)

pygame.mixer.music.stop()
gameOverSound.play()


waitForPlayerToPressKey()



