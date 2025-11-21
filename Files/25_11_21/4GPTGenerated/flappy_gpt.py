import pygame
import random
import sys

# --- CONFIG ---
WIDTH, HEIGHT = 400, 600
FPS = 60

BIRD_X = 80
GRAVITY = 0.4
FLAP_STRENGTH = -8
PIPE_SPEED = -3
PIPE_GAP = 150
PIPE_DISTANCE = 220

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird (Baby)")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 32)


class Bird:
    def __init__(self):
        self.x = BIRD_X
        self.y = HEIGHT // 2
        self.vel_y = 0
        self.radius = 15

    def flap(self):
        self.vel_y = FLAP_STRENGTH

    def update(self):
        self.vel_y += GRAVITY
        self.y += self.vel_y

    def rect(self):
        return pygame.Rect(
            self.x - self.radius,
            self.y - self.radius,
            self.radius * 2,
            self.radius * 2,
        )

    def draw(self, surf):
        pygame.draw.circle(surf, (255, 255, 0), (int(self.x), int(self.y)), self.radius)


class PipePair:
    def __init__(self, x):
        self.x = x
        self.width = 60
        self.gap_y = random.randint(150, HEIGHT - 150)
        self.passed = False

    def update(self):
        self.x += PIPE_SPEED

    def off_screen(self):
        return self.x + self.width < 0

    def rects(self):
        top_rect = pygame.Rect(
            self.x, 0, self.width, self.gap_y - PIPE_GAP // 2
        )
        bottom_rect = pygame.Rect(
            self.x, self.gap_y + PIPE_GAP // 2, self.width, HEIGHT - self.gap_y
        )
        return top_rect, bottom_rect

    def draw(self, surf):
        top_rect, bottom_rect = self.rects()
        pygame.draw.rect(surf, (0, 200, 0), top_rect)
        pygame.draw.rect(surf, (0, 200, 0), bottom_rect)


def draw_text(surf, text, size, x, y):
    f = pygame.font.SysFont("Arial", size, bold=True)
    img = f.render(text, True, (255, 255, 255))
    rect = img.get_rect(center=(x, y))
    surf.blit(img, rect)


def main():
    while True:
        run_game()


def run_game():
    bird = Bird()
    pipes = [PipePair(WIDTH + 100), PipePair(WIDTH + 100 + PIPE_DISTANCE)]
    score = 0
    running = True

    while running:
        clock.tick(FPS)

        # --- INPUT ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_SPACE, pygame.K_UP):
                    bird.flap()

        # --- UPDATE ---
        bird.update()

        # floor/ceiling collision
        if bird.y - bird.radius <= 0 or bird.y + bird.radius >= HEIGHT:
            running = False

        for pipe in pipes:
            pipe.update()

        # add new pipes and remove old ones
        if pipes[0].off_screen():
            pipes.pop(0)
            pipes.append(PipePair(pipes[-1].x + PIPE_DISTANCE))

        # collision + scoring
        bird_rect = bird.rect()
        for pipe in pipes:
            top_rect, bottom_rect = pipe.rects()
            if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect):
                running = False
            if not pipe.passed and pipe.x + pipe.width < bird.x:
                pipe.passed = True
                score += 1

        # --- DRAW ---
        screen.fill((30, 30, 60))  # background
        for pipe in pipes:
            pipe.draw(screen)
        bird.draw(screen)
        score_img = font.render(str(score), True, (255, 255, 255))
        screen.blit(score_img, (WIDTH // 2 - score_img.get_width() // 2, 20))

        pygame.display.flip()

    # game over screen
    game_over_screen(score)


def game_over_screen(score):
    wait = True
    while wait:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # restart on any key
                wait = False

        screen.fill((20, 20, 20))
        draw_text(screen, "GAME OVER", 40, WIDTH // 2, HEIGHT // 3)
        draw_text(screen, f"Score: {score}", 32, WIDTH // 2, HEIGHT // 2)
        draw_text(screen, "Press any key to retry", 20, WIDTH // 2, HEIGHT * 2 // 3)

        pygame.display.flip()


if __name__ == "__main__":
    main()