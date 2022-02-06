#from selectors import EpollSelector
from asyncio import selector_events
from urllib.request import ProxyDigestAuthHandler
import pygame
import math
import random

pygame.init()
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Fishing')
screen.fill("lightblue")
mainbg = pygame.transform.scale(pygame.image.load('sprites/startscreen.png').convert_alpha(),(1280,720))
shopbg = pygame.transform.scale(pygame.image.load('sprites/shop.png').convert_alpha(),(1280,1440))
defaultbg = pygame.transform.scale(pygame.image.load('sprites/background.png').convert_alpha(),(1280,720))
moonbg = pygame.transform.scale(pygame.image.load('sprites/moons.png').convert_alpha(),(1280,720))
docksbg = pygame.transform.scale(pygame.image.load('sprites/docks.png').convert_alpha(),(1280,720))
skybg = pygame.transform.scale(pygame.image.load('sprites/sky.png').convert_alpha(),(1280,720))
selectorbg = pygame.transform.scale(pygame.image.load('sprites/selector.png').convert_alpha(),(1280,1440))
lock = pygame.transform.scale(pygame.image.load('sprites/lock.png').convert_alpha(),(1280,360))
start1btn = pygame.transform.scale(pygame.image.load('sprites/start1.png').convert_alpha(),(300,100))
start2btn = pygame.transform.scale(pygame.image.load('sprites/start2.png').convert_alpha(),(300,100))
shop1btn = pygame.transform.scale(pygame.image.load('sprites/shop1.png').convert_alpha(),(300,100))
shop2btn = pygame.transform.scale(pygame.image.load('sprites/shop2.png').convert_alpha(),(300,100))
wave = pygame.transform.scale(pygame.image.load('sprites/wave.png').convert_alpha(),(2000,700))
cloud = pygame.transform.scale(pygame.image.load('sprites/cloud.png').convert_alpha(),(2500,250))
startbear = pygame.transform.scale(pygame.image.load('sprites/startscreenbear.png').convert_alpha(),(1280,720))
fasterreload1 = pygame.transform.scale(pygame.image.load('sprites/fasterreload1.png').convert_alpha(),(70,70))
fasterreload2 = pygame.transform.scale(pygame.image.load('sprites/fasterreload2.png').convert_alpha(),(70,70))
moredmg1 = pygame.transform.scale(pygame.image.load('sprites/moredmg1.png').convert_alpha(),(70,70))
moredmg2 = pygame.transform.scale(pygame.image.load('sprites/moredmg2.png').convert_alpha(),(70,70))
tripspear1 = pygame.transform.scale(pygame.image.load('sprites/tripspear1.png').convert_alpha(),(70,70))
tripspear2 = pygame.transform.scale(pygame.image.load('sprites/tripspear2.png').convert_alpha(),(70,70))
bear = pygame.transform.scale(pygame.image.load('sprites/bear.png').convert_alpha(),(120,120))
menus = pygame.transform.scale(pygame.image.load('sprites/menu.png').convert_alpha(),(30,30))
ssprite = pygame.transform.scale(pygame.image.load('sprites/spear.png').convert_alpha(),(24,50))
spearlevel = ['sprites/spear.png','sprites/spear1.png','sprites/spear2.png','sprites/spear3.png','sprites/spear4.png','sprites/out.png']
tanklevel = ['too lazy to change code here','sprites/tank1.png','sprites/tank2.png','sprites/tank3.png','sprites/tank4.png','sprites/out.png']
price = [0,1000,10000,100000,1000000,0]
unlock = [True,False,False,False]
spears = []
fishes = []
collided = []
pygame.mixer.music.set_volume(1)
pygame.mixer.music.load("sprites/click.mp3")
FPS = 60

#gameplay settings


'''class fish:52

    def __init__(self,x,y):
        #self.hit = pygame.Rect()'''
def crash(x,y):
    #global collided
    if [x,y] in collided:
        return False
    elif x.hit.colliderect(y.hit):
        collided.append([x,y])
        return True
    else:
        return False
Run = True
temp = None

