import pygame
from player import Player
from constants import SCREEN_HEIGHT,SCREEN_WIDTH
pygame.init()   

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    BLACK = (0,0,0)
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y)


    running = True 
    clock = pygame.time.Clock()
    dt = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
        dt = clock.tick(60) / 1000
        player.update(dt)
        
        screen.fill(BLACK)
        player.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()




