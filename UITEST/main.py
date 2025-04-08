#main.py
import pygame
import time
import datetime
import appscreen
import timerui
#import numgen
#import complexui

pygame.init()

# Screen dimensions
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
RED = (161, 73, 67)
WHITE = (255, 255, 255)
DARK_GRAY = (30, 30, 30)
BASE = (107, 106, 105)
LIGHT_GRAY = (217, 217, 217)

# Screen states
HOME_SCREEN = 0
APP_SCREEN = 1
STOPWATCH_SCREEN = 2
DICE_SCREEN = 3
NUMGEN_SCREEN = 4
current_screen = HOME_SCREEN

# Border settings
BORDER_WIDTH = 4
OUTER_RADIUS = 15
INNER_RADIUS = 15
PADDING = 10

# Button settings
button_width = 120
button_height = 40
button_x = (SCREEN_WIDTH - button_width) // 2
button_y = 160
button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

# Main loop
running = True
while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Detect mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if current_screen == HOME_SCREEN and button_rect.collidepoint(mouse_x, mouse_y):
                current_screen = APP_SCREEN
    
    # Clear screen
    screen.fill(BASE)

    if current_screen == HOME_SCREEN:
        # Draw outer border
        pygame.draw.rect(screen, BASE, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT),
                         BORDER_WIDTH, border_radius=OUTER_RADIUS)

        # Inner layer
        inner_rect = pygame.Rect(PADDING, PADDING, SCREEN_WIDTH - 2 * PADDING, SCREEN_HEIGHT - 2 * PADDING)
        pygame.draw.rect(screen, LIGHT_GRAY, inner_rect, border_radius=INNER_RADIUS)

        # Time and date 
        now = datetime.datetime.now()
        time_str = now.strftime("%I:%M")
        date_str = now.strftime("%A, %B %d").lstrip("0").replace(" 0", " ")

        # Render text
        time_surface = font_time.render(time_str, True, GOLD)
        time_rect = time_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))
        screen.blit(time_surface, time_rect)

        date_surface = font_date.render(date_str, True, GOLD)
        date_rect = date_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 10))
        screen.blit(date_surface, date_rect)

        # Hover effect for Enter button
        if button_rect.collidepoint(mouse_x, mouse_y):
            button_color = GOLD
            text_color = RED
        else:
            button_color = RED
            text_color = GOLD

        pygame.draw.rect(screen, button_color, button_rect, border_radius=10)
        button_text_surface = font_button.render("ENTER", True, text_color)
        button_text_rect = button_text_surface.get_rect(center=button_rect.center)
        screen.blit(button_text_surface, button_text_rect)
    
    # Switching between screens
    elif current_screen == APP_SCREEN:
        selected_app = appscreen.run_app_menu(screen)
        if selected_app == "stopwatch":
            current_screen = STOPWATCH_SCREEN
        elif selected_app == "dice":
            current_screen = DICE_SCREEN
        elif selected_app == "numgen":
            current_screen = NUMGEN_SCREEN
        else:
            current_screen = HOME_SCREEN

    elif current_screen == STOPWATCH_SCREEN:
        back_to_app = timerui.run_stopwatch_screen(screen)
        if back_to_app:
            current_screen = APP_SCREEN

    elif current_screen == NUMGEN_SCREEN:
        back_to_app = numgen.run_random_number_screen(screen)
        if back_to_app:
            current_screen = APP_SCREEN

    pygame.display.update()
    time.sleep(0.1)

pygame.quit()
