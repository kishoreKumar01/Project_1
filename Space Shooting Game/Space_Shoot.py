import pygame
import random
from os import path
pygame.init()
#Basic initiliazations of screen attributes
width = 600
height = 500
FPS = 60
clock = pygame.time.Clock()
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("GAME")
#Colors :
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)

#Player class and its functions
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,40))
        self.image =  pygame.transform.scale(player_img,(50,40))
        self.image.set_colorkey(black)
        self.radius = 20
        self.rect = self.image.get_rect()
        #pygame.draw.circle(self.image, blue, self.rect.center, self.radius)
        self.rect.centerx = width/2
        self.rect.bottom = height-5
        self.speedx = 8

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= self.speedx
        elif key[pygame.K_RIGHT]:
            self.rect.x += self.speedx
        if self.rect.left < 0:
            self.rect.left = 5
        if self.rect.right > width:
            self.rect.right = width-5

    def fire(self):
        bullet = Bullets(self.rect.centerx,self.rect.top)
        all_sprites.add(bullet)
        all_bullets.add(bullet)

#enemey class and its functions
class Enemey(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image = random.choice(enemey_img)
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.radius = self.rect.width/2
        #pygame.draw.circle(self.image,blue,self.rect.center,self.radius)
        self.rect.x = random.randrange(-50,width+30)
        self.rect.bottom = random.randrange(-100,-30)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        self.rect.left += self.speedx
        if (self.rect.bottom > height+10 or self.rect.left < -30 or self.rect.right > width + 25) :
            self.rect.y = random.randrange(-40,-10)
            self.rect.x = random.randrange(-10, width + 5)
            self.speedy = random.randrange(1,8)

#Bullet class and its function
class Bullets(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,15))
        self.image = bullet_img
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

#load all game graphics
img_path = path.join(path.dirname(__file__),"images")
bg = pygame.image.load(path.join(img_path,"space_bg.png")).convert()
bg_img = bg.get_rect()
player_img = pygame.image.load(path.join(img_path,"playership3_blue.png")).convert()
bullet_img = pygame.image.load(path.join(img_path,"laserBlue.png")).convert()
enemey_img = [pygame.image.load(path.join(img_path,"meteorBrown_med1.png")).convert(),
              pygame.image.load(path.join(img_path,"meteorBrown_med2.png")).convert(),
              pygame.image.load(path.join(img_path,"meteorBrown_small1.png")).convert(),
              pygame.image.load(path.join(img_path,"meteorBrown_small2.png")).convert(),
              pygame.image.load(path.join(img_path,"meteorBrown_tiny1.png")).convert(),
              pygame.image.load(path.join(img_path,"meteorBrown_big1.png")).convert(),
              pygame.image.load(path.join(img_path,"meteorBrown_big2.png")).convert(),
              pygame.image.load(path.join(img_path,"meteorBrown_big3.png")).convert(),
              pygame.image.load(path.join(img_path,"meteorBrown_big4.png")).convert()]


#grouping all sprites
all_sprites = pygame.sprite.Group()
all_enemey = pygame.sprite.Group()
all_bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

for i in range(8):
    enemey = Enemey()
    all_sprites.add(enemey)
    all_enemey.add(enemey)


#check to see if the enemey hits the player
exit = False
#Main loop of the Game
while not exit:
    clock.tick(FPS)
#User Input form keyboard or mouse (EVENTS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.fire()

# Updates
    all_sprites.update()
    hits = pygame.sprite.groupcollide(all_bullets,all_enemey,True,True)
    #redrawig the enemeys afrer shooting them
    for hit in hits:
        enemey = Enemey()
        all_sprites.add(enemey)
        all_enemey.add(enemey)
    hits = pygame.sprite.spritecollide(player, all_enemey,False,pygame.sprite.collide_circle)
    if hits:
        exit = True
#Drawing in window
    win.fill(black)
    win.blit(bg,bg_img)
    all_sprites.draw(win)
    pygame.display.flip()


pygame.quit()
