import pygame
import sys
import random

# Screen dimentions
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 320
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (161, 73, 67)
GOLD = (194, 148, 83)
BASE = (107, 106, 105)
BLUE = (100, 200, 255)
GRAY = (200, 200, 200)
DARK_BG = (30, 30, 30)
LIGHT_GRAY = (217, 217, 217)

# Fonts
pygame.init()
font = pygame.font.SysFont(None, 36)
large_font = pygame.font.SysFont(None, 48)

# Slider settings
slider_x = 50
slider_y = 150
slider_width = 400
slider_height = 5
knob_radius = 10
min_val = 1
max_val = 100

# Border settings
BORDER_WIDTH = 4
OUTER_RADIUS = 15
INNER_RADIUS = 15
PADDING = 10

def get_value(knob_x):
    ratio = (knob_x - slider_x) / slider_width
    return int(min_val + ratio * (max_val - min_val))

# Colors for the slider
def draw_slider(screen, knob_x):
    pygame.draw.rect(screen, WHITE, (slider_x, slider_y - slider_height // 2, slider_width, slider_height))
    pygame.draw.circle(screen, GOLD, (knob_x, slider_y), knob_radius)

def draw_button(screen, rect, text, hover):
    bg_color = GOLD if hover else RED
    text_color = RED if hover else GOLD
    pygame.draw.rect(screen, bg_color, rect, border_radius=10)
    txt = font.render(text, True, text_color)
    screen.blit(txt, (rect.centerx - txt.get_width() // 2, rect.centery - txt.get_height() // 2))

def run_slider_screen(screen):
    knob_x = slider_x
    dragging = False
    generate_button = pygame.Rect(SCREEN_WIDTH // 2 - 75, 220, 150, 40)
    back_button = pygame.Rect(SCREEN_WIDTH // 2 - 60, 20, 120, 40)

    while True:
        mouse_pos = pygame.mouse.get_pos()
        generate_hover = generate_button.collidepoint(mouse_pos)
        back_hover = back_button.collidepoint(mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if (knob_x - mx)**2 + (slider_y - my)**2 < knob_radius**2 * 4:
                    dragging = True
                if generate_button.collidepoint(event.pos):
                    return get_value(knob_x)
                if back_button.collidepoint(event.pos):
                    return "back_to_app"  # Return a special value to indicate going back to app screen

            elif event.type == pygame.MOUSEBUTTONUP:
                dragging = False

            elif event.type == pygame.MOUSEMOTION and dragging:
                mx, _ = pygame.mouse.get_pos()
                knob_x = max(slider_x, min(slider_x + slider_width, mx))

        screen.fill(BASE)
        inner_rect = pygame.Rect(PADDING, PADDING, SCREEN_WIDTH - 2 * PADDING, SCREEN_HEIGHT - 2 * PADDING)
        pygame.draw.rect(screen, LIGHT_GRAY, inner_rect, border_radius=INNER_RADIUS)
        draw_slider(screen, knob_x)

        value = get_value(knob_x)
        text = font.render(f"Max: {value}", True, WHITE)
        screen.blit(text, (knob_x - text.get_width() // 2, slider_y - 40))

        draw_button(screen, generate_button, "Generate", generate_hover)
        draw_button(screen, back_button, "Back", back_hover)

        pygame.display.flip()
        clock.tick(60)

def run_num_gen_screen(screen):
    while True:
        max_number = run_slider_screen(screen)
        if max_number == "back_to_app":
            return "back_to_app"  # Go back to app screen

        number = random.randint(1, max_number)
        back_button = pygame.Rect(SCREEN_WIDTH // 2 - 60, 20, 120, 40)

        while True:
            mouse_pos = pygame.mouse.get_pos()
            back_hover = back_button.collidepoint(mouse_pos)

            screen.fill(BASE)

            inner_rect = pygame.Rect(PADDING, PADDING, SCREEN_WIDTH - 2 * PADDING, SCREEN_HEIGHT - 2 * PADDING)
            pygame.draw.rect(screen, LIGHT_GRAY, inner_rect, border_radius=INNER_RADIUS)

            text = large_font.render(f"Number: {number}", True, GOLD)
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))

            draw_button(screen, back_button, "Back", back_hover)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.collidepoint(event.pos):
                        return "back_to_slider"

            pygame.display.update()
