# needed for "import complexui" for main.py
import pygame
import time

pygame.init()

# Screen dimensions
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 320
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Health Tracker")

# Fonts
font_title = pygame.font.SysFont("Rubik", 65)
font_date = pygame.font.SysFont("Rubik", 20)
font_button = pygame.font.SysFont("Rubik", 30)

# Colors
BLACK = (0, 0, 0)
GOLD = (194, 148, 83)
RED = (161, 73, 67)
WHITE = (255, 255, 255)
DARK_GRAY = (30, 30, 30)
BASE = (107, 106, 105)
LIGHT_GRAY = (217, 217, 217)

# Screen states
MAIN_SCREEN = 0
IDLE_SCREEN = 1
ACTIVE_SCREEN = 2
DAILY_SCREEN = 3
WEEKLY_SCREEN = 4
current_screen = MAIN_SCREEN

# Border settings
BORDER_WIDTH = 4
OUTER_RADIUS = 15
INNER_RADIUS = 15
PADDING = 10

# Button settings
button_width = 120
button_height = 50
button_spacing = 20

total_width = button_width * 2 + button_spacing
start_x = (SCREEN_WIDTH - total_width) // 2
button_y = 180

left_button_rect = pygame.Rect(start_x, button_y, button_width, button_height)
right_button_rect = pygame.Rect(start_x + button_width + button_spacing, button_y, button_width, button_height)

# Main loop
running = True
while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Detect mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if current_screen == MAIN_SCREEN:
                if left_button_rect.collidepoint(mouse_x, mouse_y):
                    current_screen = IDLE_SCREEN
                elif right_button_rect.collidepoint(mouse_x, mouse_y):
                    current_screen = ACTIVE_SCREEN  # define this screen if needed
    
    # Clear screen
    screen.fill(BASE)

    if current_screen == MAIN_SCREEN:
        # Draw outer border
        pygame.draw.rect(screen, BASE, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT),
                         BORDER_WIDTH, border_radius=OUTER_RADIUS)

        # Inner layer
        inner_rect = pygame.Rect(PADDING, PADDING, SCREEN_WIDTH - 2 * PADDING, SCREEN_HEIGHT - 2 * PADDING)
        pygame.draw.rect(screen, LIGHT_GRAY, inner_rect, border_radius=INNER_RADIUS)

        # Render text
        title1_str = "Health"
        title1_surface = font_title.render(title1_str, True, RED)
        title1_rect = title1_surface.get_rect(center=(SCREEN_WIDTH // 2, 80))
        screen.blit(title1_surface, title1_rect)

        title2_str = "Tracker"
        title2_surface = font_title.render(title2_str, True, GOLD)
        title2_rect = title2_surface.get_rect(center=(SCREEN_WIDTH // 2, 140))
        screen.blit(title2_surface, title2_rect)

        # IDLE button hover effect
        if left_button_rect.collidepoint(mouse_x, mouse_y):
            left_color = GOLD
            left_text_color = RED
        else:
            left_color = RED
            left_text_color = GOLD

        # ACTIVE button hover effect
        if right_button_rect.collidepoint(mouse_x, mouse_y):
            right_color = GOLD
            right_text_color = RED
        else:
            right_color = RED
            right_text_color = GOLD

        # Draw IDLE button
        pygame.draw.rect(screen, left_color, left_button_rect, border_radius=10)
        left_text_surface = font_button.render("IDLE", True, left_text_color)
        left_text_rect = left_text_surface.get_rect(center=left_button_rect.center)
        screen.blit(left_text_surface, left_text_rect)

        # Draw ACTIVE button
        pygame.draw.rect(screen, right_color, right_button_rect, border_radius=10)
        right_text_surface = font_button.render("ACTIVE", True, right_text_color)
        right_text_rect = right_text_surface.get_rect(center=right_button_rect.center)
        screen.blit(right_text_surface, right_text_rect)
    
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