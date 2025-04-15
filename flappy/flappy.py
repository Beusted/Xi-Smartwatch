import pygame
from sys import exit
import random
import os
import re

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
BRIGHT_GOLD = (255, 215, 0)  # Brighter gold for better visibility

# High score - THIS VALUE WILL BE MODIFIED BY THE GAME ITSELF
# Do not change this value manually
SAVED_HIGH_SCORE = 0

# Image Assets
pony_images = [pygame.image.load("flappy/assets/pony_up.png"), pygame.image.load("flappy/assets/pony_mid.png"), pygame.image.load("flappy/assets/pony_down.png")]
skyline_image = pygame.image.load("flappy/assets/background.png")
ground_image = pygame.image.load("flappy/assets/ground.png")
top_fence_image = pygame.image.load("flappy/assets/fence_top.png")
bottom_fence_image = pygame.image.load("flappy/assets/fence_bottom.png")
game_over_image = pygame.image.load("flappy/assets/game_over.png")
start_image = pygame.image.load("flappy/assets/start.png")

# Game
scroll_speed = 1
pony_start_position = (100, 160)
score = 0
high_score = SAVED_HIGH_SCORE
score_font = pygame.font.Font("flappy/assets/PressStart2P-Regular.ttf", 14)
small_font = pygame.font.Font("flappy/assets/PressStart2P-Regular.ttf", 10)  # Smaller font for game over screen
game_stopped = True

# Function to update high score in this file
def update_high_score_in_file(new_high_score):
    """Update the high score directly in the script file"""
    try:
        # Get the full path to the current script
        script_path = os.path.abspath(__file__)
        
        # Read the entire file content
        with open(script_path, 'r') as f:
            content = f.read()
        
        # Use regex to find and replace the SAVED_HIGH_SCORE value
        new_content = re.sub(r'SAVED_HIGH_SCORE = \d+', f'SAVED_HIGH_SCORE = {new_high_score}', content)
        
        # Write the updated content back to the file
        with open(script_path, 'w') as f:
            f.write(new_content)
            
        return True
    except Exception as e:
        print(f"Failed to update high score: {e}")
        return False

