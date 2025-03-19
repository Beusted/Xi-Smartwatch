import pygame
import time
import datetime

# Initialize Pygame
pygame.init()
SCREEN_WIDTH = 320
SCREEN_HEIGHT = 230
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Xi Smartwatch")

# Fonts
font_time = pygame.font.SysFont("Rubik", 64)
font_date = pygame.font.SysFont("Rubik", 20)
font_button = pygame.font.SysFont("Rubik", 20)

# Colors
BLACK = (0, 0, 0)
GOLD = (194, 148, 83)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
DARK_GRAY = (30, 30, 30)
BASE = (107, 106, 105)
OTHER_GREY = (84, 84, 84)
RED = (161, 73, 67)
LIGHT_GRAY = (217, 217, 217)

# Screen States
HOME_SCREEN = 0
APP_SCREEN = 1
current_screen = HOME_SCREEN

# Border Settings
BORDER_WIDTH = 4
OUTER_RADIUS = 15
INNER_RADIUS = 20
PADDING = 10

# Button Settings
button_width = 120
button_height = 40
button_x = (SCREEN_WIDTH - button_width) // 2
button_y = 160
button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

# Helper: Render Text with Outline
def render_text_with_outline(text, font, text_color, outline_color, outline_thickness=3):
    base = font.render(text, True, text_color)
    outline = font.render(text, True, outline_color)

    text_surface = pygame.Surface((base.get_width() + 2 * outline_thickness,
                                   base.get_height() + 2 * outline_thickness), pygame.SRCALPHA)

    for dx in [-outline_thickness, 0, outline_thickness]:
        for dy in [-outline_thickness, 0, outline_thickness]:
            if dx != 0 or dy != 0:
                text_surface.blit(outline, (dx + outline_thickness, dy + outline_thickness))

    text_surface.blit(base, (outline_thickness, outline_thickness))
    return text_surface

# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if current_screen == HOME_SCREEN:
                    current_screen = APP_SCREEN
            elif event.key == pygame.K_ESCAPE:
                if current_screen == APP_SCREEN:
                    current_screen = HOME_SCREEN

    # Clear screen
    screen.fill(BASE)

    if current_screen == HOME_SCREEN:
        # Draw outer border
        pygame.draw.rect(screen, BASE, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT),
                         BORDER_WIDTH, border_radius=OUTER_RADIUS)

        # Inner rounded box
        inner_rect = pygame.Rect(PADDING, PADDING, SCREEN_WIDTH - 2*PADDING, SCREEN_HEIGHT - 2*PADDING)
        pygame.draw.rect(screen, LIGHT_GRAY, inner_rect, border_radius=INNER_RADIUS)

        # Time and Date
        now = datetime.datetime.now()
        time_str = now.strftime("%I:%M")
        date_str = now.strftime("%A, %B %d").lstrip("0").replace(" 0", " ")

        time_surface = render_text_with_outline(time_str, font_time, GOLD, BLACK, outline_thickness=3)
        time_rect = time_surface.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 30))
        screen.blit(time_surface, time_rect)

        date_surface = render_text_with_outline(date_str, font_date, GOLD, BLACK, outline_thickness=3)
        date_rect = date_surface.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 30))
        screen.blit(date_surface, date_rect)

        # Draw Button (hover effect)
        mouse_pos = pygame.mouse.get_pos()
        hovered = button_rect.collidepoint(mouse_pos)
        button_color = GOLD if hovered else RED
        pygame.draw.rect(screen, button_color, button_rect, border_radius=10)

        # Button Text
        text_color = RED if hovered else GOLD
        button_text_surface = render_text_with_outline("ENTER", font_button, text_color, BLACK, outline_thickness=3)
        button_text_rect = button_text_surface.get_rect(center=button_rect.center)
        screen.blit(button_text_surface, button_text_rect)

    elif current_screen == APP_SCREEN:
        # App Screen UI
        screen.fill(LIGHT_GRAY)
        app_text_surface = render_text_with_outline("App Screen", font_time, RED, BLACK, outline_thickness=3)
        app_text_rect = app_text_surface.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        screen.blit(app_text_surface, app_text_rect)

    # Update screen
    pygame.display.update()
    time.sleep(0.1)

pygame.quit()
