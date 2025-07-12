import pygame
import sys
from player import Player
from asteroid import Asteroid
from constants import SCREEN_HEIGHT,SCREEN_WIDTH,WHITE,BLACK 
from asteroidfield import AsteroidField 
pygame.init()   

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    BLACK = (0,0,0)
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x,y)

    running = True 
    clock = pygame.time.Clock()
    dt = 0
    
    asteroids = pygame.sprite.Group()    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field_instance = AsteroidField()
    # In your initialization code
    shots = pygame.sprite.Group()
    shots.containers = (updatable,drawable)


    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False 
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collisions(asteroid):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collisions(asteroid):
                    shot.kill()
                    asteroid.kill()
        for sprite in updatable:
            sprite.update(dt)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            new_shot = player.shoot()
            if new_shot != None:
                shots.add(new_shot)
                updatable.add(new_shot)
                drawable.add(new_shot) 
            

        screen.fill(BLACK) 
        for sprite in drawable: 
            sprite.draw(screen)
        pygame.display.flip()
    

if __name__ == "__main__":
    main()                     