class Pony(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pony_images[0]
        self.rect = self.image.get_rect()
        self.rect.center = pony_start_position
        self.image_index = 0
        self.vel = 0
        self.flap = False
        self.alive = True
    
    def update(self):
        # Pony Animation
        self.image_index += 1
        if self.image_index >= 30:
            self.image_index = 0
        self.image = pony_images[self.image_index // 10]

        # Gravity and Flap
        self.vel += 0.5
        if self.vel > 7:
            self.vel = 7
        if self.rect.y < 320:
            self.rect.y += int(self.vel)
        if self.vel == 0:
            self.flap = False

        # User Input
        if pygame.mouse.get_pressed()[0] and not self.flap and self.rect.y > 0 and self.alive:
            self.flap = True
            self.vel = -7
            
class Fence(pygame.sprite.Sprite):
    def __init__(self, x, y, image, fence_type): # takes coordinates of fence, image
        pygame.sprite.Sprite.__init__(self) #initialize parent class
        self.image = image # = to image we are passing in agrs
        # conveinent for checking for collisions 
        self.rect = self.image.get_rect() # manipulate position of img
        self.rect.x, self.rect.y = x, y # set xy coords of img = to the xy coords we pass in agrs
        self.enter, self.exit, self.passed = False, False, False
        self.fence_type = fence_type

    def update(self): # responsible for moving fences from left to right side of screen
        # move fences
        self.rect.x -= scroll_speed
        if self.rect.x <= -SCREEN_WIDTH:
            self.kill()

        global score 
        if self.fence_type == "bottom":
            if pony_start_position[0] > self.rect.topleft[0] and not self.passed:
                self.enter = True 
            if pony_start_position[0] > self.rect.topright[0] and not self.passed:
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

    # Load the saved high score at the start of each game
    high_score = SAVED_HIGH_SCORE

    # Instantiate Initial Ground
    x_pos_ground, y_pos_ground = 0, 300
    ground = pygame.sprite.Group()
    ground.add(Ground(x_pos_ground, y_pos_ground))
    
    # Fences Setup
    fence_timer = 0
    fences = pygame.sprite.Group()
    
    # Instantiate Pony
    pony = pygame.sprite.GroupSingle()
    pony.add(Pony())

    # Game over state
    game_over = False
    wait_time = 0  # Add a small delay before accepting input after game over

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
            
        # Draw - Fences, Ground, and Pony
        fences.draw(screen)
        ground.draw(screen)
        pony.draw(screen)

        # Show Score
        score_text = score_font.render ('Score: ' + str(score), True, pygame.Color(255, 255, 255))
        screen.blit(score_text, (20, 20))

        # Update - Fences, Ground, and Pony
        if pony.sprite.alive and not game_over:
            fences.update()
            ground.update()
            pony.update()

        # Fence Collisions 
        collision_fences = pygame.sprite.spritecollide(pony.sprites()[0], fences, False)
        collision_ground = pygame.sprite.spritecollide(pony.sprites()[0], ground, False)
        
        if (collision_fences or collision_ground) and not game_over:
            pony.sprite.alive = False
            game_over = True
            
            # Update high score if current score is higher
            if score > high_score:
                high_score = score
                # Update the high score in the file - use a more reliable method
                success = update_high_score_in_file(high_score)
                if not success:
                    print("Warning: Failed to save high score!")
        
        # Display game over screen
        if game_over:
            screen.blit(game_over_image, (SCREEN_WIDTH // 2 - game_over_image.get_width() // 2, 
                                        SCREEN_HEIGHT // 2 - game_over_image.get_height() // 2))
            
            # Add total score text - positioned below the centered game over image
            total_score_text = small_font.render('Total Score: ' + str(score), True, WHITE)
            screen.blit(total_score_text, (SCREEN_WIDTH // 2 - total_score_text.get_width() // 2, 
                                        SCREEN_HEIGHT // 2 + 30))
            
            # Add high score text - positioned further below
            high_score_text = small_font.render('High Score: ' + str(high_score), True, BRIGHT_GOLD)
            screen.blit(high_score_text, (SCREEN_WIDTH // 2 - high_score_text.get_width() // 2, 
                                        SCREEN_HEIGHT // 2 + 50))
            
            # Add a small delay before accepting input to prevent accidental restarts
            wait_time += 1
            if wait_time > 30 and pygame.mouse.get_pressed()[0]:  # Half second delay (30 frames at 60fps)
                score = 0
                break

        # Spawn Fences 
        if fence_timer <= 0 and pony.sprite.alive and not game_over:
            x_top, x_bottom = 550, 550
            y_top = random.randint(-825, -600)
            gap = random.randint(100, 150)
            y_bottom = y_top + top_fence_image.get_height() + gap
            fences.add(Fence(x_top, y_top, top_fence_image, 'top'))
            fences.add(Fence(x_bottom, y_bottom, bottom_fence_image, 'bottom'))
            fence_timer = random.randint(180, 250)
        fence_timer -= 1

        clock.tick(30)
        pygame.display.update()

def menu():
    global game_stopped
    waiting = True

    # 1. Define a Back button rect & font (top-left or top-center)
    back_button_rect = pygame.Rect(20, 40, 60, 30)
    back_font = pygame.font.SysFont("flappy/assets/PressStart2P-Regular.ttf", 14)

    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if user clicked the BACK button
                if back_button_rect.collidepoint(event.pos):
                    # 2. Behavior: For now, exit entire game
                    pygame.quit()
                    exit()
                else:
                    # 3. Otherwise, start the game
                    waiting = False

        screen.fill(BLACK)
        screen.blit(skyline_image, (0, 0))
        screen.blit(ground_image, Ground(0, 520))
        screen.blit(pony_images[0], (100, 250))
        screen.blit(start_image, (
            SCREEN_WIDTH // 10 - start_image.get_width() // 10,
            SCREEN_WIDTH // 10 - start_image.get_height() // 10
        ))

        # Show high score on menu screen - also using the brighter gold
        high_score_text = score_font.render('High Score: ' + str(high_score), True, BRIGHT_GOLD)
        screen.blit(high_score_text, (20, 20))

        # 4. Draw the Back button
        pygame.draw.rect(screen, (80, 80, 80), back_button_rect)
        back_text = back_font.render("BACK", True, WHITE)
        back_text_rect = back_text.get_rect(center=back_button_rect.center)
        screen.blit(back_text, back_text_rect)

        pygame.display.update()

    # Go into the main game loop
    main()


# App Loop
while True:
    menu()
