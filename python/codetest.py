import pygame
pygame.init()

display_width = 450
display_height = 450

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('pacman space')
clock = pygame.time.Clock()

bG = pygame.image.load('maptest.png')
pcL = pygame.image.load('pacL.png')
pcR = pygame.image.load('pacR.png')
pcU = pygame.image.load('pacU.png')
pcD = pygame.image.load('pacD.png')
xw,yh = 25,25
#คะแนน
#def score(count):
#    font = pygame.font.SysFont(None,25)
#    text = font.render("Score: "+str(count),True,black)
#    gameDisplay.blit(text,(display_width/2 , display_height/2))
def walk(x,y,x_change,y_change):
#แนวนอน
        if (x > 88 and x+xw < 362 and y > 360 and y+yh < 397):
                x = x
        else:
               x -= x_change
#แนวตั้ง
        if checkwalk(x,y,184,218,315,397):
               y = y
        else:
               y -= y_change
        return x,y
def checkwalk(x,y,cx1,cx2,cy1,cy2):
        g = False
        if (x > cx1 and x+xw < cx2 and y > cy1 and y+yh < cy2):
                g = True
        return g
#แสดงผลตัวละคร
def pac(x,y,z):
    if z == 1:
        gameDisplay.blit(pcL,(x,y))
    elif z == 2:
        gameDisplay.blit(pcR,(x,y))
    elif z == 3:
        gameDisplay.blit(pcU,(x,y))
    elif z == 4:
        gameDisplay.blit(pcD,(x,y))
def gameloop():
        dot = []
        speed = 2
        x = 210
        y = 366
        x_change = 0
        y_change = 0
        count = 0
        z = 1
        end = False
        while not end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -speed
                        y_change = 0
                        z = 1
                    elif event.key == pygame.K_RIGHT:
                        x_change = speed
                        y_change = 0
                        z = 2
                    elif event.key == pygame.K_UP:
                        y_change = -speed
                        x_change = 0
                        z = 3
                    elif event.key == pygame.K_DOWN:
                        y_change = speed
                        x_change = 0
                        z = 4
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        x_change = -speed
                        y_change = 0
                        z = 1
                    elif event.key == pygame.K_RIGHT:
                        x_change = speed
                        y_change = 0
                        z = 2
                    elif event.key == pygame.K_UP:
                        y_change = -speed
                        x_change = 0
                        z = 3
                    elif event.key == pygame.K_DOWN:
                        y_change = speed
                        x_change = 0
                        z = 4
                print(event)
#การเดิน
            x += x_change
            y += y_change
            x,y = walk(x,y,x_change,y_change)
#การเก็บดอท
#           for i,j in dotf:
#                if x < i and x > i and y < j and y > j:
#           for u in range(-1,len(dotf)-1):
#                if dotf[u] == (i,j):
#                     del dotf[u]
#                     count += 1
#วาดรูป
            gameDisplay.fill(white)
            gameDisplay.blit(bG,(0,0))
#           for i,j in dotf:
#                gameDisplay.blit(,(i,j))
            pac(x,y,z)
#           score(count)
            pygame.display.update()
            clock.tick(60)
gameloop()
pygame.quit()
quit()
