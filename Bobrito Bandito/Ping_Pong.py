from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Пинг понг')
window.fill((200, 255, 255))

clock = time.Clock()
FPS = 60

keys_pressed = key.get_pressed()

font.init()
font1 = font.SysFont('Arial', 128)

speed_x = 3
speed_y = 3

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        # self.size_x = size_x
        # self.size_y = size_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()    
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()    
        if keys_pressed[K_i] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_k] and self.rect.y < 400:
            self.rect.y += self.speed

sprite_player1 = Player1(('roketo.jpg'), 0, 250, 60, 100, 5)
sprite_player2 = Player2(('roketo.jpg'), 640, 250, 60, 100, 5)
sprite_ball = GameSprite(('myach.jpg'), 350, 200, 60, 100, 5)

game = True
finish = False


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        if sprite_ball.rect.y > 400 or sprite_ball.rect.y < 0:
            speed_y *= -1

        if sprite_ball.rect.x < 0:
            text_1 = font1.render('PLAYER 1 LOSE!', True, (255, 0, 0))
            window.blit(text_1, (250, 250))
            finish = True
        elif sprite_ball.rect.x > 640:
            text_2 = font1.render('PLAYER 2 LOSE!', True, (0, 255, 0))
            window.blit(text_2, (250, 250))
            finish = True

        window.fill((200, 255, 255))
        sprite_player1.update()
        sprite_player2.update()        
        sprite_ball.rect.x += speed_x
        sprite_ball.rect.y += speed_y
        if sprite.collide_rect(sprite_player1, sprite_ball) or sprite.collide_rect(sprite_player2, sprite_ball):
            speed_x *= -1


        sprite_ball.reset()
        sprite_player1.reset()
        sprite_player2.reset()
    clock.tick(FPS)
    display.update()



# from pygame import *
# from random import *
# from time import time as timer

# window = display.set_mode((700, 500))
# display.set_caption('Шутер')
# galaxy = transform.scale(image.load('galaxy.jpg'), (700, 500))

# clock = time.Clock()

# keys_pressed = key.get_pressed()

# mixer.init()

# mixer.music.load('space.ogg')
# mixer.music.load('fire.ogg')
# fire_sound = mixer.Sound('fire.ogg')
# mixer.music.play()

# FPS = 60

# lost = 0
# score = 0
# hp = 3
# num_fire = 0
# font.init()
# font1 = font.SysFont('Arial', 36)
# font2 = font.SysFont('Arial', 36)
# font3 = font.SysFont('Arial', 72)
# font4 = font.SysFont('Arial', 72)
# font5 = font.SysFont('Arial', 128)

#     def fire(self):
#         bullet1 = Bullet(('bullet.png'), self.rect.centerx, self.rect.top, 15, 20, -15)
#         bullets.add(bullet1)

# class Enemy(GameSprite):
#     def update(self):
#         self.rect.y += self.speed
#         global lost
#         if self.rect.y > 500:
#             self.rect.y = 0
#             self.rect.x = randint(50, 650)
#             lost = lost + 1

# class Asteroid(GameSprite):
#     def update(self):
#         self.rect.y += self.speed
#         global lost
#         if self.rect.y > 500:
#             self.rect.y = 0
#             self.rect.x = randint(50, 650)

# class Bullet(GameSprite):
#     def update(self):
#         self.rect.y += self.speed
#         if self.rect.y < 0:
#             self.kill()

# sprite_player = Player(('rocket.png'), 200, 400, 60, 100, 5)

# enemies = sprite.Group()
# for i in range(1, 6):
#     sprite_enemy = Enemy(('ufo.png'), randint(50, 650), -40, 80, 50, randint(1, 5))
#     enemies.add(sprite_enemy)

# asteroids = sprite.Group()
# for i in range(1, 4):
#     sprite_asteroid = Asteroid(('asteroid.png'), randint(50, 650), -40, 80, 50, randint(1, 5))
#     asteroids.add(sprite_asteroid)

# bullets = sprite.Group()

# game = True
# finish = False

# rel_time = False

# while game:
    
#     for e in event.get():
#         if e.type == QUIT:
#             game = False
#         elif e.type == KEYDOWN:
#             if e.key == K_SPACE:
#                 if num_fire < 7 and rel_time == False:
#                     num_fire = num_fire + 1
#                     fire_sound.play()
#                     sprite_player.fire()

#                 if num_fire >= 7 and rel_time == False:
#                     last_time = timer()
#                     rel_time = True

#     if not finish:

#         window.blit(galaxy,(0, 0))
#         sprite_player.update()
#         enemies.draw(window)
#         enemies.update()
#         bullets.update()
#         asteroids.update()
#         asteroids.draw(window)
#         bullets.draw(window)

#         if rel_time == True:
#             now_time = timer()

#             if now_time - last_time < 3:
#                 reload = font2.render('Wait, reload...', 1, (150, 0, 0))
#                 window.blit(reload, (260, 460))
#             else:
#                 num_fire = 0
#                 rel_time = False

#         sprite_player.reset()
#         if hp == 3:
#             hp_color = (0, 150, 0)
#         if hp == 2:
#             hp_color = (150, 150, 0)
#         if hp == 1:
#             hp_color = (150, 0, 0)
#         if hp == 1:
#             hp_color = (150, 0, 0)
        
#         text_2 = font2.render('Пропущено:' + str(lost), 1, (255, 255, 255))
#         text_1 = font1.render('Счет:' + str(score), 1, (255, 255, 255))
#         text_5 = font5.render(str(hp), 1, hp_color)

#         window.blit(text_1, (10, 20))
#         window.blit(text_2, (10, 50))
#         window.blit(text_5, (620, 20))
        
#         sprites_list = sprite.groupcollide(enemies, bullets, True, True)
#         sprites_list2 = sprite.groupcollide(asteroids, bullets, False, True)
#         for c in sprites_list:
#             score = score + 1
#             sprite_enemy = Enemy(('ufo.png'), randint(50, 650), -40, 80, 50, randint(1, 5))
#             enemies.add(sprite_enemy)

#         if sprite.spritecollide(sprite_player, enemies, True) or sprite.spritecollide(sprite_player, asteroids, True):
#             hp = hp - 1

#         if lost >= 3 or hp == 0:
#             text_3 = font3.render('YOU LOSE!', 5, (255, 0, 0))
#             window.blit(text_3, (250, 250))
#             finish = True

#         if score == 10:
#             text_4 = font4.render('YOU WIN!', 5, (0, 255, 0))
#             window.blit(text_4, (250, 250))
#             finish = True

#     else:
#         finish = False
#         score = 0
#         lost = 0
#         hp = 3
#         num_fire = 0
#         for b in bullets:
#             b.kill()
#         for m in enemies:
#             m.kill()
#         for a in asteroids:
#             a.kill()

#         time.delay(3000)
#         for i in range(1, 6):
#             sprite_enemy = Enemy(('ufo.png'), randint(50, 650), -40, 80, 50, randint(1, 5))
#             enemies.add(sprite_enemy)
#         for i in range(1, 4):
#             sprite_asteroid = Asteroid(('asteroid.png'), randint(50, 650), -40, 80, 50, randint(1, 5))
#             asteroids.add(sprite_asteroid)

