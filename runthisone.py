import pygame
import sys
import time
import datetime
import random

pygame.init()

# ----------------------
# Global settings
# ----------------------
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 320
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Xi Smartwatch")

# Colors
BLACK      = (0, 0, 0)
WHITE      = (255, 255, 255)
GRAY       = (180, 180, 180)
RED        = (161, 73, 67)
GOLD       = (194, 148, 83)
DARK_GRAY  = (30, 30, 30)
BASE       = (107, 106, 105)
LIGHT_GRAY = (217, 217, 217)
BLUE       = (100, 149, 237)

# Fonts for main screen
font_time   = pygame.font.SysFont("Rubik", 88)
font_date   = pygame.font.SysFont("Rubik", 38)
font_button = pygame.font.SysFont("Rubik", 30)

# Fonts for app menu (appscreen)
app_font = pygame.font.SysFont(None, 30)

# Fonts for numgen (number generator)
numgen_font       = pygame.font.SysFont(None, 36)
numgen_large_font = pygame.font.SysFont(None, 48)

# Screen states
HOME_SCREEN       = 0
APP_SCREEN        = 1
STOPWATCH_SCREEN  = 2
NUMGEN_SCREEN     = 3
COMPLEX_APP_SCREEN = 4
current_screen = HOME_SCREEN

# Border and padding settings
BORDER_WIDTH = 4
OUTER_RADIUS = 15
INNER_RADIUS = 15
PADDING = 10

# Button settings for home screen
button_width = 180
button_height = 70
button_x = (SCREEN_WIDTH - button_width) // 2
button_y = 200
button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

# To prevent multiple screen transitions per click in the main loop
transition_in_progress = False

# ----------------------
# Helper functions to draw rounded rectangles (pygame 1.9.4 compatible)
# ----------------------
def draw_rounded_rect(surface, rect, color, radius):
    """
    Draws a filled rectangle with rounded corners.
    """
    rect = pygame.Rect(rect)
    # Draw the inner (center) rectangle
    inner_rect = rect.inflate(-2 * radius, -2 * radius)
    pygame.draw.rect(surface, color, inner_rect)
    # Draw the side rectangles
    top_rect = pygame.Rect(rect.left + radius, rect.top, rect.width - 2 * radius, radius)
    bottom_rect = pygame.Rect(rect.left + radius, rect.bottom - radius, rect.width - 2 * radius, radius)
    left_rect = pygame.Rect(rect.left, rect.top + radius, radius, rect.height - 2 * radius)
    right_rect = pygame.Rect(rect.right - radius, rect.top + radius, radius, rect.height - 2 * radius)
    pygame.draw.rect(surface, color, top_rect)
    pygame.draw.rect(surface, color, bottom_rect)
    pygame.draw.rect(surface, color, left_rect)
    pygame.draw.rect(surface, color, right_rect)
    # Draw the corner circles
    pygame.draw.circle(surface, color, (rect.left + radius, rect.top + radius), radius)
    pygame.draw.circle(surface, color, (rect.right - radius, rect.top + radius), radius)
    pygame.draw.circle(surface, color, (rect.left + radius, rect.bottom - radius), radius)
    pygame.draw.circle(surface, color, (rect.right - radius, rect.bottom - radius), radius)

def draw_rounded_rect_outline(surface, rect, color, radius, width):
    """
    Draws an outline of a rounded rectangle by drawing successive rounded rects.
    """
    for i in range(width):
        shrunk_rect = pygame.Rect(rect.left + i, rect.top + i, rect.width - 2 * i, rect.height - 2 * i)
        current_radius = max(0, radius - i)
        draw_rounded_rect(surface, shrunk_rect, color, current_radius)

