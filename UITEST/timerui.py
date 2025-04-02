import pygame
import time

pygame.init()

SCREEN_WIDTH = 320
SCREEN_HEIGHT = 230
font_large = pygame.font.SysFont(None, 50)
font_small = pygame.font.SysFont(None, 24)

WHITE = (255, 255, 255)
GOLD = (194, 148, 83)
RED = (161, 73, 67)
LIGHT_GRAY = (217, 217, 217)
BASE = (107, 106, 105)

# Stopwatch logic class
class Stopwatch:
    def __init__(self):
        self.start_time = 0
        self.elapsed_time = 0
        self.running = False

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True

    def pause(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.running = False

    def reset(self):
        self.start_time = 0
        self.elapsed_time = 0
        self.running = False

    def get_time(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
        return self.elapsed_time

# Stopwatch screen function
def run_stopwatch_screen(screen):
    clock = pygame.time.Clock()
    stopwatch = Stopwatch()
    running = True

    while running:
        screen.fill(BASE)

        # Draw background layer
        layer_rect = pygame.Rect(10, 10, SCREEN_WIDTH - 20, SCREEN_HEIGHT - 20)
        pygame.draw.rect(screen, LIGHT_GRAY, layer_rect, border_radius=15)

        # Back button centered at top
        back_rect = pygame.Rect((SCREEN_WIDTH - 60) // 2, 20, 60, 30)
        pygame.draw.rect(screen, RED, back_rect, border_radius=5)
        back_text = font_small.render("Back", True, GOLD)
        back_text_rect = back_text.get_rect(center=back_rect.center)
        screen.blit(back_text, back_text_rect)

        # Stopwatch time display
        elapsed = stopwatch.get_time()
        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)
        millis = int((elapsed * 100) % 100)
        time_str = f"{minutes:02}:{seconds:02}:{millis:02}"

        time_surface = font_large.render(time_str, True, GOLD)
        time_rect = time_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(time_surface, time_rect)

        # Play button (bottom left)
        play_rect = pygame.Rect(30, SCREEN_HEIGHT - 50, 80, 30)
        pygame.draw.rect(screen, RED, play_rect, border_radius=5)
        play_text = font_small.render("Play", True, GOLD)
        play_text_rect = play_text.get_rect(center=play_rect.center)
        screen.blit(play_text, play_text_rect)

        # Pause button (bottom right)
        pause_rect = pygame.Rect(SCREEN_WIDTH - 110, SCREEN_HEIGHT - 50, 80, 30)
        pygame.draw.rect(screen, RED, pause_rect, border_radius=5)
        pause_text = font_small.render("Pause", True, GOLD)
        pause_text_rect = pause_text.get_rect(center=pause_rect.center)
        screen.blit(pause_text, pause_text_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if back_rect.collidepoint(mouse_x, mouse_y):
                    return True  # Go back to app screen
                elif play_rect.collidepoint(mouse_x, mouse_y):
                    stopwatch.start()
                elif pause_rect.collidepoint(mouse_x, mouse_y):
                    stopwatch.pause()

        clock.tick(30)
