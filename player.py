import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED,WHITE,SHOT_RADIUS,PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from circleshape import CircleShape


class Player(CircleShape):
    
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.timer = PLAYER_SHOOT_COOLDOWN 
        
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    
   
    def draw(self, screen):
        pygame.draw.polygon(screen, WHITE, self.triangle(), 2)

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def update(self, dt):
        self.timer -= dt
        if self.timer < 0:
            self.timer = 0 
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
    
    def shoot(self): 
        if self.timer > 0:
            return None 
        self.timer = PLAYER_SHOOT_COOLDOWN
        new_shot = Shot(self.position.x, self.position.y)
        velocity = pygame.Vector2(0,1)
        velocity = velocity.rotate(self.rotation)
        velocity = velocity * PLAYER_SHOOT_SPEED
        new_shot.velocity = velocity 
        return new_shot
        

    

class Shot(CircleShape):
    def __init__(self, x, y, radius=SHOT_RADIUS, velocity=pygame.Vector2(0, 0)):
        super().__init__(x, y, radius)
        self.velocity = velocity
    
    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.position.x), int(self.position.y)), self.radius) 

    def update(self,dt):
        self.position += self.velocity * dt

  


         

    
