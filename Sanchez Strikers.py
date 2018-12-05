#Dustin Smith n Zackey Hogg
#A terrible game, made great by its soundtrack
#Welcome, to Sanchez Strikers

#IMPORTANT:make sure to put in this command: py -m pip install -U pygame

#import and start up all the systems
import pygame, sys, time, random, os
from pygame.locals import *
pygame.init()
pygame.font.init()
pygame.mixer.init()

# set up the window and fps
displayX = 800
displayY = 800
fps = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((displayX, displayY))
pygame.display.set_caption('Sanchez Strikers')

#title screen
def game_intro(displayX, displayY):
    intro = True
    sanchez = pygame.image.load('sanchez.png')
    sanchez = pygame.transform.scale(sanchez, (200,300))
    font1 = pygame.font.SysFont('Comic Sans MS', 90)
    font2 = pygame.font.SysFont('Comic Sans MS', 50)
    line1 = font1.render('Sanchez Strikers', False, (255, 255, 255))
    line2 = font2.render('Mouse to shoot and move', False, (255, 255, 255))
    line3 = font2.render('Press enter to play', False, (255, 255, 255))
    jukebox('all.mp3', 0.0)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                intro = False
                os._exit(1)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    intro = False
        gameDisplay.blit(background, (0,0))
        gameDisplay.blit(sanchez, (displayX/2-75, displayY/2-300))
        gameDisplay.blit(line1,(25,500))
        gameDisplay.blit(line2,(100,600))
        gameDisplay.blit(line3,(150,650))
        pygame.display.update()
        fps.tick(15)
#jukebox function
def jukebox(song, start):
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(-1, start)
#enemy creator
def enemyMaker(enemyType, X, Y):
    if enemyType == 1:
        enemy1List.append(1)
        enemy1X.append(X)
        enemy1Y.append(Y)
    elif enemyType == 2:
        enemy2List.append(2)
        enemy2X.append(X)
        enemy2Y.append(Y)
    elif enemyType == 3:
        enemy3List.append(4)
        enemy3X.append(X)
        enemy3Y.append(Y)
#create level 1
def level1():
    global is_running
    global level1_done
    jukebox('sax.mp3', 0.0)
    enemyMaker(1,100,000)
    enemyMaker(1,150,000)
    enemyMaker(1,200,000)
    enemyMaker(1,250,000)
    enemyMaker(1,300,000)
    enemyMaker(1,350,000)
    enemyMaker(1,400,000)
    enemyMaker(1,450,000)
    enemyMaker(1,500,000)
    enemyMaker(1,550,000)
    enemyMaker(1,600,000)
    enemyMaker(1,650,000)
    enemyMaker(1,700,000)
    enemyMaker(1,100,100)
    enemyMaker(1,150,100)
    enemyMaker(1,200,100)
    enemyMaker(1,250,100)
    enemyMaker(1,300,100)
    enemyMaker(1,350,100)
    enemyMaker(1,400,100)
    enemyMaker(1,450,100)
    enemyMaker(1,500,100)
    enemyMaker(1,550,100)
    enemyMaker(1,600,100)
    enemyMaker(1,650,100)
    enemyMaker(1,700,100)
    is_running = True
    level1_done = True
#create level 2
def level2():
    global is_running
    global level2_done
    jukebox('stars.mp3', 24.0 )
    enemyMaker(1,100,000)
    enemyMaker(2,150,000)
    enemyMaker(1,200,000)
    enemyMaker(2,250,000)
    enemyMaker(1,300,000)
    enemyMaker(2,350,000)
    enemyMaker(1,400,000)
    enemyMaker(2,450,000)
    enemyMaker(1,500,000)
    enemyMaker(2,550,000)
    enemyMaker(1,600,000)
    enemyMaker(2,650,000)
    enemyMaker(1,100,100)
    enemyMaker(2,150,100)
    enemyMaker(1,200,100)
    enemyMaker(2,250,100)
    enemyMaker(1,300,100)
    enemyMaker(2,350,100)
    enemyMaker(1,400,100)
    enemyMaker(2,450,100)
    enemyMaker(1,500,100)
    enemyMaker(2,550,100)
    enemyMaker(1,600,100)
    enemyMaker(2,650,100)
    is_running = True
    level2_done = True
