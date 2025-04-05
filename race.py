from pygame import *
from random import randint
window = display.set_mode((700, 500))
display.set_caption('Гонки')
lost = 0
background = transform.scale(image.load("асфальт.png"), (700,500))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y, player_width, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= 500:
            self.rect.x = randint(50,550)
            self.rect.y = 0
            self.speed = 4
            lost += 1
            
player = GameSprite('машинка.png',0,280,350,100,150)
enemy = Enemy('машинка.png',1,280,500,100,150)
monsters = sprite.Group()
for i in range(2):
    enemy = Enemy('машинка1.png', 4, randint(0,550), 0, 100, 150)
    monsters.add(enemy)
font.init()
font1 = font.SysFont('Arial', 36)
you_lose = font1.render('YOU LOSE!', 1, (255, 67, 50))
clock = time.Clock()
FPS = 60
game = True
finish = False
while game:
    if finish != True:
        window.blit(background, (0,0))
        monsters.update()
        monsters.draw(window)
        player.update()
        player.reset()
        text_lose = font1.render('Объехано: ' + str(lost), 1, (255, 112, 24))
        window.blit(text_lose, (0,0))
        if sprite.spritecollide(player, monsters, False):
            finish = True 
            window.blit(you_lose, (250,200)) 
    display.update()
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_a and player.rect.x > 30:
                player.rect.x += -250
            if e.key == K_d and player.rect.x < 530:
                player.rect.x += 250
    clock.tick(FPS)
