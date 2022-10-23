#imports
import random
import time
import pygame
import sys
#screen
pygame.init()
screen=pygame.display.set_mode((500,670))
pygame.display.set_caption("cross the road")

#clock
clock=pygame.time.Clock()
fps=60

#pos
posx=234
posy=600
r1y=-375
r2y=0
r3y=375
rs=0.75
cs=0.2
cms=0.75
run=True

#some logic
game=True
font = pygame.font.Font("fonts/AGENCYR.TTF", 32)
font1 = pygame.font.Font("fonts/AGENCYR.TTF", 72)


#load all img

img_c1_l=pygame.image.load("images/vec/car_1_r.png")
img_c1_r=pygame.image.load("images/vec/car_1_l.png")

img_c2_l=pygame.image.load("images/vec/car_2_r.png")
img_c2_r=pygame.image.load("images/vec/car_2_l.png")

img_c3_l=pygame.image.load("images/vec/car_3_r.png")
img_c3_r=pygame.image.load("images/vec/car_3_l.png")

#player class
#it create animation when player moves
#           |
#           V
class player(pygame.sprite.Sprite):
    def __init__(self,speed,cms):
        super().__init__()
        #creating lists for each animation
        self.img_list=[]#->for up animation
        self.img_down_list=[]#->for down animation
        self.img_left_list=[]#->for left animation
        self.img_right_list=[]#->for right animation
        
        self.image1=self.img_list
        self.currentimg=0
        self.starta=False
        self.speed=speed
        
        self.cms=cms
        
        #loading images
        self.img_list.append(pygame.image.load("images/player/up/up1.gif"))
        self.img_list.append(pygame.image.load("images/player/up/up2.gif"))
        self.img_list.append(pygame.image.load("images/player/up/up3.gif"))
        
        #loading images
        self.img_down_list.append(pygame.image.load("images/player/down/down1.gif"))
        self.img_down_list.append(pygame.image.load("images/player/down/down2.gif"))
        self.img_down_list.append(pygame.image.load("images/player/down/down3.gif"))
        
        #loading images
        self.img_left_list.append(pygame.image.load("images/player/left/left1.gif"))
        self.img_left_list.append(pygame.image.load("images/player/left/left2.gif"))
        self.img_left_list.append(pygame.image.load("images/player/left/left3.gif"))

        #loading images
        self.img_right_list.append(pygame.image.load("images/player/right/right1.gif"))
        self.img_right_list.append(pygame.image.load("images/player/right/rigth2.gif"))
        self.img_right_list.append(pygame.image.load("images/player/right/right3.gif"))
        
        #loading images
        self.image=self.image1[int(self.currentimg)]
        self.rect=self.image.get_rect()
        self.rect.topleft=[posx,posy]
    #this function update the animation
    #      |
    #      V
    def update(self):
        global posy,posx
        posy+=self.cms
        if self.starta==True:
            self.currentimg+=self.speed
            if self.currentimg>=len(self.img_down_list):
                self.currentimg=0

        if posx>=476:
            posx=476
        
        if self.rect.x<=0:
            posx=0

        if self.rect.y<=0:
            posy=0

        if keys[pygame.K_UP]:#->> check for any keyboad input
            self.starta=True
            self.image1=self.img_list
            posy-=1.5
       
        elif keys[pygame.K_DOWN]:#->> check for any keyboad input
            self.starta=True
            self.image1=self.img_down_list
            posy+=1.5
       
        elif keys[pygame.K_LEFT]:#->> check for any keyboad input
            self.starta=True
            self.image1=self.img_left_list
            posx-=1.5
       
        elif keys[pygame.K_RIGHT]:#->> check for any keyboad input
            self.starta=True
            self.image1=self.img_right_list
            posx+=1.5
        else :
            self.starta=False
        self.image=self.image1[int(self.currentimg)]
        self.rect.topleft=[posx,posy]

