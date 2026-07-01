import sys
import pygame

from floodfill.core.grid import Grid
from floodfill.rendering.renderer import Renderer

WINDOW_TITLE = "Flood Fill Visualizer"
BACKGROUND_COLOR = (30, 30, 30)
TARGET_FPS = 60

GRID_ROWS = 20
GRID_COLS = 20
CELL_SIZE = 30

WINDOW_WIDTH = GRID_ROWS * CELL_SIZE
WINDOW_HEIGHT = GRID_COLS * CELL_SIZE

def main() -> None:
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)

    clock = pygame.time.Clock()
    
    grid = Grid(rows=GRID_ROWS, cols=GRID_COLS)
    renderer = Renderer(surface=screen, cell_size=CELL_SIZE)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(BACKGROUND_COLOR)
        renderer.draw_grid(grid)
        pygame.display.flip()

        clock.tick(TARGET_FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()