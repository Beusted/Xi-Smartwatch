import time
import pygame
import sys

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((240, 240))
pygame.display.set_caption("Timer & Stopwatch")
font = pygame.font.SysFont(None, 36)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Draw text

def draw_text(text, x, y):
    txt_surface = font.render(text, True, BLACK)
    screen.blit(txt_surface, (x, y))

# Button class
class Button:
    def __init__(self, rect, text):
        self.rect = pygame.Rect(rect)
        self.text = text

    def draw(self):
        pygame.draw.rect(screen, GRAY, self.rect)
        draw_text(self.text, self.rect.x + 10, self.rect.y + 10)

    def is_pressed(self, pos):
        return self.rect.collidepoint(pos)

# Format time to HH:MM:SS

def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

# Main app

def run_timer_app():
    mode = None
    running = False
    start_time = 0
    elapsed = 0

    timer_btn = Button((20, 20, 90, 40), "Timer")
    sw_btn = Button((130, 20, 90, 40), "Stopwatch")
    start_btn = Button((20, 180, 60, 40), "Start")
    stop_btn = Button((90, 180, 60, 40), "Stop")
    reset_btn = Button((160, 180, 60, 40), "Reset")

    while True:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if timer_btn.is_pressed(pos):
                    mode = "Timer"
                    elapsed = 0
                elif sw_btn.is_pressed(pos):
                    mode = "Stopwatch"
                    elapsed = 0
                elif start_btn.is_pressed(pos):
                    if not running:
                        start_time = time.time() - elapsed
                        running = True
                elif stop_btn.is_pressed(pos):
                    if running:
                        elapsed = time.time() - start_time
                        running = False
                elif reset_btn.is_pressed(pos):
                    running = False
                    elapsed = 0

        # Timer logic
        if running:
            elapsed = time.time() - start_time

        # Display selected mode
        if mode:
            draw_text(f"Mode: {mode}", 60, 80)
            draw_text(format_time(elapsed), 60, 120)

        # Draw buttons
        timer_btn.draw()
        sw_btn.draw()
        start_btn.draw()
        stop_btn.draw()
        reset_btn.draw()

        pygame.display.flip()
        pygame.time.Clock().tick(30)

if __name__ == '__main__':
    run_timer_app()