def game(bg,fish1,fish2,fish3,hp1,hp2,hp3,val1,val2,val3,max1,max2,max3,size1,size2,size3,posy,grav):
    #fishes = []
    #spears = []
    global Run,clock,clicking ,velo ,score ,counter ,reload,money ,gravity ,semiauto ,spearhp ,fishhp ,temprect,time,speardmg ,home,fastreload ,font ,font1 ,font2 ,startanimate,fastreloadcooldown,moredmgcooldown,moredmg,tripspearcooldown,tripspear,slevel,tlevel,tripnum,reloadnum,dmgnum,bear
    gravity = 0
    while(Run and counter < time*60*FPS and home):
        if int(time*60-math.floor(counter/60)) == 20:
            pygame.mixer.music.load("sprites/tick.mp3")
            pygame.mixer.music.play()
            #pygame.mixer.music.load("sprites/click.mp3")
        #print(speardmg)
        pygame.display.update()
        #counter = counter%(FPS*1000)
        clock.tick(FPS)
        screen.blit(bg,(0,0))
        scoretxt = font.render(str(score), True, (255,255,0))
        timetxt = font.render("Time: "+str(int(time*60-math.floor(counter/60))), True, (0,255,0))
        screen.blit(pygame.transform.scale(pygame.image.load('sprites/coin.png').convert_alpha(),(30,30)),(40,0))
        screen.blit(scoretxt,(75,0))
        screen.blit(timetxt,(1105,0))
        screen.blit(fasterreload1,(1210,650))
        screen.blit(moredmg1,(1140,650))
        screen.blit(tripspear1,(1070,650))
        screen.blit(menus,(0,0))

        triptext = font2.render(str(tripnum), True, (255,0,0))
        screen.blit(triptext,(1080,658))
        dmgtext = font2.render(str(dmgnum), True, (255,0,0))
        screen.blit(dmgtext,(1150,658))
        retext = font2.render(str(reloadnum), True, (255,0,0))
        screen.blit(retext,(1220,658))


        if 1280 >= pygame.mouse.get_pos()[0] >= 1210 and 720 >= pygame.mouse.get_pos()[1] >= 650:
            screen.blit(fasterreload2,(1210,650))
        if 1210 >= pygame.mouse.get_pos()[0] >= 1140 and 720 >= pygame.mouse.get_pos()[1] >= 650:
            screen.blit(moredmg2,(1140,650))
        if 1140 >= pygame.mouse.get_pos()[0] >= 1070 and 720 >= pygame.mouse.get_pos()[1] >= 650:
            screen.blit(tripspear2,(1070,650))
        if clicking and counter%reload == 0:
            #spears.append(spear(pygame.mouse.get_pos()[0]-12,pygame.mouse.get_pos()[1]))
            spears.append(spear(70,posy,pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]))
            if tripspear:
                spears.append(spear(70,posy,pygame.mouse.get_pos()[0]*1.5,pygame.mouse.get_pos()[1]))
                spears.append(spear(70,posy,pygame.mouse.get_pos()[0],720-(720-pygame.mouse.get_pos()[1])*1.5))
            semiauto+=1
        if not fastreload:
            fastreloadcooldown = counter
        if not moredmg :
            moredmgcooldown = counter
        if not tripspear :
            tripspearcooldown = counter
        if counter-fastreloadcooldown >= 300:
            fastreloadcooldown = counter
            fastreload = False
            reload *= 5
        if counter-moredmgcooldown >= 300:
            moredmgcooldown = counter
            moredmg = False
            speardmg /= 5
        if counter-tripspearcooldown >= 300:
            tripspearcooldown = counter
            tripspear = False
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                Run = False
            screen.blit(menus,(0,0))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 30 >= pygame.mouse.get_pos()[0] >= 0 and 30 >= pygame.mouse.get_pos()[1] >= 0:
                pygame.mixer.music.load("sprites/click.mp3")
                pygame.mixer.music.play()
                while (Run and home):
                    pygame.display.update()
                    clock.tick(FPS)
                    screen.blit(pygame.transform.scale(pygame.image.load('sprites/Continue1.png').convert_alpha(),(250,70)),(509,270))
                    screen.blit(pygame.transform.scale(pygame.image.load('sprites/home1.png').convert_alpha(),(250,70)),(509,350))
                    if 760 >= pygame.mouse.get_pos()[0] >= 507 and 335 >= pygame.mouse.get_pos()[1] >= 267:
                        screen.blit(pygame.transform.scale(pygame.image.load('sprites/Continue2.png').convert_alpha(),(250,70)),(509,270))
                    if 760 >= pygame.mouse.get_pos()[0] >= 507 and 415 >= pygame.mouse.get_pos()[1] >= 347:
                        screen.blit(pygame.transform.scale(pygame.image.load('sprites/home2.png').convert_alpha(),(250,70)),(509,350))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            Run = False
                            break
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 760 >= pygame.mouse.get_pos()[0] >= 507 and 335 >= pygame.mouse.get_pos()[1] >= 267:#760 >= pygame.mouse.get_pos()[0] >= 510 and 355 >= pygame.mouse.get_pos()[0] >= 295:
                            pygame.mixer.music.load("sprites/click.mp3")
                            pygame.mixer.music.play()
                            home = False
                            temp = True
                            break
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 760 >= pygame.mouse.get_pos()[0] >= 507 and 415 >= pygame.mouse.get_pos()[1] >= 347:#760 >= pygame.mouse.get_pos()[0] >= 510 and 355 >= pygame.mouse.get_pos()[0] >= 295:
                            pygame.mixer.music.load("sprites/click.mp3")
                            pygame.mixer.music.play()
                            home = False
                            temp = False
                            break

                home = temp
                if not temp:
                    break
            if reloadnum > 0 and not fastreload and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 1280 >= pygame.mouse.get_pos()[0] >= 1210 and 720 >= pygame.mouse.get_pos()[1] >= 650:
                pygame.mixer.music.load("sprites/click.mp3")
                pygame.mixer.music.play()
                reloadnum-=1
                fastreload = True
                reload /= 5
                reload = math.ceil(reload)
                fastreloadcooldown = counter
            if dmgnum > 0 and not moredmg and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 1210 >= pygame.mouse.get_pos()[0] >= 1140 and 720 >= pygame.mouse.get_pos()[1] >= 650:
                pygame.mixer.music.load("sprites/click.mp3")
                pygame.mixer.music.play()
                dmgnum-=1
                moredmg = True
                speardmg *= 5
                moredmgcooldown = counter
            if tripnum > 0 and not tripspear and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 1140 >= pygame.mouse.get_pos()[0] >= 1070 and 720 >= pygame.mouse.get_pos()[1] >= 650:
                pygame.mixer.music.load("sprites/click.mp3")
                pygame.mixer.music.play()
                tripspear = True
                tripspearcooldown = counter
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not clicking:
                clicking = True
                if semiauto == 0: # pygame.mouse.get_pressed()[0]:
                    semiauto+=FPS/reload
                #print('yes',clicking)
                #pygame.draw.circle(screen,"red",pygame.mouse.get_pos(),10)
                #spears.append(spear(pygame.mouse.get_pos()[0]-12,pygame.mouse.get_pos()[1]))
                    spears.append(spear(70,posy,pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]))
                    if tripspear:
                        spears.append(spear(70,posy,pygame.mouse.get_pos()[0]*1.5,pygame.mouse.get_pos()[1]))
                        spears.append(spear(70,posy,pygame.mouse.get_pos()[0],720-(720-pygame.mouse.get_pos()[1])*1.5))
            if event.type == pygame.MOUSEBUTTONUP:
                semiauto+=1
                clicking = False
        if counter%60== 0:
            for i in range(random.randint(0,3)):
                temp = random.randint(0,6)
                if 0 <= temp <= 3:
                    fishes.append(fish(random.randint(200,1200),random.randint(0,500),size1,val1,max1,fish1,hp1))
                elif 3 < temp <= 5:
                    fishes.append(fish(random.randint(200,1200),random.randint(0,500),size2,val2,max2,fish2,hp2))
                else:
                    fishes.append(fish(random.randint(200,1200),random.randint(0,500),size3,val3,max3,fish3,hp3))
        
        for i in collided:
            if i[0].dead or i[1].dead:
                collided.remove(i)
        for Spear in spears:
            if Spear.dead:
                spears.remove(Spear)
            else:
                Spear.move()

        for Fish in fishes:
            if Fish.dead:
                fishes.remove(Fish)
            else:
                Fish.move()

            #print(spears)
        counter+=1
        semiauto = semiauto%reload
        try:
            bear = pygame.transform.rotate(bear,math.atan((520-pygame.mouse.get_pos()[1])/(pygame.mouse.get_pos()[0]+1))*(180)/3.1415926535897932384)
            #bear = pygame.transform.rotate(bear,90)
            #print(math.atan(520-pygame.mouse.get_pos()[1]/pygame.mouse.get_pos()[0]+1)*(180)/3.1415926535897932384)
            screen.blit(bear,(0,posy-80))
            bear = pygame.transform.scale(pygame.image.load('sprites/bear.png').convert_alpha(),(120,120))
        except:
            bear = pygame.transform.rotate(bear,90)
            #bear = pygame.transform.rotate(bear,90)
            #print(math.atan(520-pygame.mouse.get_pos()[1]/pygame.mouse.get_pos()[0]+1)*(180)/3.1415926535897932384)
            screen.blit(bear,(0,posy-80))
            bear = pygame.transform.scale(pygame.image.load('sprites/bear.png').convert_alpha(),(120,120))
    
    while(Run and home):
        pygame.display.update()
        clock.tick(FPS)
        screen.blit(bg,(0,0))
        scoretxt = font1.render("You Made "+str(score), True, (0,255,0))
        #pygame.draw.rect(screen,"red",temprect)
        screen.blit(pygame.transform.scale(pygame.image.load('sprites/Continue1.png').convert_alpha(),(250,70)),(509,290))
        if 760 >= pygame.mouse.get_pos()[0] >= 507 and 355 >= pygame.mouse.get_pos()[1] >= 287:
            screen.blit(pygame.transform.scale(pygame.image.load('sprites/Continue2.png').convert_alpha(),(250,70)),(509,290))
        screen.blit(pygame.transform.scale(pygame.image.load('sprites/coin.png').convert_alpha(),(50,50)),(720+30*len(str(score)),197))
        screen.blit(scoretxt,(460,200))
        #scoretxt = font1.render("Continue", True, (255,255,255))
        #screen.blit(scoretxt,(520,300))
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 760 >= pygame.mouse.get_pos()[0] >= 507 and 355 >= pygame.mouse.get_pos()[1] >= 287:#760 >= pygame.mouse.get_pos()[0] >= 510 and 355 >= pygame.mouse.get_pos()[0] >= 295:
                pygame.mixer.music.load("sprites/click.mp3")
                pygame.mixer.music.play()
                home = False
                break





