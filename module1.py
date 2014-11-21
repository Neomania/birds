#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Timothy
#
# Created:     03/09/2014
# Copyright:   (c) Timothy 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    import pygame, sys, os, random
    FPS = 60
    DEVPINK = (255,0,255)
    RED = (255,255,0)
    BLACK = (0,0,0)
    PATHINT = 0

    pygame.init()
    screensurface = pygame.display.set_mode((800,640))
    pygame.display.set_caption('hello birb')

    pygame.display.update()
    fpsClock = pygame.time.Clock()
    boidArray = []
    boidArray.append(boid(500,500))
    boidArray.append(boid(350,350))
    nearestBoidIndex = 0
    lowestDistance = 0.0
    currentDistance = 0.0
    boidXArray = []
    boidYArray = []
    turncount = 0
    counter1 = 0
    counter2 = 0
    random.seed()
    rndthing = random.Random()
    calculationCounter = 0
    yOffset = 0
    xOffset = 0
    xMovementState = 0
    xMovementLeft = False
    xMovementRight = False
    yMovementUp = False
    yMovementDown = False
    yMovementState = 0
    movementAmount = 10
    floTimeScale = 1.0
    wallArray = []

    while True:
        turncount = turncount + 1
        surfaceArray = pygame.PixelArray(screensurface)
        #if turncount == PATHINT:
         #   turncount = 0
        counter1 = - 1
        for birb in boidArray:
            birb.timeToMove = birb.timeToMove - 1
            counter1 = counter1 + 1
            if birb.timeToMove <= 0:
                counter2 = - 1
                lowestDistance = 999999.0
                nearestBoidIndex = 0
                if random.random() < 0.9:
                    for birby in boidArray:
                        calculationCounter = calculationCounter + 1
                        counter2 = counter2 + 1
                        if not counter1 == counter2:
                            currentDistance = birb.calcDistanceTo(birby.posX,birby.posY)
                            if currentDistance < lowestDistance:
                                lowestDistance = currentDistance
                                nearestBoidIndex = counter2
                    birb.moveTowards(boidArray[nearestBoidIndex])
                else:
                    birb.randomMove()
                print(calculationCounter)

                #birb.randomMove()


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                boidArray.append(boid(pygame.mouse.get_pos()[0] - xOffset,pygame.mouse.get_pos()[1] - yOffset))
            elif event.type == KEYDOWN:
                if event.key == K_a:
                    xMovementLeft = True
                elif event.key == K_d:
                    xMovementRight = True
                elif event.key == K_w:
                    yMovementUp = True
                elif event.key == K_s:
                    yMovementDown = True
                elif event.key == K_RIGHT:
                    floTimeScale = floTimeScale * 2
                elif event.key == K_LEFT:
                    if floTimeScale > 0.125:
                        floTimeScale = floTimeScale / 2
                elif event.key == K_i:
                    wallArray.append(Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],50,50))
            elif event.type == KEYUP:
                if event.key == K_a:
                    xMovementLeft = False
                elif event.key == K_d:
                    xMovementRight = False
                elif event.key == K_w:
                    yMovementUp = False
                elif event.key == K_s:
                    yMovementDown = False
        if xMovementLeft:
            xOffset = xOffset + movementAmount
        if xMovementRight:
            xOffset = xOffset - movementAmount
        if yMovementUp == 1:
            yOffset = yOffset + movementAmount
        if yMovementDown:
            yOffset = yOffset - movementAmount

        screensurface.fill(BLACK)
        for wall in wallArray:
            screensurface.fill(DEVPINK,wall)
##        for currentBee in boidArray:
##            #currentBee.updatePosition()
##
##            #Collision handling for each bee
##            if surfaceArray[round(currentBee.posX),round(currentBee.posY)] == screensurface.map_rgb(DEVPINK):
##                print('collision detected')
##                if surfaceArray[round(currentBee.posX),round(currentBee.lastPosY)] == screensurface.map_rgb(DEVPINK):
##                    if currentBee.lastPosX > currentBee.posX:
##                        while surfaceArray[round(currentBee.posX),round(currentBee.lastPosY)] == screensurface.map_rgb(DEVPINK): #removed +/- 1 on coordinates to fix jitter bug
##                            currentBee.posX = currentBee.posX + 1
##                    else:
##                        while surfaceArray[round(currentBee.posX),round(currentBee.lastPosY)] == screensurface.map_rgb(DEVPINK):
##                            currentBee.posX = currentBee.posX - 1
##                    currentBee.xVelocity = 0
##                if surfaceArray[round(currentBee.lastPosX),round(currentBee.posY)] == screensurface.map_rgb(DEVPINK):
##                    if currentBee.lastPosY > currentBee.posY:
##                        while surfaceArray[round(currentBee.lastPosX),round(currentBee.posY)] == screensurface.map_rgb(DEVPINK):
##                            currentBee.posY = currentBee.posY + 1
##                    else:
##                        while surfaceArray[round(currentBee.lastPosX),round(currentBee.posY)] == screensurface.map_rgb(DEVPINK):
##                            currentBee.posY = currentBee.posY - 1
##                    currentBee.yVelocity = 0


        for birb in boidArray:
            if birb.xVelocity > 0:
                birb.xVelocity = birb.xVelocity - 0.01
            elif birb.xVelocity < 0:
                birb.xVelocity = birb.xVelocity + 0.01
            if birb.yVelocity > 0:
                birb.yVelocity = birb.yVelocity - 0.01
            elif birb.yVelocity < 0:
                birb.yVelocity = birb.yVelocity + 0.01
            birb.updatePosition()
            pygame.draw.circle(screensurface,(birb.rColor,255,birb.bColor),(round(birb.posX) + xOffset,round(birb.posY) + yOffset),2,0)
        pygame.display.update()
        fpsClock.tick(FPS * floTimeScale)

class boid:
    posX = 0.0
    posY = 0.0
    xVelocity = 0.0
    yVelocity = 0.0
    timeToMove = 0
    rColor = 255
    gColor = 255
    bColor = 255
    def __init__(self,posX,posY):
        import random
        self.posX = posX
        self.posY = posY
        self.rColor = round(random.random() * 255)
        self.gColor = round(random.random() * 255)
        self.bColor = round(random.random() * 255)
    def randomMove(self):
        import random
        self.xVelocity = round((random.random() * 5) - 2.5,1)
        self.yVelocity = round((random.random() * 5) - 2.5,1)
        self.timeToMove = (random.random() * 60) + 30

    def moveTowards(self,otherbirb):
        import random
        thing = self.calcDistanceTo(otherbirb.posX,otherbirb.posY)
        if thing == 0:
            self.randomMove()
        else:
            self.xVelocity = 2 * ((otherbirb.posX - self.posX)/thing)
            self.yVelocity = 2 * ((otherbirb.posY - self.posY)/thing)
            self.timeToMove = (random.random() * 60) + 30


    def updatePosition(self):
        self.lastPosX = self.posX
        self.lastPosY = self.posY
        self.posX = self.posX + self.xVelocity
        self.posY = self.posY + self.yVelocity
    def calcDistanceTo(self,boidX,boidY):
        return (((self.posX - boidX) ** 2)+((self.posY - boidY)** 2)) ** 0.5


class boidposition:
    posX = 0
    posY = 0


if __name__ == '__main__':
    from pygame.locals import *
    main()