# ----------------------
# appscreen functionality
# ----------------------
# List each app in the menu
menu_items = ["Stopwatch", "Number Generator", "Fitness Tracker"]
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
        # Draw light gray background layer (rounded)
        layer_rect = pygame.Rect(10, 10, SCREEN_WIDTH - 20, SCREEN_HEIGHT - 20)
        draw_rounded_rect(screen, layer_rect, LIGHT_GRAY, 15)

        # Create a subsurface to clip menu items within the light gray area
        scroll_surface = screen.subsurface(scroll_area).copy()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        adjusted_mouse_y = mouse_y - scroll_area.y

        # Draw each menu item within the scroll surface
        for i, item in enumerate(menu_items):
            y_pos = 10 + i * (item_height + spacing) + scroll_offset
            if 0 <= y_pos <= scroll_area.height - item_height:
                container_rect = pygame.Rect(0, y_pos, scroll_area.width, item_height)
                # Check if the mouse is over the item
                if container_rect.collidepoint(mouse_x - scroll_area.x, adjusted_mouse_y):
                    draw_rounded_rect(scroll_surface, container_rect, GOLD, 10)
                    text = app_font.render(item, True, RED)
                else:
                    draw_rounded_rect(scroll_surface, container_rect, RED, 10)
                    text = app_font.render(item, True, GOLD)
                text_rect = text.get_rect(center=container_rect.center)
                scroll_surface.blit(text, text_rect)

        # Blit the clipped scroll surface onto the main screen
        screen.blit(scroll_surface, scroll_area.topleft)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if scroll_area.collidepoint(event.pos):
                    dragging = True
                    start_y = event.pos[1]
            elif event.type == pygame.MOUSEBUTTONUP:
                dragging = False
                # Check for menu selection click
                for i, item in enumerate(menu_items):
                    y_pos = 10 + i * (item_height + spacing) + scroll_offset
                    container_rect = pygame.Rect(0, y_pos, scroll_area.width, item_height)
                    if container_rect.collidepoint(event.pos[0] - scroll_area.x, event.pos[1] - scroll_area.y):
                        # Return lowercase name with spaces removed
                        return item.lower().replace(" ", "")
            elif event.type == pygame.MOUSEMOTION and dragging:
                scroll_offset += event.rel[1]
                scroll_offset = max(min_scroll, min(scroll_offset, max_scroll))
        clock.tick(30)

# ----------------------
# numgen (number generator) functionality
# ----------------------
# Slider settings
slider_x = 50
slider_y = 150
slider_width = 400
slider_height = 5
knob_radius = 10
min_val = 1
max_val = 100

def get_value(knob_x):
    ratio = (knob_x - slider_x) / slider_width
    return int(min_val + ratio * (max_val - min_val))

