import pygame
import sys

pygame.init()

# Colors, fonts, and dimensions
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 320
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
menu_items = ["Stopwatch", "Number Generator", "Fitness Tracker", "Clock"]
item_height = 65
spacing = 25
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

    # Define the scrollable area inside the light gray layer
    scroll_area = pygame.Rect(20, 20, SCREEN_WIDTH - 40, SCREEN_HEIGHT - 40)

    while running:
        screen.fill(BASE)

        # Light gray background layer
        layer_rect = pygame.Rect(10, 10, SCREEN_WIDTH - 20, SCREEN_HEIGHT - 20)
        pygame.draw.rect(screen, LIGHT_GRAY, layer_rect, border_radius=15)

        # Create a subsurface to clip buttons within the light gray area
        scroll_surface = screen.subsurface(scroll_area).copy()

        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Offset mouse coordinates for detection inside scroll area
        adjusted_mouse_y = mouse_y - scroll_area.y

        # Draw each menu item within the scroll surface
        for i, item in enumerate(menu_items):
            y_pos = 10 + i * (item_height + spacing) + scroll_offset
            if 0 <= y_pos <= scroll_area.height - item_height:  # Clip strictly to the gray box
                container_rect = pygame.Rect(0, y_pos, scroll_area.width, item_height)
                if container_rect.collidepoint(mouse_x - scroll_area.x, adjusted_mouse_y):
                    pygame.draw.rect(scroll_surface, GOLD, container_rect, border_radius=10)
                    text = font.render(item, True, RED)
                else:
                    pygame.draw.rect(scroll_surface, RED, container_rect, border_radius=10)
                    text = font.render(item, True, GOLD)

                text_rect = text.get_rect(center=container_rect.center)
                scroll_surface.blit(text, text_rect)

        # Blit the clipped scroll surface onto the main screen
        screen.blit(scroll_surface, scroll_area.topleft)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if scroll_area.collidepoint(event.pos):
                    dragging = True
                    start_y = event.pos[1]

            elif event.type == pygame.MOUSEBUTTONUP:
                dragging = False
                for i, item in enumerate(menu_items):
                    y_pos = 10 + i * (item_height + spacing) + scroll_offset
                    container_rect = pygame.Rect(0, y_pos, scroll_area.width, item_height)
                    if container_rect.collidepoint(event.pos[0] - scroll_area.x, event.pos[1] - scroll_area.y):
                        return item.lower().replace(" ", "")

            elif event.type == pygame.MOUSEMOTION and dragging:
                scroll_offset += event.rel[1]
                scroll_offset = max(min_scroll, min(scroll_offset, max_scroll))

        clock.tick(30)