#create level 3
def level3():
    global is_running
    global level3_done
    jukebox('fire.mp3',12.0)
    enemyMaker(1,100,000)
    enemyMaker(2,200,000)
    enemyMaker(3,300,000)
    enemyMaker(2,400,000)
    enemyMaker(3,500,000)
    enemyMaker(2,600,000)
    enemyMaker(1,700,000)
    enemyMaker(1,100,100)
    enemyMaker(2,200,100)
    enemyMaker(3,300,100)
    enemyMaker(2,400,100)
    enemyMaker(3,500,100)
    enemyMaker(2,600,100)
    enemyMaker(1,700,100)
    is_running = True
    level3_done = True
#create level 4
def level4():
    global is_running
    global level4_done
    jukebox('run.mp3', 20.0)
    enemyMaker(2,100,000)
    enemyMaker(3,200,000)
    enemyMaker(2,300,000)
    enemyMaker(3,400,000)
    enemyMaker(2,500,000)
    enemyMaker(3,600,000)
    enemyMaker(2,700,000)
    enemyMaker(2,100,100)
    enemyMaker(3,200,100)
    enemyMaker(2,300,100)
    enemyMaker(3,400,100)
    enemyMaker(2,500,100)
    enemyMaker(3,600,100)
    enemyMaker(2,700,100)
    is_running = True
    level4_done = True
#boss level
def bossLevel():
    global is_running
    global bossDone
    global bossHealth
    jukebox('zinogre.mp3', 0.0)
    bossHealth = 50
    bossDone = True
    is_running = True
#checks if game is running
def runchecker():
    if len(enemy1List) == 0 and len(enemy2List) == 0 and len(enemy3List) == 0 and bossHealth == 0:
        return False
    else:
        return True
#level complete message
def levelComplete(is_running,jukeon, jukeon2):
    font1 = pygame.font.SysFont('Comic Sans MS', 90)
    font2 = pygame.font.SysFont('Comic Sans MS', 50)
    line2 = font2.render('Press enter to continue', False, (255, 255, 255))
    waitscreen = True
    if is_running == False and end == False:
        while waitscreen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    waitscreen = False
                    os._exit(1)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waitscreen = False
            if bossDone == True:
                pygame.display.update()
                pygame.time.wait(100)
                cutscene()
            elif level4_done == True:
                if jukeon == False:
                    jukebox('warning.mp3', 0.0)
                    jukeon = True
                font3 = pygame.font.SysFont('Impact', 90)
                font4 = pygame.font.SysFont('Impact', 50)
                line1 = font3.render('WARNING!', False, (255, 0, 0))
                line2 = font4.render('BOSS FIGHT!', False, (255, 0, 0))
                line3 = font4.render('ENTER TO CONTINUE', False, (255, 0, 0))
                gameDisplay.blit(line1, (225,300))
                gameDisplay.blit(line2, (275,400))
                gameDisplay.blit(line3, (210,450))
            elif level3_done == True:
                line1 = font1.render('You beat level 3!', False, (255, 255, 255))
                gameDisplay.blit(line1, (50,300))
                gameDisplay.blit(line2, (125,400))
            elif level2_done == True:
                line1 = font1.render('You beat level 2!', False, (255, 255, 255))
                gameDisplay.blit(line1, (50,300))
                gameDisplay.blit(line2, (125,400))
            elif level1_done == True:
                line1 = font1.render('You beat level 1!', False, (255, 255, 255))
                gameDisplay.blit(line1, (50,300))
                gameDisplay.blit(line2, (125,400))
            else:
                waitscreen = False
            pygame.display.flip()
#runs approriate level
def levelRunner(on):
    if on != True and level1_done != True:
        level1()
    elif on != True and level2_done != True:
        level2()
    elif on != True and level3_done != True:
        level3()
    elif on != True and level4_done != True:
        level4()
    elif on != True and bossDone != True:
        bossLevel()
    elif on != True and bossDone == True:
        cutscene()
#bullet move and display function
def bulletManager():
    global bulletX
    global bulletY
    #create movement of bullets
    for b in range(len(bulletX)):
        bulletY[b]-=10

    #display bullet image for each projectile
    if is_running == True:
        for b in range(len(bulletX)):
            gameDisplay.blit(goodTea, (bulletX[b], bulletY[b]))
    else:
        bulletX = []
        bulletY = []
    
    #deletes bullet if it reaches the top
    if len(bulletX) > 0:
        if bulletY[0] == 0:
            bulletX.remove(bulletX[0])
            bulletY.remove(bulletY[0])