def draw_slider(screen, knob_x):
    # Draw the slider track
    pygame.draw.rect(screen, WHITE, (slider_x, slider_y - slider_height // 2, slider_width, slider_height))
    # Draw the knob as a circle
    pygame.draw.circle(screen, GOLD, (knob_x, slider_y), knob_radius)

def draw_button(screen, rect, text, hover):
    bg_color = GOLD if hover else RED
    text_color = RED if hover else GOLD
    draw_rounded_rect(screen, rect, bg_color, 10)
    txt = numgen_font.render(text, True, text_color)
    screen.blit(txt, (rect.centerx - txt.get_width() // 2, rect.centery - txt.get_height() // 2))

def run_slider_screen(screen):
    knob_x = slider_x
    dragging = False
    generate_button = pygame.Rect(SCREEN_WIDTH // 2 - 75, 220, 150, 40)
    back_button = pygame.Rect(SCREEN_WIDTH // 2 - 60, 20, 120, 40)
    clock = pygame.time.Clock()

    while True:
        mouse_pos = pygame.mouse.get_pos()
        generate_hover = generate_button.collidepoint(mouse_pos)
        back_hover = back_button.collidepoint(mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if (knob_x - mx)**2 + (slider_y - my)**2 < (knob_radius * 2)**2:
                    dragging = True
                if generate_button.collidepoint(event.pos):
                    return get_value(knob_x)
                if back_button.collidepoint(event.pos):
                    return "back_to_app"
            elif event.type == pygame.MOUSEBUTTONUP:
                dragging = False
            elif event.type == pygame.MOUSEMOTION and dragging:
                mx, _ = pygame.mouse.get_pos()
                knob_x = max(slider_x, min(slider_x + slider_width, mx))
        screen.fill(BASE)
        inner_rect = pygame.Rect(PADDING, PADDING, SCREEN_WIDTH - 2 * PADDING, SCREEN_HEIGHT - 2 * PADDING)
        draw_rounded_rect(screen, inner_rect, LIGHT_GRAY, INNER_RADIUS)
        draw_slider(screen, knob_x)
        value = get_value(knob_x)
        text = numgen_font.render(f"Max: {value}", True, WHITE)
        screen.blit(text, (knob_x - text.get_width() // 2, slider_y - 40))
        draw_button(screen, generate_button, "Generate", generate_hover)
        draw_button(screen, back_button, "Back", back_hover)
        pygame.display.flip()
        clock.tick(60)

def run_num_gen_screen(screen):
    while True:
        max_number = run_slider_screen(screen)
        if max_number == "back_to_app":
            return "back_to_app"
        number = random.randint(1, max_number)
        back_button = pygame.Rect(SCREEN_WIDTH // 2 - 60, 20, 120, 40)
        clock = pygame.time.Clock()
        while True:
            mouse_pos = pygame.mouse.get_pos()
            back_hover = back_button.collidepoint(mouse_pos)
            screen.fill(BASE)
            inner_rect = pygame.Rect(PADDING, PADDING, SCREEN_WIDTH - 2 * PADDING, SCREEN_HEIGHT - 2 * PADDING)
            draw_rounded_rect(screen, inner_rect, LIGHT_GRAY, INNER_RADIUS)
            text = numgen_large_font.render(f"Number: {number}", True, GOLD)
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2,
                               SCREEN_HEIGHT // 2 - text.get_height() // 2))
            draw_button(screen, back_button, "Back", back_hover)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.collidepoint(event.pos):
                        return "back_to_slider"
            pygame.display.flip()
            clock.tick(60)

# ----------------------
# timerui (stopwatch) placeholder functionality
# ----------------------
def run_stopwatch_screen(screen):
    # Stub: Display a placeholder screen and wait for a keypress to return to app menu.
    waiting = True
    clock = pygame.time.Clock()
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False
        screen.fill(DARK_GRAY)
        placeholder_text = font_button.render("Stopwatch Placeholder - Press any key", True, WHITE)
        rect = placeholder_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        screen.blit(placeholder_text, rect)
        pygame.display.flip()
        clock.tick(30)
    return True

# ----------------------
# complexui (complex app) placeholder functionality
# ----------------------
def run_complex_app_screen(screen):
    # Stub: Display a placeholder screen and wait for a keypress to return to app menu.
    waiting = True
    clock = pygame.time.Clock()
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False
        screen.fill(DARK_GRAY)
        placeholder_text = font_button.render("Complex App Placeholder - Press any key", True, WHITE)
        rect = placeholder_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        screen.blit(placeholder_text, rect)
        pygame.display.flip()
        clock.tick(30)
    return True

# ----------------------
# Main loop
# ----------------------
running = True
while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Detect mouse click on HOME_SCREEN for transition
        if event.type == pygame.MOUSEBUTTONDOWN and not transition_in_progress:
            if current_screen == HOME_SCREEN and button_rect.collidepoint(mouse_x, mouse_y):
                transition_in_progress = True
                current_screen = APP_SCREEN

    # Clear screen
    screen.fill(BASE)

    if current_screen == HOME_SCREEN:
        # Draw "outer border" using our outline helper
        outer_rect = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        draw_rounded_rect_outline(screen, outer_rect, BASE, OUTER_RADIUS, BORDER_WIDTH)
        # Draw inner layer
        inner_rect = pygame.Rect(PADDING, PADDING, SCREEN_WIDTH - 2 * PADDING, SCREEN_HEIGHT - 2 * PADDING)
        draw_rounded_rect(screen, inner_rect, LIGHT_GRAY, INNER_RADIUS)
        # Time and date
        now = datetime.datetime.now()
        time_str = now.strftime("%I:%M")
        date_str = now.strftime("%A, %B %d").lstrip("0").replace(" 0", " ")
        time_surface = font_time.render(time_str, True, GOLD)
        time_rect = time_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40))
        screen.blit(time_surface, time_rect)
        date_surface = font_date.render(date_str, True, GOLD)
        date_rect = date_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 10))
        screen.blit(date_surface, date_rect)
        # Draw enter button with hover effect
        if button_rect.collidepoint(mouse_x, mouse_y):
            button_color = GOLD
            text_color = RED
        else:
            button_color = RED
            text_color = GOLD
        draw_rounded_rect(screen, button_rect, button_color, 10)
        button_text_surface = font_button.render("ENTER", True, text_color)
        button_text_rect = button_text_surface.get_rect(center=button_rect.center)
        screen.blit(button_text_surface, button_text_rect)

    elif current_screen == APP_SCREEN:
        selected_app = run_app_menu(screen)
        transition_in_progress = False
        if selected_app == "stopwatch":
            current_screen = STOPWATCH_SCREEN
        elif selected_app == "numbergenerator":
            current_screen = NUMGEN_SCREEN
        elif selected_app == "complex":
            current_screen = COMPLEX_APP_SCREEN
        elif selected_app == "clock":
            current_screen = HOME_SCREEN

    elif current_screen == STOPWATCH_SCREEN:
        back_to_app = run_stopwatch_screen(screen)
        if back_to_app:
            current_screen = APP_SCREEN
            transition_in_progress = True

    elif current_screen == NUMGEN_SCREEN:
        back_to_app = run_num_gen_screen(screen)
        if back_to_app == "back_to_app":
            current_screen = APP_SCREEN
            transition_in_progress = True

    elif current_screen == COMPLEX_APP_SCREEN:
        back_to_app = run_complex_app_screen(screen)
        if back_to_app:
            current_screen = APP_SCREEN
            transition_in_progress = True

    pygame.display.update()
    time.sleep(0.1)

pygame.quit()
