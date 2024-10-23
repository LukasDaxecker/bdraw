# pyinstaller --onefile -w "name.py"
import pygame
import os

def SaveWindow():
    return

def OpenWindow():
    return
    
class SavableRect:
    def __init__(self, color, pos, size):
        self.color = color
        self.pos = pos
        self.size = size

    def __str__(self):
        if self.color == 0:
            return ("white, x: " + str(self.pos[0]) + ", y: " + str(self.pos[1]) + ", " + str(self.size))
        elif self.color == 1:
            return ("black, x: " + str(self.pos[0]) + ", y: " + str(self.pos[1]) + ", " + str(self.size))

if __name__ =="__main__":
        pygame.init()
        cwd = os.getcwd()
        done = False
        rects = []
        window = pygame.display.set_mode((1200, 1200/12 * 9))
        window.fill((0,0,0))
        rectSize = 10
        rectSizeUser = 10

        while not done:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            done = True

                        if pygame.mouse.get_pressed()[0]:
                            rectPos = pygame.mouse.get_pos()
                            rects.append(SavableRect(0, rectPos, rectSize))
                            pygame.draw.rect(window, (200,200,200), pygame.Rect(rectPos[0], rectPos[1], rectSize, rectSize))
                        if pygame.mouse.get_pressed()[2]:
                            rectPos = pygame.mouse.get_pos()
                            rects.append(SavableRect(1, rectPos, rectSize))
                            pygame.draw.rect(window, (0,0,0), pygame.Rect(rectPos[0], rectPos[1], rectSize + 2.5, rectSize + 2.5))

                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 4:
                                if rectSize < 75:
                                    rectSize += 2.5
                                    rectSizeUser = rectSize
                            if event.button == 5:
                                if rectSize > 2.5:
                                    rectSize -= 2.5
                                    rectSizeUser = rectSize

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                pygame.QUIT
                                done = True
                            if event.key == pygame.K_LSHIFT:
                                if rectSize != 75:
                                    rectSize = 75
                                else:
                                    rectSize = rectSizeUser
                            if event.key == pygame.K_n: # Create new Window
                                os.startfile(cwd + "\\bdraw.exe")
                            if event.key == pygame.K_s:
                                SaveWindow()
                            if event.key == pygame.K_o:
                                OpenWindow()
                            # if event.key == pygame.K_u  # Undo last move
                            if event.key == pygame.K_c: 
                                window.fill((0,0,0))

                pygame.display.update()