#enemy moving function
def enemyMove():
    global lives
    #deletes any life removing enemies later
    global enemy1R
    global enemy2R
    global enemy3R
    enemy1R = []
    enemy2R = []
    enemy3R = []

    for e in range(len(enemy1List)):
        if enemy1Y[e] == 100 or enemy1Y[e] == 300 or enemy1Y[e] == 500:
            enemy1X[e] -= 5
        else:
            enemy1X[e] += 5
        if enemy1X[e] > 760 and enemy1Y[e] == 600:
            lives -= 1
            enemy1R.append(e)
        if enemy1X[e] < 0:
            enemy1X[e] = 0
            enemy1Y[e] += 100
        elif enemy1X[e] > 760:
            enemy1X[e] = 760
            enemy1Y[e] += 100
    
    for e in range(len(enemy2List)):
        if enemy2Y[e] == 100 or enemy2Y[e] == 300 or enemy2Y[e] == 500:
            enemy2X[e] -= 5
        else:
            enemy2X[e] += 5
        if enemy2X[e] > 760 and enemy2Y[e] == 600:
            lives -= 1
            enemy2R.append(e)
        if enemy2X[e] < 0:
            enemy2X[e] = 0
            enemy2Y[e] += 100
        elif enemy2X[e] > 760:
            enemy2X[e] = 760
            enemy2Y[e] += 100
    
    for e in range(len(enemy3List)):
        if enemy3Y[e] == 100 or enemy3Y[e] == 300 or enemy3Y[e] == 500:
            enemy3X[e] -= 5
        else:
            enemy3X[e] += 5
        if enemy3X[e] > 760 and enemy3Y[e] == 600:
            lives -= 1
            enemy3R.append(e)
        if enemy3X[e] < 0:
            enemy3X[e] = 0
            enemy3Y[e] += 100
        elif enemy3X[e] > 760:
            enemy3X[e] = 760
            enemy3Y[e] += 100
    #removes any enemies that cause you to lose a life
    for index in sorted(enemy1R, reverse=True):
        del enemy1Y[index]
        del enemy1X[index]
        del enemy1List[index]
    for index in sorted(enemy2R, reverse=True):
        del enemy2Y[index]
        del enemy2X[index]
        del enemy2List[index]
    for index in sorted(enemy3R, reverse=True):
        del enemy3Y[index]
        del enemy3X[index]
        del enemy3List[index]
        enemy1R = []
        enemy2R = []
        enemy3R = []
#enemy displayer function
def enemyDisplay():
    for e in range(len(enemy1List)):
        currentX = enemy1X[e]
        currentY = enemy1Y[e]
        gameDisplay.blit(enemy1,(currentX, currentY))
    
    for e in range(len(enemy2List)):
        currentX = enemy2X[e]
        currentY = enemy2Y[e]
        gameDisplay.blit(enemy2,(currentX, currentY))

    for e in range(len(enemy3List)):
        currentX = enemy3X[e]
        currentY = enemy3Y[e]
        gameDisplay.blit(enemy3,(currentX, currentY))
