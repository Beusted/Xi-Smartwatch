# import pygame
# import time
# import datetime
# import appscreen

# # Initialize Pygame
# pygame.init()
# SCREEN_WIDTH = 320
# SCREEN_HEIGHT = 230
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Xi Smartwatch")

# # Fonts
# font_time = pygame.font.SysFont("Rubik", 64)
# font_date = pygame.font.SysFont("Rubik", 25)
# font_button = pygame.font.SysFont("Rubik", 20)

# # Colors
# BLACK = (0, 0, 0)
# GOLD = (194, 148, 83)
# RED = (161, 73, 67)
# WHITE = (255, 255, 255)
# DARK_GRAY = (30, 30, 30)
# BASE = (107, 106, 105)
# LIGHT_GRAY = (217, 217, 217)

# # Screen States
# HOME_SCREEN = 0
# APP_SCREEN = 1
# current_screen = HOME_SCREEN

# # Border Settings
# BORDER_WIDTH = 4
# OUTER_RADIUS = 15
# INNER_RADIUS = 20
# PADDING = 10

# # Button Settings
# button_width = 120
# button_height = 40
# button_x = (SCREEN_WIDTH - button_width) // 2
# button_y = 160
# button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

# # Main Loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#         # Keyboard input: Press ENTER to go to APP_SCREEN
#         if event.type == pygame.KEYDOWN:
#             if current_screen == HOME_SCREEN and event.key == pygame.K_RETURN:
#                 current_screen = APP_SCREEN

#     # Clear screen
#     screen.fill(BASE)

#     if current_screen == HOME_SCREEN:
#         # Draw outer border
#         pygame.draw.rect(screen, BASE, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT),
#                          BORDER_WIDTH, border_radius=OUTER_RADIUS)

#         # Inner rounded box
#         inner_rect = pygame.Rect(PADDING, PADDING, SCREEN_WIDTH - 2 * PADDING, SCREEN_HEIGHT - 2 * PADDING)
#         pygame.draw.rect(screen, LIGHT_GRAY, inner_rect, border_radius=INNER_RADIUS)

#         # Time and Date
#         now = datetime.datetime.now()
#         time_str = now.strftime("%I:%M")
#         date_str = now.strftime("%A, %B %d").lstrip("0").replace(" 0", " ")

#         # Render the time and date text
#         time_surface = font_time.render(time_str, True, GOLD)
#         time_rect = time_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))
#         screen.blit(time_surface, time_rect)

#         date_surface = font_date.render(date_str, True, GOLD)
#         date_rect = date_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 10))
#         screen.blit(date_surface, date_rect)

#         # Draw Button (static)
#         pygame.draw.rect(screen, RED, button_rect, border_radius=10)

#         # Button Text
#         button_text_surface = font_button.render("ENTER", True, GOLD)
#         button_text_rect = button_text_surface.get_rect(center=button_rect.center)
#         screen.blit(button_text_surface, button_text_rect)

#     elif current_screen == APP_SCREEN:
#         # Call the App Screen menu and wait until user exits
#         appscreen.run_app_menu(screen)
#         current_screen = HOME_SCREEN  # Return to Home Screen after exiting menu

#     # Update display
#     pygame.display.update()
#     time.sleep(0.1)

# pygame.quit()

import pygame
import time
import datetime
import appscreen

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
RED = (161, 73, 67)
WHITE = (255, 255, 255)
DARK_GRAY = (30, 30, 30)
BASE = (107, 106, 105)
LIGHT_GRAY = (217, 217, 217)

# Screen States
HOME_SCREEN = 0
APP_SCREEN = 1
current_screen = HOME_SCREEN

# Border Settings
BORDER_WIDTH = 4
OUTER_RADIUS = 15  # Uniform rounded corners for all rectangles
INNER_RADIUS = 15  # Same as OUTER_RADIUS for consistency
PADDING = 10

# Button Settings
button_width = 120
button_height = 40
button_x = (SCREEN_WIDTH - button_width) // 2
button_y = 160
button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard input: Press ENTER to go to APP_SCREEN
        if event.type == pygame.KEYDOWN:
            if current_screen == HOME_SCREEN and event.key == pygame.K_RETURN:
                current_screen = APP_SCREEN

    # Clear screen
    screen.fill(BASE)

    if current_screen == HOME_SCREEN:
        # Draw outer border with consistent rounded corners
        pygame.draw.rect(screen, BASE, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT),
                         BORDER_WIDTH, border_radius=OUTER_RADIUS)

        # Inner rounded box with consistent rounded corners
        inner_rect = pygame.Rect(PADDING, PADDING, SCREEN_WIDTH - 2 * PADDING, SCREEN_HEIGHT - 2 * PADDING)
        pygame.draw.rect(screen, LIGHT_GRAY, inner_rect, border_radius=INNER_RADIUS)

        # Time and Date
        now = datetime.datetime.now()
        time_str = now.strftime("%I:%M")
        date_str = now.strftime("%A, %B %d").lstrip("0").replace(" 0", " ")

        # Render the time and date text
        time_surface = font_time.render(time_str, True, GOLD)
        time_rect = time_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))
        screen.blit(time_surface, time_rect)

        date_surface = font_date.render(date_str, True, GOLD)
        date_rect = date_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 10))
        screen.blit(date_surface, date_rect)

        # Draw Button (static) with consistent rounded corners
        pygame.draw.rect(screen, RED, button_rect, border_radius=10)

        # Button Text
        button_text_surface = font_button.render("ENTER", True, GOLD)
        button_text_rect = button_text_surface.get_rect(center=button_rect.center)
        screen.blit(button_text_surface, button_text_rect)

    elif current_screen == APP_SCREEN:
        # Call the App Screen menu and wait until user exits
        appscreen.run_app_menu(screen)
        current_screen = HOME_SCREEN  # Return to Home Screen after exiting menu

    # Update display
    pygame.display.update()
    time.sleep(0.1)

pygame.quit()