class fish:
    def __init__(self,x,y,size,value,maxspeed,sprite,hp):
        self.posx = x
        self.posy = y
        self.size = size
        self.hit = pygame.Rect(x,y,size[0],size[1])
        self.velo = [(-1)**random.randint(1,2)*random.randint(1,maxspeed),random.randint(-1*maxspeed,maxspeed)]
        self.dead = False
        self.maxspeed = maxspeed
        self.sprite = pygame.transform.scale(pygame.image.load(sprite).convert_alpha(),(size[0],size[1]))
        if self.velo[0] < 0:
            self.sprite = pygame.transform.flip(self.sprite,1,0)
            #self.sprite = pygame.transform.rotate(self.sprite,180/math.pi*math.atan(self.velo[1]/self.velo[0]))
        self.health = hp
        self.value = value
        #screen.blit
    
    def move(self):
        global score, money
        self.posx += self.velo[0]
        self.posy += self.velo[1]
        '''if self.posy < 400 and self.sprite == pygame.transform.scale(pygame.image.load('sprites/puffer1.png').convert_alpha(),(self.size[0],self.size[1])):
            self.sprite = pygame.transform.scale(pygame.image.load('sprites/puffer2.png').convert_alpha(),(self.size[0],self.size[1]))
        elif self.posy >= 400 and self.sprite == pygame.transform.scale(pygame.image.load('sprites/puffer2.png').convert_alpha(),(self.size[0],self.size[1])):
            self.sprite = pygame.transform.scale(pygame.image.load('sprites/puffer1.png').convert_alpha(),(self.size[0],self.size[1]))
        '''
        if counter%(60*random.randint(1,3))==0:
            
            #print(math.atan(self.velo[1]/self.velo[0]))
            #self.velo = [random.randint(-5,5),random.randint(-5,5)]
            if self.velo[0] < 0:
                self.velo = [(-1)**random.randint(1,2)*random.randint(1,self.maxspeed),random.randint(-1*self.maxspeed,self.maxspeed)]
                if self.velo[0] > 0:
                    self.sprite = pygame.transform.flip(self.sprite,1,0)

            else:
                self.velo = [(-1)**random.randint(1,2)*random.randint(1,self.maxspeed),random.randint(-1*self.maxspeed,self.maxspeed)]
                self.sprite = pygame.transform.rotate(self.sprite,math.atan(self.velo[1]/self.velo[0]))
                if self.velo[0] < 0:
                    self.sprite = pygame.transform.flip(self.sprite,1,0)
        self.hit = pygame.Rect(self.posx-2*self.velo[0],self.posy-2*self.velo[1],self.size[0],self.size[1])
        #pygame.draw.rect(screen,'green',self.hit)
        screen.blit(self.sprite,(self.posx-2*self.velo[0],self.posy-2*self.velo[1]))
        if self.posy > 720 or self.posy < -100 or self.posx < -100 or self.posx > 1280:
            self.dead = True
            #print("hello")
        for Spear in spears:
            if crash(self,Spear):
                self.health-=Spear.dmg
                if self.health <= 0:
                    self.dead = True
                    score+= self.value
                    money+= self.value
                break
        if self.health <= 0:
            self.dead = True
        
        #pygame.Rect((500,200,10,10))
        #screen.blit



