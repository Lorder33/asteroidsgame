import pygame
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


    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False 
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        screen.fill(BLACK)
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()
    

if __name__ == "__main__":
    main()




