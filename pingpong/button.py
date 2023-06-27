import pygame

class Button():
    def __init__(self, x,y, image, scale=1):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int((width*scale)), int((height*scale))))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False
    def draw(self, window):
        action = False

        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if self.clicked == False and pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
                action = True
                

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            

        window.blit(self.image, (self.rect.x, self.rect.y))

        return action