#hit detection program
def hitDetection():
    global points
    global lives
    global enemy1R
    global enemy2R
    global enemy3R
    bulletR = []
    enemy1R = []
    enemy2R = []
    enemy3R = []
    #hit detection for enemy 1
    for e in range(len(enemy1List)):
        for b in range(len(bulletX)):
            if bulletX[b] >= enemy1X[e] and bulletX[b] <= enemy1X[e] + 40:
                if bulletY[b] >= enemy1Y[e] and bulletY[b] <= enemy1Y[e] + 90:
                        if e not in enemy1R:
                            bulletR.append(b)
                            enemy1R.append(e)
                        else:
                            placeholder = 1
                else:
                    placeholder = 1
            else:
                placeholder = 1
    #remove any bullet and enemy 1 collisions
    for index in sorted(bulletR, reverse=True):
        del bulletY[index]
        del bulletX[index]
    for index in sorted(enemy1R, reverse=True):
        del enemy1Y[index]
        del enemy1X[index]
        del enemy1List[index]
    for kills in range(len(enemy1R)):
        points += 10
    bulletR = []
    enemy1R = []

    #hit detection for enemy 2
    for e in range(len(enemy2List)):
        for b in range(len(bulletX)):
            if bulletX[b] >= enemy2X[e] and bulletX[b] <= enemy2X[e] + 40:
                if bulletY[b] >= enemy2Y[e] and bulletY[b] <= enemy2Y[e] + 90:
                    if e not in enemy2R: 
                        bulletR.append(b)
                        enemy2List[e] -= 1
                        if enemy2List[e] == 0:
                            enemy2R.append(e)
                    else:
                        placeholder = 1
                else:
                    placeholder = 1
            else:
                placeholder = 1
    #removes any bullet and enemy 2 deaths
    for index in sorted(bulletR, reverse=True):
        del bulletY[index]
        del bulletX[index]
    for index in sorted(enemy2R, reverse=True):
        del enemy2Y[index]
        del enemy2X[index]
        del enemy2List[index]
    for kills in range(len(enemy2R)):
        points += 20
    bulletR = []
    enemy2R = []

    #hit detection for enemy 3
    for e in range(len(enemy3List)):
        for b in range(len(bulletX)):
            if bulletX[b] >= enemy3X[e] and bulletX[b] <= enemy3X[e] + 90:
                if bulletY[b] >= enemy3Y[e] and bulletY[b] <= enemy3Y[e] + 90:
                    if e not in enemy3R:
                        bulletR.append(b)
                        enemy3List[e] -= 1
                        if enemy3List[e] == 0:
                            enemy3R.append(e)
                    else:
                        placeholder = 1
                else:
                    placeholder = 1
            else:
                placeholder = 1
    #removes any bullet and enemy 2 deaths
    for index in sorted(bulletR, reverse=True):
        del bulletY[index]
        del bulletX[index]
    for index in sorted(enemy3R, reverse=True):
        del enemy3Y[index]
        del enemy3X[index]
        del enemy3List[index]
    for kills in range(len(enemy3R)):
        points += 40
    bulletR = []
    enemy3R = []
#displays points
def pointDisplay():
    font1 = pygame.font.SysFont('Arial', 30)
    line1 = font1.render('Points:' + str(points), False, (255, 255, 255))
    gameDisplay.blit(line1, (10, 750))
#display lives
def lifeDisplay():
    global dead
    font1 = pygame.font.SysFont('Arial', 30)
    line1 = font1.render('Lives:', False, (255, 255, 255))
    gameDisplay.blit(line1, (600, 750))
    if lives == 3:
        gameDisplay.blit(life, (690, 750))
        gameDisplay.blit(life, (730, 750))
        gameDisplay.blit(life, (770, 750))
    elif lives == 2:
        gameDisplay.blit(life, (690, 750))
        gameDisplay.blit(life, (730, 750))
    elif lives == 1:
        gameDisplay.blit(life, (690, 750))
    else:
        dead = True
#death screen
def deathScreen():
    global lives
    music = False
    while lives == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                os._exit(1)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main()
        if music == False:
            deathsound = random.randint(1,3)
        if deathsound == 1 and music == False:
            pygame.mixer.music.load('ah.mp3')
            pygame.mixer.music.play(0, 0.0)
            music = True
        elif deathsound == 2 and music == False:
            pygame.mixer.music.load('snake.mp3')
            pygame.mixer.music.play(0, 6.0)
            music = True
        elif deathsound == 3 and music == False:
            pygame.mixer.music.load('fatal.mp3')
            pygame.mixer.music.play(0, 0.0)
            music = True
        font3 = pygame.font.SysFont('Impact', 90)
        font4 = pygame.font.SysFont('Impact', 50)
        line1 = font3.render('GAME OVER!', False, (255, 0, 0))
        line2 = font4.render('ENTER TO CONTINUE', False, (255, 0, 0))
        gameDisplay.blit(line1, (210,300))
        gameDisplay.blit(line2, (210,450))
        pygame.display.update()
#create boss everything
def bossMove():
    global bossHealth
    if bossHealth > 0:
        global left
        global enraged
        global bossX
        global bossY
        if bossHealth <= 25:
            enraged = True
        
        if left == True and enraged == False:
            bossX -= 5
        elif left == False and enraged == False:
            bossX += 5
        elif left == True and enraged == True:
            bossX -= 10
        elif left == False and enraged == True:
            bossX += 10
        
        if bossX-90 < 0:
            left = False
            bossX = 90
        elif bossX+210 > 800:
            left = True
            bossX = 590
