import pygame
import sys

pygame.init()

# Colors, fonts, and dimensions
SCREEN_WIDTH = 320
SCREEN_HEIGHT = 230
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

# Lists each app
menu_items = ["Stopwatch", "Dice", "Number Generator", "Clock"]
item_height = 50
spacing = 10
visible_items = 3
scroll_offset = 0
min_scroll = -(len(menu_items) - visible_items) * (item_height + spacing)
max_scroll = 0

def run_app_menu(screen):
    global scroll_offset
    clock = pygame.time.Clock()
    running = True
    dragging = False
    start_y = 0

    while running:
        screen.fill(BASE)
        layer_rect = pygame.Rect(10, 10, SCREEN_WIDTH - 20, SCREEN_HEIGHT - 20)
        pygame.draw.rect(screen, LIGHT_GRAY, layer_rect, border_radius=15)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        for i, item in enumerate(menu_items):
            y_pos = 30 + i * (item_height + spacing) + scroll_offset
            if 10 <= y_pos <= SCREEN_HEIGHT - 30:  # Ensure items stay within the grey box
                container_rect = pygame.Rect(20, y_pos, SCREEN_WIDTH - 40, item_height)
                if container_rect.collidepoint(mouse_x, mouse_y):
                    pygame.draw.rect(screen, GOLD, container_rect, border_radius=10)
                    text = font.render(item, True, RED)
                else:
                    pygame.draw.rect(screen, RED, container_rect, border_radius=10)
                    text = font.render(item, True, GOLD)
                text_rect = text.get_rect(center=container_rect.center)
                screen.blit(text, text_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                dragging = True
                start_y = event.pos[1]

            elif event.type == pygame.MOUSEBUTTONUP:
                dragging = False
                for i, item in enumerate(menu_items):
                    y_pos = 30 + i * (item_height + spacing) + scroll_offset
                    container_rect = pygame.Rect(20, y_pos, SCREEN_WIDTH - 40, item_height)
                    if container_rect.collidepoint(event.pos):
                        return item.lower().replace(" ", "")

            elif event.type == pygame.MOUSEMOTION and dragging:
                scroll_offset += event.rel[1]
                scroll_offset = max(min_scroll, min(scroll_offset, max_scroll))  # Keep scrolling within bounds

        clock.tick(30)
