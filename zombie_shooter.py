#importing usefull libreries.
import pygame
import random
import pygame.display

pygame.init()
width = 500
height = 750
player_speed = 5
bullet_speed = 5
zombie1_speed = 2
zombie1_spawn_delay = 60
player_health = 100
score = 0

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('ZOMBIE SHOOTER')
game_logo  = pygame.image.load('/yj/graphics/game icon.png')
pygame.display.set_icon(game_logo)
clock = pygame.time.Clock()
#font
font  = pygame.font.Font('go3v2.ttf',30)
#graphics
line = pygame.Rect(0,height-150,width,2)
box = pygame.Rect(150,435,200,50)
game_screen = pygame.image.load('yj/graphics/background 2.png')
game_screen = pygame.transform.scale(game_screen,(width,height))
loading_screen = pygame.image.load('yj/graphics/loading screen .png')
loading_screen = pygame.transform.scale(loading_screen,(width,height))
loading_screen1 = pygame.image.load('yj/graphics/loading screen 1 .png')
loading_screen1 = pygame.transform.scale(loading_screen1,(width,height))
loading_screen2 = pygame.image.load('yj/graphics/loading screen 2.png')
loading_screen2 = pygame.transform.scale(loading_screen2,(width,height))
background = pygame.image.load('yj/graphics/game background 2.jpg')
background = pygame.transform.scale(background,(width,height))
shooter_image = pygame.image.load('yj/graphics/player pistol.gif')
shooter_image = pygame.transform.scale(shooter_image,(75,75))
zombie1_image = pygame.image.load('yj/graphics/zombie 1.png')
zombie1_image = pygame.transform.scale(zombie1_image,(75,75))
zombie2_image = pygame.image.load('yj/graphics/zombie 2.png')
zombie2_image = pygame.transform.scale(zombie2_image,(100,40.48))
zombie3_image = pygame.image.load('yj/graphics/zombie 3.png')
zombie3_image = pygame.transform.scale(zombie3_image,(100,40.48))
sniper_bullet = pygame.image.load('yj/graphics/sniper bullet.png')
sniper_bullet = pygame.transform.scale(sniper_bullet,(7,35))
pistol_bullet = pygame.image.load('yj/graphics/pistol bullet.png')
pistol_bullet = pygame.transform.scale(pistol_bullet,(7,15.55))
AR_bullet = pygame.image.load('yj/graphics/ar bullet.png')
AR_bullet = pygame.transform.scale(AR_bullet,(7,15.55))
#player
shooter = pygame.Rect(width//2-50,height-90,10,10)
#list 
Bullet_ = []
Zombie1_ = []
Zombie2_ = []
Zombie3_ = []

mode = True
while mode:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              mode = False
              load1 = False
              load2 = False
              level1_ = False
              level1 = False
              level2 = False
              level3 = False
              t = 0 

          elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_DOWN:
                  box = pygame.Rect(150,490,200,50)
               if box.top == 490 and event.key == pygame.K_RETURN:
                   load1 = False
                   load2 = True
                   mode = False               
               elif event.key == pygame.K_UP:
                  box = pygame.Rect(150,435,200,50)
               if box.top == 435 and event.key == pygame.K_RETURN:
                   load1 = True
                   load2 = False
                   level1_ = False
                   mode = False

      screen.fill('white')            
      screen.blit(loading_screen1,(0,0))
      pygame.draw.rect(screen,'white',box)   
      pygame.draw.rect(screen,'white',box)  
      mode1_text = font.render('LEVEL MODE',True,'black')
      mode2_text = font.render('MIX MODE',True,'black')
      screen.blit(mode1_text,(170,440))
      screen.blit(mode2_text,(180,500))                               
       
      pygame.display.flip()
      clock.tick(60)

while load2 :
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              load1 = False
              load2 = False
              level1_ = False
              level1 = False
              level2 = False
              level3 = False
              t = 0
          elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_SPACE:
                   level1_ = True
                   level1 = False
                   level2 = False
                   level3 = False
                   load1 = False
                   load2 = False
      screen.fill('white')            
      screen.blit(loading_screen2,(0,0))
      pygame.display.flip()
      clock.tick(60)

while level1_:
      zombie2_speed = 0.6
      zombie3_speed = 0.5
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
            level1_ = False
            load1 = False
            level1 = False
            level2 = False
            level3 = False
            t = 0
          elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_SPACE:
                   bullet = pygame.Rect(shooter.centerx+52,shooter.top-10,10,20)
                   Bullet_.append(bullet)
      #move player.
      keys = pygame.key.get_pressed()
      if keys[pygame.K_LEFT] and shooter.x>=10:
          shooter.x-=player_speed
      if keys[pygame.K_RIGHT] and shooter.x<=width-85:
          shooter.x+=player_speed
      if keys[pygame.K_LEFT] and shooter.x<=10:
          shooter.x+=0
      if keys[pygame.K_RIGHT] and shooter.x>=width-85:
          shooter.x+=0    
      for bullet in Bullet_:
          bullet.y-=bullet_speed
          if bullet.y<-1:
              Bullet_.remove(bullet)
      #spawn zombie 
      if random.randint(0,zombie1_spawn_delay+60)==0:
         zombie1 = pygame.Rect(random.randint(0,width-100),0,100,10)
         zombie1_health = 100
         Zombie1_.append([zombie1,zombie1_health])
      if random.randint(0,zombie1_spawn_delay+120)==0:
         zombie2 = pygame.Rect(random.randint(0,width-100),0,100,10)
         zombie2_health = 150
         Zombie2_.append([zombie2,zombie2_health])  
      if random.randint(0,zombie1_spawn_delay+200)==0:
         zombie3 = pygame.Rect(random.randint(0,width-100),0,100,10)
         zombie3_health = 250
         Zombie3_.append([zombie3,zombie3_health])
      #move zombies toward shooter
      for zombie in Zombie1_:
          zombie[0].y+=zombie1_speed-1
      for zombie in Zombie2_:
          zombie[0].y+=zombie2_speed
      for zombie in Zombie3_:
          zombie[0].y+=zombie3_speed  
      #collision detection
      for bullet in Bullet_:
          for zombie in Zombie1_:
              if bullet.colliderect(zombie[0]):
                 Bullet_.remove(bullet)
                 zombie[1]-=50
      for bullet in Bullet_:
          for zombie in Zombie2_:
              if bullet.colliderect(zombie[0]):
                 Bullet_.remove(bullet)  
                 zombie[1]-=50
      for bullet in Bullet_:
          for zombie in Zombie3_:
              if bullet.colliderect(zombie[0]):
                 Bullet_.remove(bullet)  
                 zombie[1]-=50
      for zombie in Zombie1_:
          if zombie[1]<=0:
              Zombie1_.remove(zombie)
              score+=5
      for zombie in Zombie2_:
          if zombie[1]<=0:
              Zombie2_.remove(zombie)
              score+=10
      for zombie in Zombie3_:
          if zombie[1]<=0:
              Zombie3_.remove(zombie)
              score+=20
      #if zombie cross the health line.
      for zombie in Zombie1_:
          if zombie[0].y>=height-150:
              player_health-=10
              Zombie1_.remove(zombie)
      for zombie in Zombie2_:
          if zombie[0].y>=height-150:
              player_health-=10
              Zombie2_.remove(zombie)
      for zombie in Zombie3_:
          if zombie[0].y>=height-150:
              player_health-=10
              Zombie3_.remove(zombie)
      #clear the screen.
      screen.fill('white')
      #draw the background and health line on the screen.
      screen.blit(background,(0,0))
      pygame.draw.rect(screen,(255,255,255),line)
      #draw shooter and zombie on screen.
      screen.blit(shooter_image,shooter)
      for zombie in Zombie1_:
          screen.blit(zombie1_image,zombie[0])
      for zombie in Zombie2_:
          screen.blit(zombie2_image,zombie[0])
      for zombie in Zombie3_:
          screen.blit(zombie3_image,zombie[0])
      #draw bullets
      for bullet in Bullet_:
          screen.blit(pistol_bullet,bullet)
      #player health and score.  
      if player_health>=60:
          a = 'green'
      elif player_health>=20 and player_health<60:
           a = 'orange'
      elif player_health<20:
           a = 'red'
      health_text = font.render(f'HEALTH:{player_health}',True,a)
      score_text = font.render(f'SCORE:{score}/500',True,'white')
      screen.blit(health_text,(10,45))
      screen.blit(score_text,(10,5))
      #check for game over or level completed.
      if player_health<=0:
          game_over = font.render('GAME OVER !! ',True,"red")
          screen.blit(game_screen,(0,0))
          screen.blit(game_over,(165,410))
          level1_ = False
          load1 = False
          level1 = False
          level2 = False
          level3 = False
          t = 0
      elif score>=500:
          level_completed = font.render('LEVEL COMPLETED',True,"green")
          screen.blit(game_screen,(0,0))
          screen.blit(level_completed ,(135,410))
          level1_ = False
          load1 = False
          level1 = False
          level2 = False
          level3 = False
          t = 0
      pygame.display.flip()
      clock.tick(60)       


while load1 :
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              load1 = False
              level1 = False
              level2 = False
              level3 = False
              t = 0
          elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_SPACE:
                   level1 = True
                   load1 = False
      screen.fill('white')            
      screen.blit(loading_screen,(0,0))
      pygame.display.flip()
      clock.tick(60)

while level1:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
            level1 = False
            level2 = False
            level3 = False
            t = 0
          elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_SPACE:
                   bullet = pygame.Rect(shooter.centerx+52,shooter.top-10,10,20)
                   Bullet_.append(bullet)
      #move player.
      keys = pygame.key.get_pressed()
      if keys[pygame.K_LEFT] and shooter.x>=10:
          shooter.x-=player_speed
      if keys[pygame.K_RIGHT] and shooter.x<=width-85:
          shooter.x+=player_speed
      if keys[pygame.K_LEFT] and shooter.x<=10:
          shooter.x+=0
      if keys[pygame.K_RIGHT] and shooter.x>=width-85:
          shooter.x+=0    
      for bullet in Bullet_:
          bullet.y-=bullet_speed
          if bullet.y<0:
              Bullet_.remove(bullet)
      #spawn zombie 
      if random.randint(0,zombie1_spawn_delay)==0:
          zombie1 = pygame.Rect(random.randint(0,width-100),0,100,10) 
          Zombie1_.append(zombie1)
      #move zombies toward shooter
      for zombie in Zombie1_:
          zombie.y+=zombie1_speed
      #collision detection
      for bullet in Bullet_:
          for zombie in Zombie1_:
              if bullet.colliderect(zombie):
                 Bullet_.remove(bullet)
                 Zombie1_.remove(zombie)
                 score+=10
      #if zombie cross the health line.
      for zombie in Zombie1_:
          if zombie.y>=height-150:
              player_health-=10
              Zombie1_.remove(zombie)
      #clear the screen.
      screen.fill('white')
      #draw the background and health line on the screen.
      screen.blit(background,(0,0))
      pygame.draw.rect(screen,(255,255,255),line)
      #draw shooter and zombie on screen.
      screen.blit(shooter_image,shooter)
      for zombie in Zombie1_:
          screen.blit(zombie1_image,zombie)
      #draw bullets
      for bullet in Bullet_:
          screen.blit(pistol_bullet,bullet)
      #player health and score.
      if player_health>=60:
          a = 'green'
      elif player_health>=20 and player_health<60:
           a = 'orange'
      elif player_health<20:
           a = 'red'
      health_text = font.render(f'HEALTH:{player_health}',True,a)
      score_text = font.render(f'SCORE:{score}/500',True,'white')
      screen.blit(health_text,(10,45))
      screen.blit(score_text,(10,5))
      #check for game over or level completed.
      if player_health<=0:
          game_over = font.render('GAME OVER !! ',True,"red")
          screen.blit(game_screen,(0,0))
          screen.blit(game_over,(165,410))
          level1 = False
          level2 = False
          level3 = False  
          t = 0
      elif score>=500:
          level_completed = font.render('LEVEL 1 COMPLETED',True,"green")
          screen.blit(game_screen,(0,0))
          screen.blit(level_completed ,(120,410))
          level1 = False
          level2 = True
          level3 = False
          t = 2000
      pygame.display.flip()
      clock.tick(60) 

pygame.time.delay(t)

if level2:
   bullet_speed = 10
   zombie2_speed = 3.7
   zombie2_spawn_delay = 45
   player_health = 100
   score = 0

   #graphics
   shooter_image = pygame.image.load('/graphics/player rifle.png')
   shooter_image = pygame.transform.scale(shooter_image,(75,75)) 
   #list 
   Bullet2_ = []
   Zombie2_ = []
   level2_ = True
   while level2_:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
            level2_ = False
            level3 = False
            t = 0
          elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_SPACE:
                   bullet2 = pygame.Rect(shooter.centerx+47,shooter.top-10,10,20)
                   Bullet2_.append(bullet2)
      #move player.
      keys = pygame.key.get_pressed()
      if keys[pygame.K_LEFT] and shooter.x>=10:
          shooter.x-=player_speed
      if keys[pygame.K_RIGHT] and shooter.x<=width-85:
          shooter.x+=player_speed
      if keys[pygame.K_LEFT] and shooter.x<=10:
          shooter.x+=0
      if keys[pygame.K_RIGHT] and shooter.x>=width-85:
          shooter.x+=0    
      for bullet2 in Bullet2_:
          bullet2.y-=bullet_speed
          if bullet2.y<0:
              Bullet2_.remove(bullet2)
      #spawn zombie 
      if random.randint(0,zombie2_spawn_delay)==0:
          zombie2 = pygame.Rect(random.randint(0,width-100),0,100,10)
          Zombie2_.append(zombie2)
      #move zombies toward shooter
      for zombie2 in Zombie2_:
          zombie2.y+=zombie2_speed
      #collision detection
      for bullet2 in Bullet2_:
          for zombie2 in Zombie2_:
              if bullet2.colliderect(zombie2):
                 Bullet2_.remove(bullet2)
                 Zombie2_.remove(zombie2)
                 score+=10 
      #if zombie cross the health line.
      for zombie2 in Zombie2_:
          if zombie2.y>=height-150:
              player_health-=10
              Zombie2_.remove(zombie2)
      #clear the screen.
      screen.fill('white')
      #draw the background and health line on the screen.
      screen.blit(background,(0,0))
      pygame.draw.rect(screen,(255,255,255),line)
      #draw shooter and zombie on screen.
      screen.blit(shooter_image,shooter)
      for zombie2 in Zombie2_:
          screen.blit(zombie2_image,zombie2)
      #draw bullets
      for bullet2 in Bullet2_:
          screen.blit(AR_bullet,bullet2)
      #player health and score.
      if player_health>=60:
          a = 'green'
      elif player_health>=20 and player_health<60:
           a = 'orange'
      elif player_health<20:
           a = 'red'
      health_text = font.render(f'HEALTH:{player_health}',True,a)
      score_text = font.render(f'SCORE:{score}/1000',True,'white')
      screen.blit(health_text,(10,45))
      screen.blit(score_text,(10,5))
      #check for game over or level completed.
      if player_health<=0:
          game_over = font.render('GAME OVER !! ',True,"red")
          screen.blit(game_screen,(0,0))
          screen.blit(game_over,(165,410))
          level2_ = False
          level3 = False
          t = 0
           
      elif score>=1000:
          level_completed = font.render('LEVEL 2 COMPLETED',True,"green")
          screen.blit(game_screen,(0,0))
          screen.blit(level_completed ,(120,410))
          level2_ = False
          level3 = True
          t = 2000
      pygame.display.flip()
      clock.tick(60)

pygame.time.delay(t)

if level3:
   bullet_speed = 10
   zombie3_speed = 4
   zombie3_spawn_delay = 40
   player_health = 100
   score = 0

   #graphics
   shooter_image = pygame.image.load('/graphics/player 1.png')
   shooter_image = pygame.transform.scale(shooter_image,(75,75))
   #list 
   Bullet3_ = []
   Zombie3_ = []
   level3_ = True
   while level3_:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
            level3_ = False
          elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_SPACE:
                   bullet3 = pygame.Rect(shooter.centerx+47,shooter.top-15,10,20)
                   Bullet3_.append(bullet3)
      #move player.
      keys = pygame.key.get_pressed()
      if keys[pygame.K_LEFT] and shooter.x>=10:
          shooter.x-=player_speed
      if keys[pygame.K_RIGHT] and shooter.x<=width-85:
          shooter.x+=player_speed
      if keys[pygame.K_LEFT] and shooter.x<=10:
          shooter.x+=0
      if keys[pygame.K_RIGHT] and shooter.x>=width-85:
          shooter.x+=0    
      for bullet3 in Bullet3_:
          bullet3.y-=bullet_speed
          if bullet3.y<0:
              Bullet3_.remove(bullet3)
      #spawn zombie 
      if random.randint(0,zombie3_spawn_delay)==0:
          zombie3 = pygame.Rect(random.randint(0,width-100),0,100,10)
          Zombie3_.append(zombie3)
      #move zombies toward shooter
      for zombie3 in Zombie3_:
          zombie3.y+=zombie3_speed
      #collision detection
      for bullet3 in Bullet3_:
          for zombie3 in Zombie3_:
              if bullet3.colliderect(zombie3):
                 Bullet3_.remove(bullet3)
                 Zombie3_.remove(zombie3)
                 score+=10 
      #if zombie cross the health line.
      for zombie3 in Zombie3_:
          if zombie3.y>=height-150:
              player_health-=10
              Zombie3_.remove(zombie3)
      #clear the screen.
      screen.fill('white')
      #draw the background and health line on the screen.
      screen.blit(background,(0,0))
      pygame.draw.rect(screen,(255,255,255),line)
      #draw shooter and zombie on screen.
      screen.blit(shooter_image,shooter)
      for zombie3 in Zombie3_:
          screen.blit(zombie3_image,zombie3)
      #draw bullets
      for bullet3 in Bullet3_:
          screen.blit(sniper_bullet,bullet3)
      #player health and score.
      if player_health>=60:
          a = 'green'
      elif player_health>=20 and player_health<60:
           a = 'orange'
      elif player_health<20:
           a = 'red'
      health_text = font.render(f'HEALTH:{player_health}',True,a)
      score_text = font.render(f'SCORE:{score}/1500',True,'white')
      screen.blit(health_text,(10,45))
      screen.blit(score_text,(10,5))
      #check for game over or level completed.
      if player_health<=0:
          game_over = font.render('GAME OVER !! ',True,"red")
          screen.blit(game_screen,(0,0))
          screen.blit(game_over,(165,410))
          level3_ = False
      elif score>=1500:
          level_completed = font.render('LEVEL 3 COMPLETED',True,"green")
          screen.blit(game_screen,(0,0))
          screen.blit(level_completed ,(120,410))
          level3_ = False
          
      pygame.display.flip()
      clock.tick(120)

pygame.display.flip()
#wait
pygame.time.delay(2000)
#exit the game
pygame.quit() 