#class for road
#       |
#       v
class road(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y,speed):
        super().__init__()
        self.posy=pos_y
        self.posx=pos_x
        self.speed=speed
        self.rand=0
        self.roads=[]
        self.roads.append(pygame.image.load("images/road_0.png").convert())
        self.image=self.roads[self.rand]
        self.rect=self.image.get_rect(bottomleft=(self.posx,self.posy))        
    def update(self):
        self.posy+=self.speed
        if self.posy>=670+150:
            self.rand=0
            self.image=self.roads[self.rand]
            self.posy=-300

        self.rect=self.image.get_rect(bottomleft=(self.posx,self.posy))

#class forcar hurddle
class car(pygame.sprite.Sprite):
    def __init__(self,imgpath,pos_x,pos_y,type):
        super().__init__()
        self.posx=pos_x
        self.posy=pos_y
        self.type=type
        self.image=imgpath
        self.rect=self.image.get_rect()
        self.rect.topleft=[self.posx,self.posy]
        
    def update(self):
        self.posy+=0.75
        if self.type=="r":
            self.posx+=0.75
            if self.posx>=420:
                self.posx=-50
        
        if self.type=="l":
            self.posx-=0.75
            if self.posx<=0:
                self.posx=500
        if self.posy>=670:
            self.posy=-450
        self.rect.topleft=[self.posx,self.posy]
        

#group of sprite
sprite=pygame.sprite.Group()
sprite_car=pygame.sprite.Group()

#road1
road1=road(0,r1y,rs)
sprite.add(road1)

rand_r1=random.randint(180,250)
car_1_r1_l=car(img_c1_l,0,-525,"r")#formula roady-150
car_2_r1_l=car(img_c2_l,0+rand_r1,-525,"r")

car_3_r1_r=car(img_c3_r,0,-435,"l")
car_4_r1_r=car(img_c1_r,0+rand_r1,-435,"l")

sprite_car.add(car_1_r1_l)
sprite_car.add(car_2_r1_l)

sprite_car.add(car_3_r1_r)
sprite_car.add(car_4_r1_r)

#road2
road2=road(0,r2y,rs)
sprite.add(road2)

car_1_r2_l=car(img_c2_l,0,-150,"r")
car_2_r2_l=car(img_c3_l,0+rand_r1,-150,"r")

car_3_r2_r=car(img_c1_r,420,-60,"l")
car_4_r2_l=car(img_c2_r,420+rand_r1,-60,"l")

sprite_car.add(car_1_r2_l)
sprite_car.add(car_2_r2_l)

sprite_car.add(car_3_r2_r)
sprite_car.add(car_4_r2_l)

#road3
road3=road(0,r3y,rs)
sprite.add(road3)

car_1_r3_l=car(img_c2_l,0,225,"r")
car_2_r3_l=car(img_c1_l,0+rand_r1,225,"r")

car_3_r3_r=car(img_c1_r,420,315,"l")
car_4_r3_l=car(img_c3_r,420+rand_r1,315,"l")

sprite_car.add(car_1_r3_l)
sprite_car.add(car_2_r3_l)

sprite_car.add(car_3_r3_r)
sprite_car.add(car_4_r3_l)

player1=player(cs,cms)
sprite.add(player1)

#score function
def score():
    time1=pygame.time.get_ticks()
    time=int(time1/500)
    return time

while run:
    
    keys=pygame.key.get_pressed()
    
    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
            pygame.quit()
            run=False
    
    score_ply=score()
    screen_txt=font.render("score:"+str(score_ply),True,(255,0,0))
    screen_over=font1.render("Game Over",True,(255,0,0))
    
    cs+=0.001
    rs+=0.001

    if pygame.sprite.spritecollide(player1,sprite_car,False):
        sys.exit()
    if posy>=670:
        screen.blit(screen_over,(178,300))
        sys.exit()

    screen.fill((0,145,0))
    sprite.draw(screen)#->> draw the animation
    sprite_car.draw(screen)
    screen.blit(screen_txt,[0,0])

    sprite.update()
    sprite_car.update()

    pygame.display.update()
    clock.tick(fps)
#end of code