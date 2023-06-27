from multiprocessing import Event
import pygame #Імпорт модуля
from time import*
from button import*
pygame.init() #                               ↰ 
color = (0,0,0)#                          | стврення вікна гри
window = pygame.display.set_mode((850,850))#  |
window.fill(color)#                           ↲
pygame.display.set_caption('Пінг понг')
pygame.display.set_icon(pygame.image.load("icon.png"))
class Area(): # створення класу
    def __init__(self,x,y,width,height,color): # cтворення конструктора класу
        self.rect = pygame.Rect(x,y,width,height)
        self.color = color 

    def set_color(self, color):#Встановлення кольору класу
        self.color = color
        
    def fill(self):#Втановлення заливки класу
        pygame.draw.rect(window, self.color, self.rect)
    def outline(self, color, thickness):#Створення обводки
        pygame.draw.rect(window, color, self.rect,thickness)
    def colliderect(self,enemy):
        return self.rect.colliderect(enemy.rect)

class Label(Area):#Створення класу картки
    def set_text(self, text, text_color, text_size):#Встановлення тексту картки
        self.font = pygame.font.SysFont("Bold", text_size)#Встановлення шрифту текста
        self.text = self.font.render(text, True, text_color)
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)
    def draw(self, s_x, s_y):
        self.fill()
        window.blit(self.text, (self.rect.x+s_x, self.rect.y+s_y))

class Picture(Area):#Стврення класу картинки
    def __init__(self, filename, x, y,width,height,color=(0,255,25)):
        super().__init__(x, y,width,height,color)
        self.image = pygame.image.load(filename)
    def draw(self):#Відмальовування картинк
        window.blit(self.image,(self.rect.x,self.rect.y))
play = False
clock = pygame.time.Clock() 

platform1 = Picture("platform.png", 0,200,10,100)
platform2 = Picture("platform.png", 800,200,10,100)
ball = Picture("ball.png", 230,230,30,100)

iquit = pygame.image.load("quit.png")


iresum = pygame.image.load("resum.png")

resumbtn = Button(400,300, iresum , 1)
quitbtn = Button(200, 300, iquit, 1)
menu = True

musca = True

startt = False



speed_x = 2
speed_y = 2
musice = pygame.mixer.Sound('music.mp3')
jump = pygame.mixer.Sound('jump.mp3')
jump.set_volume(0.5)
move_up1 = False
move_down1 = False
move_up2 = False
move_down2 = False
winleft = 0
winright = 0

musice.set_volume(0.1)
musice.play(-1)


p1 = Label(0, 0, 150, 25,(0,0,0))
p1.set_text("Player1: " + str(winleft) ,(255,255,255), 40)
p1.outline((255,255,255),10)
p2 = Label(700, 0, 150, 25,(0,0,0))
p2.set_text("Player2: " + str(winright) ,(255,255,255), 40)
p2.outline((255,255,255),10)
while True: 
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_up1 = True
            if event.key == pygame.K_DOWN:
                move_down1 = True
            if event.key == pygame.K_w:
                move_up2 = True
            if event.key == pygame.K_s:
                move_down2 = True
            if event.key == pygame.K_l:
                sleep(10)
            if event.key == pygame.K_ESCAPE:
                menu = True
                musca = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                move_up1 = False
            if event.key == pygame.K_DOWN:
                move_down1 = False
            if event.key == pygame.K_w:
                move_up2 = False
            if event.key == pygame.K_s:
                move_down2 = False
    
    

    if menu:
        if resumbtn.draw(window):
            menu = False
            
        if quitbtn.draw(window):
            exit() 
            
    else:

        if move_up1 == True:
            platform2.rect.y -= 5
    
        if move_down1 == True:
            platform2.rect.y += 5
        
        if move_up2 == True:
            platform1.rect.y -= 5
    
        if move_down2 == True:
            platform1.rect.y += 5
    
        if platform1.rect.y <=0:
            platform1.rect.y = 1
    
        if platform2.rect.y <=0:
            platform2.rect.y = 1 
    
        if platform1.rect.y >=800:
            platform1.rect.y = 800
    
        if platform2.rect.y >=800:
            platform2.rect.y = 800 
        
        p1.outline((255,255,255),10)
        p2.outline((255,255,255),10)
        
        
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.colliderect(platform1):
            speed_x *= -1
            jump.play()
        if ball.colliderect(platform2):
            speed_x *= -1
            jump.play()
                
        if ball.rect.x >=870:
            winleft += 1
            ball.rect.x = 500
            ball.rect.y = 500
            p1.set_text("Player1: " + str(winleft) ,(255,255,255), 40)
            jump.play()

        if ball.rect.y <=0:
            speed_y *=-1
            jump.play()
                
        if ball.rect.x <=-10:
            winright +=1
            ball.rect.x = 500
            ball.rect.y = 500
            p2.set_text("Player2: " + str(winright) ,(255,255,255), 40)
            jump.play()

        if ball.rect.y >=800:    
            speed_y *=-1
            jump.play()
        
        window.fill(color)
        
        platform1.draw()
        ball.draw()
        p1.draw(0,0)
        p2.draw(0,0)
        platform2.draw()




    clock.tick(60)#Встановлення кадрів в секунду
    pygame.display.update()#Оновлення екрану
pygame.display.update()#Оновлення екрану
