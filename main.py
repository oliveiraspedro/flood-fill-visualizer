import sys
import pygame

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Flood Fill Visualizer"
BACKGROUND_COLOR = (30, 30, 30)
TARGET_FPS = 60

def main() -> None:
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(BACKGROUND_COLOR)
        pygame.display.flip()

        clock.tick(TARGET_FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()