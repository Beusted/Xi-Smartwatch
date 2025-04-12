import pygame
from sys import exit
import random
import os

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

# High score - THIS VALUE WILL BE MODIFIED BY THE GAME ITSELF
# Do not change this value manually
SAVED_HIGH_SCORE = 2

# Image Assets
pony_images = [pygame.image.load("flappy/assets/pony_stretch.png"), pygame.image.load("flappy/assets/pony_mid.png"), pygame.image.load("flappy/assets/pony_close.png")]
skyline_image = pygame.image.load("flappy/assets/background.png")
ground_image = pygame.image.load("flappy/assets/ground.png")
top_pipe_image = pygame.image.load("flappy/assets/pipe_top.png")
bottom_pipe_image = pygame.image.load("flappy/assets/pipe_bottom.png")
game_over_image = pygame.image.load("flappy/assets/game_over.png")
start_screen = pygame.image.load("flappy/assets/GoldenPonyStartHigher.png")

# Game
scroll_speed = 1
bird_start_position = (100, 160)
score = 0
high_score = SAVED_HIGH_SCORE
font = pygame.font.SysFont('Segoe', 26)
game_stopped = True

# Function to update high score in this file
def update_high_score_in_file(new_high_score):
    # Get the path to the current script file
    script_path = os.path.abspath(__file__)
    
    # Read the content of the current script
    with open(script_path, 'r') as file:
        lines = file.readlines()
    
    # Find the line with SAVED_HIGH_SCORE and replace it
    for i, line in enumerate(lines):
        if 'SAVED_HIGH_SCORE =' in line:
            lines[i] = f"SAVED_HIGH_SCORE = {new_high_score}\n"
            break
    
    # Write the modified content back to the script
    with open(script_path, 'w') as file:
        file.writelines(lines)

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pony_images[0]
        self.rect = self.image.get_rect()
        self.rect.center = bird_start_position
        self.image_index = 0
        self.vel = 0
        self.flap = False
        self.alive = True
    
    def update(self):
        # Bird Animation
        self.image_index += 1
        if self.image_index >= 30:
            self.image_index = 0
        self.image = pony_images[self.image_index // 10]

        # Gravity and Flap
        self.vel += 0.5
        if self.vel > 7:
            self.vel = 7
        if self.rect.y < 500:
            self.rect.y += int(self.vel)
        if self.vel == 0:
            self.flap = False

        # User Input
        if pygame.mouse.get_pressed()[0] and not self.flap and self.rect.y > 0 and self.alive:
            self.flap = True
            self.vel = -7
            
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, image, pipe_type): # takes coordinates of pipe, image
        pygame.sprite.Sprite.__init__(self) #initialize parent class
        self.image = image # = to image we are passing in agrs
        # conveinent for checking for collisions 
        self.rect = self.image.get_rect() # manipulate position of img
        self.rect.x, self.rect.y = x, y # set xy coords of img = to the xy coords we pass in agrs
        self.enter, self.exit, self.passed = False, False, False
        self.pipe_type = pipe_type
        
    def update(self): # responsible for moving pipes from left to right side of screen
        # move pipes
        self.rect.x -= scroll_speed
        if self.rect.x <= -SCREEN_WIDTH:
            self.kill()
        
        global score 
        if self.pipe_type == "bottom":
            if bird_start_position[0] > self.rect.topleft[0] and not self.passed:
                self.enter = True 
            if bird_start_position[0] > self.rect.topright[0] and not self.passed:
                self.exit = True
            if self.enter and self.exit and not self.passed:
                self.passed = True
                score += 1
                
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
    global score, high_score

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
        
        # User Input 
        user_input = pygame.mouse.get_pressed()
        
        # Draw Background
        screen.blit(skyline_image, (0, 0))

        # Spawn Ground
        if len(ground) <= 2:
            ground.add(Ground(SCREEN_WIDTH, y_pos_ground))
            
        # Draw - Pipes, Ground, and Bird
        pipes.draw(screen)
        ground.draw(screen)
        bird.draw(screen)
        
        # Show Score and High Score
        score_text = font.render('Score: ' + str(score), True, pygame.Color(255, 255, 255))
        high_score_text = font.render('High Score: ' + str(high_score), True, pygame.Color(255, 255, 255))
        screen.blit(score_text, (20, 20))
        screen.blit(high_score_text, (20, 50))
        
        # Update - Pipes, Ground, and Bird
        if bird.sprite.alive:
            pipes.update()
            ground.update()
            bird.update()
        
        # Pipe Collisions 
        collision_pipes = pygame.sprite.spritecollide(bird.sprites()[0], pipes, False)
        collision_ground = pygame.sprite.spritecollide(bird.sprites()[0], ground, False)
        if collision_pipes or collision_ground:
            bird.sprite.alive = False
            
            # Update high score if current score is higher
            if score > high_score:
                high_score = score
                # Update the high score in the file itself
                try:
                    update_high_score_in_file(high_score)
                except Exception as e:
                    print(f"Could not update high score in file: {e}")
                
            screen.blit(game_over_image, (SCREEN_WIDTH // 2 - game_over_image.get_width() // 2, 
                                          SCREEN_HEIGHT // 2 - game_over_image.get_height() // 2))
            if pygame.mouse.get_pressed()[0]:
                score = 0
                break
            
        # Spawn Pipes 
        if pipe_timer <= 0 and bird.sprite.alive:
            x_top, x_bottom = 550, 550
            y_top = random.randint(-600, -480)
            gap = random.randint(90, 130)
            y_bottom = y_top + gap + bottom_pipe_image.get_height()
            pipes.add(Pipe(x_top, y_top, top_pipe_image, 'top'))
            pipes.add(Pipe(x_bottom, y_bottom, bottom_pipe_image, 'bottom'))
            pipe_timer = random.randint(180, 250)
        pipe_timer -= 1

        clock.tick(60)
        pygame.display.update()

def menu():
    global game_stopped
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # Trigger the game start on a discrete mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False
                
        # Draw Menu pop up
        screen.fill((0, 0, 0))
        screen.blit(skyline_image, (0, 0))
        screen.blit(ground_image, Ground(0, 520))
        screen.blit(pony_images[0], (100, 250))
        screen.blit(start_screen, (SCREEN_WIDTH // 10 - start_screen.get_width() // 10,
                                  SCREEN_WIDTH // 10 - start_screen.get_height() // 10))
        
        # Show high score on menu screen
        high_score_text = font.render('High Score: ' + str(high_score), True, pygame.Color(255, 255, 255))
        screen.blit(high_score_text, (20, 20))

        pygame.display.update()
    main()

while True:
    menu()