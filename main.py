import sys
import pygame

from floodfill.core.grid import Grid
from floodfill.core.flood_fill import flood_fill_bfs
from floodfill.rendering.renderer import Renderer

WINDOW_TITLE = "Flood Fill Visualizer"
BACKGROUND_COLOR = (30, 30, 30)
TARGET_FPS = 60

GRID_ROWS = 20
GRID_COLS = 20
CELL_SIZE = 30
MOUSE_OFFSET_X = 0
MOUSE_OFFSET_Y = 0

WINDOW_WIDTH = GRID_COLS* CELL_SIZE
WINDOW_HEIGHT = GRID_ROWS * CELL_SIZE

def main() -> None:
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)

    clock = pygame.time.Clock()
    
    grid = Grid(rows=GRID_ROWS, cols=GRID_COLS)
    renderer = Renderer(surface=screen, cell_size=CELL_SIZE)

    running = True
    gerador = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row = (y - MOUSE_OFFSET_Y ) // CELL_SIZE
                col = (x - MOUSE_OFFSET_X) // CELL_SIZE
                print(f"Mouse clicked on the cell ({row, col})")
                gerador = flood_fill_bfs(grid, row, col, (200, 50, 50))
        
        screen.fill(BACKGROUND_COLOR)
        if gerador:
            try:
                next(gerador)
            except StopIteration:
                gerador = None
                pass
        renderer.draw_grid(grid)
        pygame.display.flip()

        clock.tick(TARGET_FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()