#displays boss
def bossDisplay():
    global bossJug
    global boss
    if bossHealth > 0:
        if bossHealth <= 25:
            boss = angryBoss
            bossJug = angryJug
        gameDisplay.blit(bossJug,(bossX-90,bossY+30))
        gameDisplay.blit(boss,(bossX,bossY))
        gameDisplay.blit(bossJug,(bossX+120,bossY+30))
#boss hit detection
def bossHit():
    global bossHealth
    if bossHealth > 0:
        bulletR = []
        for b in range(len(bulletX)):
            if bulletX[b] >= bossX - 90 and bulletX[b] <= bossX + 210:
                if bulletY[b] <= 120:
                    bulletR.append(b)
                    bossHealth -= 1
                else:
                    placeholder = 1
            else:
                placeholder = 1
        
        for index in sorted(bulletR, reverse=True):
            del bulletY[index]
            del bulletX[index]
        bulletR = []
#shooting function
def bossFire():
    global cansY
    global cansX
    global bossTimer
    global pos
    global lives
    cansR = []
    if bossHealth > 0:
        if bossHealth <= 25:
            if bossTimer >= 44:
                canY = bossY + 30
                can1X = bossX - 45
                can2X = bossX + 165
                can3X = bossX + 60
                cansY.append(canY)
                cansY.append(canY)
                cansY.append(canY)
                cansX.append(can1X)
                cansX.append(can2X)
                cansX.append(can3X)
                bossTimer = 0
            else:
                 bossTimer += 1
            can = angryCan
        else:
            if bossTimer >= 66:
                canY = bossY + 30
                can1X = bossX - 45
                can2X = bossX + 165
                cansY.append(canY)
                cansY.append(canY)
                cansX.append(can1X)
                cansX.append(can2X)
                bossTimer = 0
            else:
                 bossTimer += 1
            can = enemy2
        
        #create movement of bullets
        for c in range(len(cansY)):
            cansY[c]+=10

        #display bullet image for each projectile
        for c in range(len(cansY)):
            gameDisplay.blit(can, (cansX[c], cansY[c]))
        
        #creates collison vs sanchez
        for c in range(len(cansY)):
            if cansX[c] >= pos[0]-32-40 and cansX[c] <= pos[0]+43:
                if cansY[c] >= 700 - 90 and cansY[c] <= 700 + 90: 
                        cansR.append(c)
                        lives -= 1
                else:
                    placeholder = 1
            else:
                placeholder = 1

        #deletes bullet if it reaches the bottom
        if len(cansY) > 0:
            for c in range(len(cansY)):
                if cansY[c] >= 800:
                    cansR.append(c)

        #removes cans from list
        for index in sorted(cansR, reverse=True):
            del cansY[index]
            del cansX[index]
        cansR = []
#cutscene
def cutscene():
    global final
    global charging
    global end
    if final == False:
        bossFight()
    if charging == False:
        beam()
    if end == False:
        ending()
#boss fight cinematic
def bossFight():
    global final
    superSanchez = pygame.image.load('superSanchez.png')
    superSanchez = pygame.transform.scale(superSanchez,(200,200))
    jukebox('screm.mp3',0.0)
    gameDisplay.blit(superSanchez,(300,600))
    gameDisplay.blit(angryJug,(320-90,0+30))
    gameDisplay.blit(angryBoss,(320,0))
    gameDisplay.blit(angryJug,(320+120,0+30))
    pygame.display.update()
    final = True
