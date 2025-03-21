import pygame
import sys

pygame.init()

# screen dimentions
SCREEN_WIDTH = 320
SCREEN_HEIGHT = 230

# fonts and colors
font = pygame.font.SysFont(None, 30)
WHITE = (255, 255, 255)
GRAY = (180, 180, 180)
BLUE = (100, 149, 237)
BLACK = (0, 0, 0)
GOLD = (194, 148, 83)
RED = (161, 73, 67)
DARK_GRAY = (30, 30, 30)
BASE = (107, 106, 105)
LIGHT_GRAY = (217, 217, 217)

# app names
menu_items = ["Stopwatch", "Dice", "Fitness Tracker", "Exit"]
selected_index = 0

# constants for each item
item_height = 50
spacing = 10
visible_items = 3

# main function, calls to apps
def run_app_menu(screen):
    global selected_index
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(BASE)

        # light gray layer behind containers
        layer_rect = pygame.Rect(10, 10, SCREEN_WIDTH - 20, SCREEN_HEIGHT - 20)  # Increased height
        pygame.draw.rect(screen, LIGHT_GRAY, layer_rect, border_radius=15)

        # scroll effect
        start_index = max(0, selected_index - visible_items + 1)
        end_index = min(len(menu_items), start_index + visible_items)

        for i in range(start_index, end_index):
            y_pos = 30 + (i - start_index) * (item_height + spacing)
            container_rect = pygame.Rect(20, y_pos, SCREEN_WIDTH - 40, item_height)

            if i == selected_index:
                pygame.draw.rect(screen, GOLD, container_rect, border_radius=10)
                text_color = RED
            else:
                pygame.draw.rect(screen, RED, container_rect, border_radius=10)
                text_color = GOLD

            # render text
            text = font.render(menu_items[i], True, text_color)
            text_rect = text.get_rect(center=container_rect.center)
            screen.blit(text, text_rect)

        pygame.display.flip()

        # handels events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_index = (selected_index - 1) % len(menu_items)
                elif event.key == pygame.K_DOWN:
                    selected_index = (selected_index + 1) % len(menu_items)
                elif event.key == pygame.K_RETURN:
                    print(f"Selected: {menu_items[selected_index]}")
                    if menu_items[selected_index] == "Exit":
                        running = False

        clock.tick(30)
