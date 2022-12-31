import pygame, sys
from pygame.locals import QUIT
import random

pygame.init()
screen = pygame.display.set_mode((800, 400))  #sets the world boundaries
pygame.display.set_caption('space invader-like game')
clock = pygame.time.Clock()
font = pygame.font.Font(None,50)

bullet = pygame.image.load('bullet.png').convert_alpha()#loading in the bullet
world_background = pygame.image.load('space.png').convert() #loading in the background
space_ship = pygame.image.load('spaceship.png').convert_alpha()#loading in the space ship
alien = pygame.image.load('alien_2.png')#loading in the alien


'''WORLD'''
world_back_scaled = pygame.transform.scale(world_background, (800, 400)) #updating the size of the background
screen.blit(world_back_scaled, (0, 0)) #adding the fixed background onto the screen

'''BULLET'''
bullet_scaled =  pygame.transform.scale(bullet, (35,30)) #updating the size of the bullet
bullet_rect = bullet_scaled.get_rect(midbottom = (90,93)) #making a rectangle around the scaled alien
 #making sure that the bullet goes whereever the ship goes
 #adding the fixed alien onto the screen

'''SPACE SHIP'''
space_ship_scaled = pygame.transform.scale(space_ship, (200,100)) #updating the size of the space ship
space_ship_rect = space_ship_scaled.get_rect(midbottom = (50,100)) #making a rectangle around the scaled space ship
screen.blit(space_ship_scaled, space_ship_rect) #adding the fixed space ship onto the screen

'''ALIEN'''
alien_scaled = pygame.transform.scale(alien, (65,70)) #updating the size of the aliens
alien_rect = alien_scaled.get_rect(midbottom = (500,300)) #making a rectangle around the scaled alien
screen.blit(alien_scaled, alien_rect) #adding the fixed alien onto the screen

"SCORE"
score = 0
score_board = font.render(f"Score: {score}",None,'Green')
score_rec = score_board.get_rect(midbottom = (300,50))
screen.blit(score_board,score_rec)

"Game over"
Game_over = font.render("Game over",None,'Red')
Game_over_rec = Game_over.get_rect(midbottom = (400,200))
screen.blit(Game_over,Game_over_rec)

ship_movement = 0 
bullet_movement = 0
alien_movement = 0


game_ongoing = True

while True:
    #leave comments
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if game_ongoing:
            if event.type == pygame.KEYDOWN: #if the wanted key is pressed
                if event.key == pygame.K_UP: #if the wanted key is the up arrow
                    if space_ship_rect.y >= -30:
                        space_ship_rect.y  -= 20  
                if event.key == pygame.K_DOWN: #if the wanted key is the down arrow
                    if space_ship_rect.y <= 340: 
                        space_ship_rect.y  += 20
                #space_ship_rect.y += ship_movement

                if event.key == pygame.K_SPACE:
                    if bullet_rect.x <= 800:
                        bullet_movement = 10
                    elif bullet_rect.x > 800:
                        bullet_rect.x = space_ship_rect.x +100
                        bullet_rect.y = space_ship_rect.y
                if alien_rect.x < 0:
                    alien_rect.y = random.randint(0,400)
                    alien_rect.x = 800
                

                if bullet_rect.colliderect(alien_rect) == True:
                    score +=1 
    bullet_rect.x += bullet_movement
    screen.blit(Game_over,Game_over_rec)
    screen.blit(world_back_scaled, (0, 0))
    screen.blit(bullet_scaled, bullet_rect)
    screen.blit(space_ship_scaled, space_ship_rect)
    screen.blit(alien_scaled,alien_rect)
    screen.blit(score_board,score_rec)
    score_board = font.render(f"Score: {score}",None,'Red')

    alien_rect.x -=2

    if space_ship_rect.colliderect(alien_rect):
        screen.blit(Game_over,Game_over_rec)
        game_ongoing = False


    




    pygame.display.update()  #second last line of code
    clock.tick(60)  #last line of code