#beam function
def beam():
    global charging
    placeholder = useless()
    pygame.time.wait(1000)
    teaX = 320
    for i in range(6):
        gameDisplay.blit(goodTea,(teaX,600))
        teaX += 20
        pygame.display.update()
        pygame.time.wait(1000)
    placeholder = useless()
    teaX = 320
    for i in range(6):
        gameDisplay.blit(goodTea,(teaX,600-60))
        teaX += 20
        pygame.display.update()
        pygame.time.wait(800)
    placeholder = useless()
    teaX = 320
    for i in range(6):
        gameDisplay.blit(goodTea,(teaX,600-120))
        teaX += 20
        pygame.display.update()
        pygame.time.wait(600)
    placeholder = useless()
    teaX = 320
    for i in range(6):
        gameDisplay.blit(goodTea,(teaX,600-180))
        teaX += 20
        pygame.display.update()
        pygame.time.wait(400)
    placeholder = useless()
    teaX = 320
    for i in range(6):
        gameDisplay.blit(goodTea,(teaX,600-240))
        teaX += 20
        pygame.display.update()
        pygame.time.wait(200)
    placeholder = useless()
    teaX = 320
    for i in range(6):
        gameDisplay.blit(goodTea,(teaX,600-300))
        teaX += 20
        pygame.display.update()
        pygame.time.wait(100)
    placeholder = useless()
    teaX = 320
    for i in range(6):
        gameDisplay.blit(goodTea,(teaX,600-360))
        teaX += 20
        pygame.display.update()
        pygame.time.wait(50)
    placeholder = useless()
    teaX = 320
    for i in range(6):
        gameDisplay.blit(goodTea,(teaX,600-420))
        teaX += 20
        pygame.display.update()
        pygame.time.wait(0)
    placeholder = useless()
    pygame.time.wait(100)
    bigTea = pygame.image.load('goodTea.png')
    bigTea = pygame.transform.scale(bigTea,(120,500))
    gameDisplay.blit(bigTea,(320,160))
    pygame.display.update()
    jukebox('Boom.mp3',0.0)
    placeholder = useless()
    pygame.time.wait(2000)
    charging = True
#ending cinematic
def ending():
    global end
    boom1=pygame.image.load('Boom1.png')
    boom1=pygame.transform.scale(boom1,(800,800))
    boom2=pygame.image.load('Boom2.png')
    boom2=pygame.transform.scale(boom2,(800,800))
    boom3=pygame.image.load('Boom3.png')
    boom3=pygame.transform.scale(boom3,(800,800))
    boom4=pygame.image.load('Boom4.png')
    boom4=pygame.transform.scale(boom4,(800,800))
    boom5=pygame.image.load('Boom5.png')
    boom5=pygame.transform.scale(boom5,(800,800))
    boom6=pygame.image.load('Boom6.png')
    boom6=pygame.transform.scale(boom6,(800,800))
    boom7=pygame.image.load('Boom7.png')
    boom7=pygame.transform.scale(boom7,(800,800))
    boom8=pygame.image.load('Boom8.png')
    boom8=pygame.transform.scale(boom8,(800,800))
    jukebox('chorus.mp3',3.0)
    placeholder = useless()
    gameDisplay.blit(boom1,(0,0))
    pygame.display.update()
    pygame.time.wait(1750)
    placeholder = useless()
    gameDisplay.blit(boom2,(0,0))
    pygame.display.update()
    pygame.time.wait(1750)
    placeholder = useless()
    gameDisplay.blit(boom3,(0,0))
    pygame.display.update()
    pygame.time.wait(1750)
    placeholder = useless()
    gameDisplay.blit(boom4,(0,0))
    pygame.display.update()
    pygame.time.wait(1750)
    placeholder = useless()
    gameDisplay.blit(boom5,(0,0))
    pygame.display.update()
    pygame.time.wait(1750)
    placeholder = useless()
    gameDisplay.blit(boom6,(0,0))
    pygame.display.update()
    pygame.time.wait(1750)
    placeholder = useless()
    gameDisplay.blit(boom7,(0,0))
    pygame.display.update()
    pygame.time.wait(1750)
    placeholder = useless()
    gameDisplay.blit(boom8,(0,0))
    pygame.display.update()
    pygame.time.wait(1750)
    placeholder = useless()
    superSanchez = pygame.image.load('superSanchez.png')
    superSanchez = pygame.transform.scale(superSanchez,(200,200))
    gameDisplay.blit(background,(0,0))
    gameDisplay.blit(superSanchez,(300,600))
    pygame.display.update()
    placeholder = useless()
    jukebox('win.mp3',0.0)
    font3 = pygame.font.SysFont('Impact', 190)
    line1 = font3.render('YOU WIN!', False, (255, 0, 0))
    gameDisplay.blit(line1,(50,200))
    pygame.display.update()
    end = True 
#function that prevents game freezing
def useless():
    if pygame.event.pump() != 'placeholder':
        return 1
