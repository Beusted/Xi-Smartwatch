import pygame
from sys import exit

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

        # Draw - Pipes, Ground, and Bird
        ground.draw(screen)
        bird.draw(screen)

        # Update - Pipes, Ground, and Bird
        ground.update()
        bird.update()

        clock.tick(60)
        pygame.display.update()


main()