class spear:
    def __init__(self,x,y,mousex,mousey):
        #global sspear
        print(mousex)
        if mousex < 70:
            mousex = 71
        print(mousex)
        self.hit = pygame.Rect(x+12,y+30,15,15)
        self.posx = x
        self.posy = y
        self.health = spearhp
        self.dmg = speardmg
        self.mousex = mousex
        self.mousey = mousey
        temp1 = mousex+1-self.posx
        temp2 = self.posy-mousey
        temp3 = (temp1**2+temp2**2)**(1/2)
        self.velo = [velo*temp1/temp3,velo*temp2/temp3]
        #self.velo = [10,10*temp2/temp1]
        #self.velo = [(600-pygame.mouse.get_pos()[1])/pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[0]/(600-pygame.mouse.get_pos()[1])]
        #pygame.mouse.get_pos()[0]-12,pygame.mouse.get_pos()[1]
        if temp1 == 0:
            self.ang = 0
        else:
            self.ang = -90+math.atan(temp2/temp1)*(180)/3.1415926535897932384
        self.dead = False
        self.sprite = ssprite
        self.sprite = pygame.transform.rotate(self.sprite,self.ang)
        self.posx -= self.velo[0]
        self.posy += self.velo[1]
        #print(temp1,temp2,temp3)
    
    def move(self):
        temp1 = self.mousex+1
        temp2 = 600-self.mousey
        self.posx += self.velo[0]
        self.posy -= self.velo[1]
        hitbox = (self.posx+self.velo[0]+3-10*(math.sin((-1*self.ang)*math.pi/180)),self.posy-2*self.velo[1]+5+3*(math.cos((-1*self.ang)*math.pi/180)),15,15)
        self.hit = pygame.Rect(hitbox)
        #self.sprite = pygame.transform.rotate(self.sprite,self.ang)#math.atan(self.velo[1]/self.velo[0]))
        self.velo[1] -= gravity
        #self.velo[0] -= 0.1
        #self.ang -= 0.1
        #screen.fill('lightblue')
        #if -0.25<= self.velo[1]: #< 0.25:
            #self.sprite = pygame.transform.rotate(self.sprite,-90-math.``````atan(temp2/temp1)*(180)/3.14159265358979323840)
        #self.sprite = pygame.transform.rotate(self.sprite,(-2)*math.atan(temp2/temp1)*(180)/3.14159265358979323840)
            #self.sprite = pygame.transform.rotate(self.sprite,+359)
        #    print(abs((math.atan((self.velo[1])/self.velo[0])*(180)/3.1415926535897932384))-90,self.velo)
        #print(math.cos((-1*self.ang)*math.pi/180))
        screen.blit(self.sprite,(self.posx-2*self.velo[0],self.posy-2*self.velo[1]))
        #pygame.draw.rect(screen,'blue',hitbox)
        #pygame.draw.rect(screen,"yellow",(self.posx,self.posy,10,10))
        #pygame.draw.rect(screen,'green',(self.posx+30,self.posy+12,10,10))
        if self.posy > 720 or self.posx < -100 or self.posx > 1280 or self.posy < -100:
            self.dead = True
        for Fish in fishes:
            if crash(self,Fish):
                self.health-=1
                break
                
        if self.health <= 0:
            self.dead = True
        #else:
        #    pygame.display.update()
        #    pygame.time.delay(100)
        #    self.move()


