import pygame
from sys import exit
import random

pygame.init()
clock = pygame.time.Clock()

# Screen dimensions
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 320
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Xi Smartwatch")

# Colors
BLACK = (0, 0, 0)
GOLD = (194, 148, 83)
RED = (161, 73, 67)
WHITE = (255, 255, 255)
DARK_GRAY = (30, 30, 30)
BASE = (107, 106, 105)
LIGHT_GRAY = (217, 217, 217)

# Image Assets
bird_images = [pygame.image.load("flappy/assets/bird_down.png"), pygame.image.load("flappy/assets/bird_mid.png"), pygame.image.load("flappy/assets/bird_up.png")]
skyline_image = pygame.image.load("flappy/assets/background.png")
ground_image = pygame.image.load("flappy/assets/ground.png")
top_pipe_image = pygame.image.load("flappy/assets/pipe_top.png")
bottom_pipe_image = pygame.image.load("flappy/assets/pipe_bottom.png")
game_over_image = pygame.image.load("flappy/assets/game_over.png")
start_image = pygame.image.load("flappy/assets/start.png")

# Game
scroll_speed = 1
bird_start_position = (100, 160)
score = 0 

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = bird_images[0]
        self.rect = self.image.get_rect()
        self.rect.center = bird_start_position
        self.image_index = 0
        self.vel = 0
        self.flap = False
    
    def update(self):
        # Bird Animation
        self.image_index += 1
        if self.image_index >= 30:
            self.image_index = 0
        self.image = bird_images[self.image_index // 10]

        # Gravity and Flap
        self.vel += 0.5
        if self.vel > 7:
            self.vel = 7
        if self.rect.y < 500:
            self.rect.y += int(self.vel)
        if self.vel == 0:
            self.flap = False

        # User Input
        if pygame.mouse.get_pressed()[0] and not self.flap and self.rect.y > 0:
            self.flap = True
            self.vel = -7
            
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, image): # takes coordinates of pipe, image
        pygame.sprite.Sprite.__init__(self) #initialize parent class
        self.image = image # = to image we are passing in agrs
        # conveinent for checking for collisions 
        self.rect = self.image.get_rect() # manipulate position of img
        self.rect.x, self.rect.y = x, y # set xy coords of img = to the xy coords we pass in agrs
        
        def update(self): # responsible for moving pipes from left to right side of screen
            # move pipes
            self.rect.x -= scroll_speed
            if self.rect.x <= -SCREEN_WIDTH:
                self.kill()

class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = ground_image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self):
        # Moving ground
        self.rect.x -= scroll_speed
        if self.rect.x <= -SCREEN_WIDTH:
            self.kill()

# Exiting game
def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

# Game Main Method
def main():
    # Instantiate Initial Ground
    x_pos_ground, y_pos_ground = 0, 520
    ground = pygame.sprite.Group()
    ground.add(Ground(x_pos_ground, y_pos_ground))
    
    # Pipes Setup
    pipe_timer = 0
    pipes = pygame.sprite.Group()
    
    # Instantiate Bird
    bird = pygame.sprite.GroupSingle()
    bird.add(Bird())

    run = True
    while run:
        # Quit game
        quit_game()

        # Reset Frame
        screen.fill(BLACK)

        # Draw Background
        screen.blit(skyline_image, (0, 0))

        # Spawn Ground
        if len(ground) <= 2:
            ground.add(Ground(SCREEN_WIDTH, y_pos_ground))
            
        # Spawn Pipes 
        if pipe_timer <= 0:
            x_top, x_bottom = 479, 479
            y_top = random.randint(-400, -300)
            gap = random.randint(90, 130)
            y_bottom = y_top + gap + bottom_pipe_image.get_height()
            pipes.add(Pipe(x_top, y_top, top_pipe_image))
            pipes.add(Pipe(x_bottom, y_bottom, bottom_pipe_image))
            pipe_timer = random.randint(180, 250)
        pipe_timer -= 1
        
        # Draw - Pipes, Ground, and Bird
        pipes.draw(screen)
        ground.draw(screen)
        bird.draw(screen)
        
        # Update - Pipes, Ground, and Bird
        pipes.update()
        ground.update()
        bird.update()

        clock.tick(60)
        pygame.display.update()

        # Show Score
        score_text = font.render ('Score: ' + str(score), True, pygame.Color(255, 255, 255))
        window.blit(score_text, (20, 20))
        



main()
