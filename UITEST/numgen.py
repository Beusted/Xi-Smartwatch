import pygame
import random

pygame.init()

# Colors and fonts
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (161, 73, 67)
GOLD = (194, 148, 83)
font = pygame.font.SysFont(None, 48)

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 320

def run_random_number_screen(screen):
    running = True
    number = random.randint(1, 100)

    while running:
        screen.fill(BLACK)
        text = font.render(f"Number: {number}", True, GOLD)
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))

        back_button = pygame.Rect(20, 20, 120, 40)
        pygame.draw.rect(screen, RED, back_button)
        back_text = font.render("Back", True, WHITE)
        screen.blit(back_text, (back_button.x + 20, back_button.y + 5))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    return True

        pygame.display.update()

    return False
