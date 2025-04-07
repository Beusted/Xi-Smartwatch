import time
import pygame
import sys

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((360, 480))
pygame.display.set_caption("Timer & Stopwatch")
font = pygame.font.SysFont(None, 32)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (100, 149, 237)

# Draw text
def draw_text(text, x, y, center=False):
    txt_surface = font.render(text, True, BLACK)
    if center:
        rect = txt_surface.get_rect(center=(x, y))
        screen.blit(txt_surface, rect)
    else:
        screen.blit(txt_surface, (x, y))

# Button class
class Button:
    def __init__(self, rect, text):
        self.rect = pygame.Rect(rect)
        self.text = text

    def draw(self):
        pygame.draw.rect(screen, GRAY, self.rect, border_radius=8)
        draw_text(self.text, self.rect.centerx, self.rect.centery, center=True)

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
    timer_seconds = 0

    # Main buttons
    timer_btn = Button((50, 20, 120, 40), "Timer")
    sw_btn = Button((190, 20, 120, 40), "Stopwatch")
    start_btn = Button((30, 420, 90, 40), "Start")
    stop_btn = Button((135, 420, 90, 40), "Stop")
    reset_btn = Button((240, 420, 90, 40), "Reset")

    # Increment buttons (top half)
    inc_h1 = Button((30, 80, 70, 40), "+1h")
    inc_h5 = Button((30, 130, 70, 40), "+5h")
    inc_m1 = Button((145, 80, 70, 40), "+1m")
    inc_m5 = Button((145, 130, 70, 40), "+5m")
    inc_s1 = Button((260, 80, 70, 40), "+1s")
    inc_s5 = Button((260, 130, 70, 40), "+5s")

    # Decrement buttons (bottom half)
    dec_h1 = Button((30, 180, 70, 40), "-1h")
    dec_h5 = Button((30, 230, 70, 40), "-5h")
    dec_m1 = Button((145, 180, 70, 40), "-1m")
    dec_m5 = Button((145, 230, 70, 40), "-5m")
    dec_s1 = Button((260, 180, 70, 40), "-1s")
    dec_s5 = Button((260, 230, 70, 40), "-5s")

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
                    timer_seconds = 0
                    running = False
                elif sw_btn.is_pressed(pos):
                    mode = "Stopwatch"
                    elapsed = 0
                    running = False
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
                    if mode == "Timer":
                        timer_seconds = 0

                if mode == "Timer" and not running:
                    if inc_h1.is_pressed(pos):
                        timer_seconds += 3600
                    elif inc_h5.is_pressed(pos):
                        timer_seconds += 5 * 3600
                    elif inc_m1.is_pressed(pos):
                        timer_seconds += 60
                    elif inc_m5.is_pressed(pos):
                        timer_seconds += 5 * 60
                    elif inc_s1.is_pressed(pos):
                        timer_seconds += 1
                    elif inc_s5.is_pressed(pos):
                        timer_seconds += 5
                    elif dec_h1.is_pressed(pos):
                        timer_seconds = max(0, timer_seconds - 3600)
                    elif dec_h5.is_pressed(pos):
                        timer_seconds = max(0, timer_seconds - 5 * 3600)
                    elif dec_m1.is_pressed(pos):
                        timer_seconds = max(0, timer_seconds - 60)
                    elif dec_m5.is_pressed(pos):
                        timer_seconds = max(0, timer_seconds - 5 * 60)
                    elif dec_s1.is_pressed(pos):
                        timer_seconds = max(0, timer_seconds - 1)
                    elif dec_s5.is_pressed(pos):
                        timer_seconds = max(0, timer_seconds - 5)

        if running:
            elapsed = time.time() - start_time

        if mode:
            draw_text(f"Mode: {mode}", 180, 280, center=True)
            current_time = timer_seconds - elapsed if mode == "Timer" else elapsed
            current_time = max(0, current_time)
            draw_text(format_time(current_time), 180, 320, center=True)

        # Draw common buttons
        timer_btn.draw()
        sw_btn.draw()
        start_btn.draw()
        stop_btn.draw()
        reset_btn.draw()

        if mode == "Timer" and not running:
            inc_h1.draw()
            inc_h5.draw()
            inc_m1.draw()
            inc_m5.draw()
            inc_s1.draw()
            inc_s5.draw()
            dec_h1.draw()
            dec_h5.draw()
            dec_m1.draw()
            dec_m5.draw()
            dec_s1.draw()
            dec_s5.draw()

        pygame.display.flip()
        pygame.time.Clock().tick(30)

if __name__ == '__main__':
    run_timer_app()