Run = True
clock = pygame.time.Clock()
clicking = False
velo = 15
score = 0
counter = 0
reload = 10
money = 10000000000
gravity = 0
semiauto = 0
spearhp = 1
fishhp = 5
temprect = pygame.Rect((510,294,250,60))
#score = 0
time = 0.5
speardmg = 1
home = False
fastreload = False
font = pygame.font.Font("freesansbold.ttf", 37)
font1 = pygame.font.Font("freesansbold.ttf", 50)
font2 = pygame.font.Font("freesansbold.ttf", 10)
startanimate = 0
fastreloadcooldown = counter
moredmgcooldown = counter
moredmg = False
tripspearcooldown = counter
tripspear = False
slevel = 0
tlevel = 0
tripnum = 0
reloadnum = 0
dmgnum = 0
#text = font.render("Score:"+str(score)+"Time:", True, (0,0,0))

while (Run):
    if home == False:
        Run = True
        clock = pygame.time.Clock()
        clicking = False
        velo = 15
        score = 0
        counter = 0
        reload = 10-slevel
        #money = 100000000000
        gravity = 0
        semiauto = 0
        fishhp = 5
        temprect = pygame.Rect((510,294,250,60))
        score = 0
        home = True
        fastreload = False
        font = pygame.font.Font("freesansbold.ttf", 37)
        font1 = pygame.font.Font("freesansbold.ttf", 50)
        startanimate = 0
        fastreloadcooldown = counter
        moredmgcooldown = counter
        tripspearcooldown = counter
        tripspear = False
        moredmg = False
        collided.clear()
        fishes.clear()
        spears.clear()
    startanimate += 1
    startanimate = startanimate%179
    counter = 0
    pygame.display.update()
    #counter = counter%(FPS*1000)
    clock.tick(FPS)
    screen.blit((mainbg),(0,0))
    screen.blit((cloud),(-startanimate*7.33,0))
    screen.blit((startbear),(0,0))
    screen.blit((wave),(0,20+10*math.sin(startanimate*math.pi/180)))
    screen.blit((wave),(-100,20+10*math.cos((startanimate+90)*math.pi/180)))
    screen.blit((start1btn),(505,200))
    screen.blit((shop1btn),(505,310))
    
    if 805 >= pygame.mouse.get_pos()[0] >= 505 and 300 >= pygame.mouse.get_pos()[1] >= 200:
        screen.blit((start2btn),(505,200))
    if 805 >= pygame.mouse.get_pos()[0] >= 505 and 410 >= pygame.mouse.get_pos()[1] >= 310:
        screen.blit((shop2btn),(505,310))
    #reload -= 0.000000000000001
    #pygame.display.update()
    #counter = counter%(FPS*1000)
    #clock.tick(FPS)
    #screen.blit(bg,(0,0))
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            Run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 805 >= pygame.mouse.get_pos()[0] >= 505 and 410 >= pygame.mouse.get_pos()[1] >= 310:
            pygame.mixer.music.load("sprites/click.mp3")
            pygame.mixer.music.play()
            home = True
            y = 0
            while(Run and home):
                pygame.display.update()
                clock.tick(FPS)
                screen.blit(shopbg,(0,y))
                screen.blit(pygame.transform.rotate(pygame.transform.scale(pygame.image.load(spearlevel[slevel+1]).convert_alpha(),(196,800)),90),(230,y+90))
                screen.blit(menus,(0,0))
                moneytxt = font.render(str(money), True, (255,255,0))
                screen.blit(pygame.transform.scale(pygame.image.load('sprites/coin.png').convert_alpha(),(30,30)),(40,0))
                screen.blit(moneytxt,(75,0))
                if money >= price[slevel+1] and slevel<4:
                    screen.blit(pygame.transform.scale(pygame.image.load('sprites/blankgreen.png').convert_alpha(),(400,100)),(450,260+y))
                else:
                    screen.blit(pygame.transform.scale(pygame.image.load('sprites/blankred.png').convert_alpha(),(400,100)),(450,260+y))
                if slevel < 4:
                    costtxt = font1.render(str(price[slevel+1]), True, (255,255,0))
                    screen.blit(costtxt,(590-slevel*14,290+y))
                
                screen.blit(pygame.transform.rotate(pygame.transform.scale(pygame.image.load(tanklevel[tlevel+1]).convert_alpha(),(150,600)),90),(350,y+475))
                if money >= price[tlevel+1] and tlevel<4:
                    screen.blit(pygame.transform.scale(pygame.image.load('sprites/blankgreen.png').convert_alpha(),(400,100)),(450,625+y))
                else:
                    screen.blit(pygame.transform.scale(pygame.image.load('sprites/blankred.png').convert_alpha(),(400,100)),(450,625+y))
                if tlevel < 4:
                    costtxt = font1.render(str(price[tlevel+1]), True, (255,255,0))
                    screen.blit(costtxt,(590-tlevel*14,655+y))   
            
                #screen.blit(pygame.transform.rotate(pygame.transform.scale(pygame.image.load(tanklevel[tlevel+1]).convert_alpha(),(150,600)),90),(350,y+475))
                if money >= 200:
                    screen.blit(pygame.transform.scale(pygame.image.load('sprites/blankgreen.png').convert_alpha(),(100,25)),(590,1045+y))
                else:
                    screen.blit(pygame.transform.scale(pygame.image.load('sprites/blankred.png').convert_alpha(),(100,25)),(590,1045+y))
                
                if money >= 200:
                    screen.blit(pygame.transform.scale(pygame.image.load('sprites/blankgreen.png').convert_alpha(),(100,25)),(265,1045+y))
                else:
                    screen.blit(pygame.transform.scale(pygame.image.load('sprites/blankred.png').convert_alpha(),(100,25)),(265,1045+y))
                
                if money >= 300:
                    screen.blit(pygame.transform.scale(pygame.image.load('sprites/blankgreen.png').convert_alpha(),(100,25)),(915,1045+y))
                else:
                    screen.blit(pygame.transform.scale(pygame.image.load('sprites/blankred.png').convert_alpha(),(100,25)),(915,1045+y))
                
                triptext = font.render(str(tripnum), True, (0,0,0))
                screen.blit(triptext,(210,840+y))
                dmgtext = font.render(str(dmgnum), True, (0,0,0))
                screen.blit(dmgtext,(530,840+y))
                retext = font.render(str(reloadnum), True, (0,0,0))
                screen.blit(retext,(850,840+y))


                for event in pygame.event.get():    
                    if event.type == pygame.QUIT:
                        Run = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 4:
                            y+= 30
                            y = min(y,0)
                        elif event.button == 5:
                            y-= 30
                            y = max(y,-720)
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 850 >= pygame.mouse.get_pos()[0] >= 450 and 360+y >= pygame.mouse.get_pos()[1] >= 260+y:
                        #print(slevel)
                        pygame.mixer.music.load("sprites/click.mp3")
                        pygame.mixer.music.play()
                        if slevel < 4 and money>=price[slevel+1]:
                            money-=price[tlevel+1]
                            speardmg+=1
                            spearhp+=1
                            reload-=1
                            slevel+=1
                            ssprite = pygame.transform.scale(pygame.image.load(spearlevel[slevel]).convert_alpha(),(24,50))
                        #if slevel == 3 and money>price[slevel+1]:

                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 850 >= pygame.mouse.get_pos()[0] >= 450 and 725+y >= pygame.mouse.get_pos()[1] >= 625+y:
                        #print(slevel)
                        pygame.mixer.music.load("sprites/click.mp3")
                        pygame.mixer.music.play()
                        if tlevel < 4 and money>=price[tlevel+1]:
                            money-=price[tlevel+1]
                            time+=1
                            tlevel+=1
                            #ssprite = pygame.transform.scale(pygame.image.load(spearlevel[slevel]).convert_alpha(),(24,50))
                            #    slevel+=1
                        #    ssprite = pygame.transform.scale(pygame.image.load(spearlevel[slevel]).convert_alpha(),(24,50))
                    
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 365 >= pygame.mouse.get_pos()[0] >= 265 and 1070+y >= pygame.mouse.get_pos()[1] >= 1045+y:
                        pygame.mixer.music.load("sprites/click.mp3")
                        pygame.mixer.music.play()
                        if money >= 200:
                            tripnum+=1
                            money-=200
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 690 >= pygame.mouse.get_pos()[0] >= 590 and 1070+y >= pygame.mouse.get_pos()[1] >= 1045+y:
                        pygame.mixer.music.load("sprites/click.mp3")
                        pygame.mixer.music.play()
                        if money >= 200:
                            dmgnum+=1
                            money-=200
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 1015 >= pygame.mouse.get_pos()[0] >= 915 and 1070+y >= pygame.mouse.get_pos()[1] >= 1045+y:
                        pygame.mixer.music.load("sprites/click.mp3")
                        pygame.mixer.music.play()
                        if money >= 300:
                            reloadnum+=1
                            money-=300
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 30 >= pygame.mouse.get_pos()[0] >= 0 and 30 >= pygame.mouse.get_pos()[1] >= 0:
                        pygame.mixer.music.load("sprites/click.mp3")
                        pygame.mixer.music.play()
                        while (Run and home):
                            pygame.display.update()
                            clock.tick(FPS)
                            screen.blit(pygame.transform.scale(pygame.image.load('sprites/Continue1.png').convert_alpha(),(250,70)),(509,270))
                            screen.blit(pygame.transform.scale(pygame.image.load('sprites/home1.png').convert_alpha(),(250,70)),(509,350))
                            if 760 >= pygame.mouse.get_pos()[0] >= 507 and 335 >= pygame.mouse.get_pos()[1] >= 267:
                                screen.blit(pygame.transform.scale(pygame.image.load('sprites/Continue2.png').convert_alpha(),(250,70)),(509,270))
                            if 760 >= pygame.mouse.get_pos()[0] >= 507 and 415 >= pygame.mouse.get_pos()[1] >= 347:
                                screen.blit(pygame.transform.scale(pygame.image.load('sprites/home2.png').convert_alpha(),(250,70)),(509,350))
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    Run = False
                                    break
                                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 760 >= pygame.mouse.get_pos()[0] >= 507 and 335 >= pygame.mouse.get_pos()[1] >= 267:#760 >= pygame.mouse.get_pos()[0] >= 510 and 355 >= pygame.mouse.get_pos()[0] >= 295:
                                    pygame.mixer.music.load("sprites/click.mp3")
                                    pygame.mixer.music.play()
                                    home = False
                                    temp = True
                                    break
                                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 760 >= pygame.mouse.get_pos()[0] >= 507 and 415 >= pygame.mouse.get_pos()[1] >= 347:#760 >= pygame.mouse.get_pos()[0] >= 510 and 355 >= pygame.mouse.get_pos()[0] >= 295:
                                    pygame.mixer.music.load("sprites/click.mp3")
                                    pygame.mixer.music.play()
                                    home = False
                                    temp = False
                                    break

                        home = temp
                        if not temp:
                            break        
                    

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 805 >= pygame.mouse.get_pos()[0] >= 505 and 300 >= pygame.mouse.get_pos()[1] >= 200:
            pygame.mixer.music.load("sprites/click.mp3")
            pygame.mixer.music.play()
            home = True
            y = 0
            while(Run and home):
                pygame.display.update()
                counter = counter%(FPS*1000)
                clock.tick(FPS)
                screen.blit(selectorbg,(0,0+y))
                screen.blit(menus,(0,0))
                for i in range(4):
                    if not unlock[i]:
                        screen.blit(lock,(0,360*i+y))
                        costtxt = font1.render(str(1000*i), True, (255,255,0))
                        screen.blit(costtxt,(570,360*i+200+y))
                for event in pygame.event.get():

                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 30 >= pygame.mouse.get_pos()[0] >= 0 and 30 >= pygame.mouse.get_pos()[1] >= 0:
                        pygame.mixer.music.load("sprites/click.mp3")
                        pygame.mixer.music.play()
                        while (Run and home):
                            pygame.display.update()
                            clock.tick(FPS)
                            screen.blit(pygame.transform.scale(pygame.image.load('sprites/Continue1.png').convert_alpha(),(250,70)),(509,270))
                            screen.blit(pygame.transform.scale(pygame.image.load('sprites/home1.png').convert_alpha(),(250,70)),(509,350))
                            if 760 >= pygame.mouse.get_pos()[0] >= 507 and 335 >= pygame.mouse.get_pos()[1] >= 267:
                                screen.blit(pygame.transform.scale(pygame.image.load('sprites/Continue2.png').convert_alpha(),(250,70)),(509,270))
                            if 760 >= pygame.mouse.get_pos()[0] >= 507 and 415 >= pygame.mouse.get_pos()[1] >= 347:
                                screen.blit(pygame.transform.scale(pygame.image.load('sprites/home2.png').convert_alpha(),(250,70)),(509,350))
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    Run = False
                                    break
                                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 760 >= pygame.mouse.get_pos()[0] >= 507 and 335 >= pygame.mouse.get_pos()[1] >= 267:#760 >= pygame.mouse.get_pos()[0] >= 510 and 355 >= pygame.mouse.get_pos()[0] >= 295:
                                    pygame.mixer.music.load("sprites/click.mp3")
                                    pygame.mixer.music.play()
                                    home = False
                                    temp = True
                                    break
                                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 760 >= pygame.mouse.get_pos()[0] >= 507 and 415 >= pygame.mouse.get_pos()[1] >= 347:#760 >= pygame.mouse.get_pos()[0] >= 510 and 355 >= pygame.mouse.get_pos()[0] >= 295:
                                    pygame.mixer.music.load("sprites/click.mp3")
                                    pygame.mixer.music.play()
                                    home = False
                                    temp = False
                                    break

                        home = temp
                        if not temp:
                            break
                        break

                    if event.type == pygame.QUIT:
                        Run = False
                    if event.type == pygame.MOUSEBUTTONDOWN :
                        if event.button == 4:
                            y+= 30
                            y = min(y,0)
                        elif event.button == 5:
                            y-= 30
                            y = max(y,-720)
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        pygame.mixer.music.load("sprites/click.mp3")
                        pygame.mixer.music.play()

                        if 360+y >= pygame.mouse.get_pos()[1] >= 0+y:
                            game(defaultbg,'sprites/fish4.png','sprites/fish3.png','sprites/fish1.png',1,3,5,10,30,50,2,3,5,(50,20),(120,40),(200,60),600,-0.1)
                        elif 720+y >= pygame.mouse.get_pos()[1] >= 360+y:
                            if unlock[1]:
                                game(docksbg,'sprites/fish3.png','sprites/puffer2.png','sprites/seagull.png',3,7,5,30,70,50,3,4,7,(120,40),(120,120),(120,40),300,0.1)
                            else:
                                if money>=1000:
                                    money-=1000
                                    unlock[1] = True
                        elif 1080+y >= pygame.mouse.get_pos()[1] >= 720+y:
                            if unlock[2]:
                                game(skybg,'sprites/pigeon.png','sprites/rooster.png','sprites/eagle.png',10,20,30,100,100,300,5,3,10,(120,40),(120,40),(200,60),600,0)
                            else:
                                if money>=2000:
                                    money-=2000
                                    unlock[2] = True
                        else:
                            if unlock[3]:
                                game(moonbg,'sprites/fish5.png','sprites/elephant.png','sprites/rocket.png',20,40,100,200,400,1000,10,5,10,(60,20),(120,120),(400,120),600,0)
                            else:
                                if money>=3000:
                                    money-=3000
                                    unlock[3] = True
                
            
                    #print(pygame.mouse.get_pos())
            #print(len(fishes))
            #print(semiauto)
            #print(score)
            #if 
        #print(pygame.font.get_fonts())
pygame.quit()