#create main loop
def main():
    #import all images
    global background
    background = pygame.image.load('space.jpg')
    background = pygame.transform.scale(background, (800,800))
    global sanchez
    sanchez = pygame.image.load('sanchez.png')
    sanchez = pygame.transform.scale(sanchez, (75,90))
    global goodTea
    goodTea = pygame.image.load('goodTea.png')
    goodTea = pygame.transform.scale(goodTea, (20,60))
    global enemy1
    enemy1 = pygame.image.load('arizona grunt.png').convert_alpha()
    enemy1 = pygame.transform.scale(enemy1, (40,90))
    global enemy2
    enemy2 = pygame.image.load('arizona tea.png').convert_alpha()
    enemy2 = pygame.transform.scale(enemy2, (40,90))
    global enemy3
    enemy3 = pygame.image.load('arizona jug.png').convert_alpha()
    enemy3 = pygame.transform.scale(enemy3, (90,90))
    global boss
    boss = pygame.image.load('arizona ceo.jpg').convert_alpha()
    boss = pygame.transform.scale(boss, (120,150))
    global life
    life = pygame.image.load('lives.png').convert_alpha()
    life = pygame.transform.scale(life, (30,60))
    global bossJug
    bossJug = pygame.transform.rotate(enemy3, 180)
    global angryBoss
    angryBoss = pygame.image.load('angry boss.png').convert_alpha()
    angryBoss = pygame.transform.scale(angryBoss, (120, 150))
    global angryCan
    angryCan = pygame.image.load('angryCan.png').convert_alpha()
    angryCan = pygame.transform.scale(angryCan, (40,90))
    global angryJug
    angryJug = pygame.image.load('angryJug.png').convert_alpha()
    angryJug = pygame.transform.scale(angryJug, (90,90))
    #set up various conditions
    global points
    points = 0
    global lives
    lives = 3
    global dead
    dead = False
    global gameEnd
    gameEnd = False
    global is_running
    is_running = False
    global level1_done
    level1_done = False
    global level2_done
    level2_done = False
    global level3_done
    level3_done = False
    global level4_done
    level4_done = False
    global bossDone
    bossDone = False
    global jukeon
    jukeon = False
    #create enemy and bullet stuff
    #bullet list
    global bulletX
    bulletX = []
    global bulletY
    bulletY = []
    #enemy 1 lists
    global enemy1List
    enemy1List = []
    global enemy1X
    enemy1X = []
    global enemy1Y
    enemy1Y = []
    #enemy 2 lists
    global enemy2List
    enemy2List = []
    global enemy2X
    enemy2X = []
    global enemy2Y
    enemy2Y = []
    #enemy 3 lists
    global enemy3List
    enemy3List = []
    global enemy3X
    enemy3X = []
    global enemy3Y
    enemy3Y = []
    #boss stuff
    global bossHealth
    bossHealth = 0
    global bossX
    bossX = 290
    global bossY
    bossY = 0
    global left
    left = True
    global enraged
    enraged = False
    global cansX
    cansX = []
    global cansY
    cansY = []
    global bossTimer
    bossTimer = 0
    global jukeon2
    jukeon2 = False
    global final
    final = False
    global charging
    charging = False
    global end
    end = False
    #title screen
    game_intro(displayX, displayY)
    # run the game loop
    while not gameEnd:
        #gets position of mouse
        global pos
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                gameEnd = True
                os._exit(1)
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    bulletX.append(pos[0])
                    bulletY.append(700)

        #sets frames per second
        fps.tick(60)
    
        #creates background
        gameDisplay.blit(background,(0,0))
    
        #checks if game is running
        is_running = runchecker()

        #call bullet management function
        bulletManager()

        #you beat the level message
        levelComplete(is_running, jukeon, jukeon2)

        #spawns levels if the game isnt running
        levelRunner(is_running)
    
        #moves the enemies
        enemyMove()

        #displays every enemy
        enemyDisplay()

        #hit detection program
        hitDetection()

        #display sanchez
        gameDisplay.blit(sanchez,(pos[0]-32, 700))

        #display points
        pointDisplay()

        #display lives
        lifeDisplay()

        #death screen
        deathScreen()

        #boss ai
        bossMove()
        
        #boss display
        bossDisplay()

        #boss hit detection
        bossHit()

        #boss fire
        bossFire()
        #update entire screen
        pygame.display.flip()
main()
