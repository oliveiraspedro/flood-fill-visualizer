import sys
import pygame

from floodfill.core.grid import Grid
from floodfill.core.flood_fill import flood_fill_bfs
from floodfill.rendering.renderer import Renderer
from floodfill.rendering.panel import Panel

WINDOW_TITLE = "Flood Fill Visualizer"
BACKGROUND_COLOR = (30, 30, 30)
TARGET_FPS = 60

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

GRID_ROWS = 20
GRID_COLS = 20
CELL_WIDTH_SIZE = int(((2 * WINDOW_WIDTH) / 3) / GRID_COLS)
CELL_HEIGHT_SIZE = int(WINDOW_HEIGHT / GRID_ROWS)
MOUSE_OFFSET_X = 0
MOUSE_OFFSET_Y = 0

def main() -> None:
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)

    clock = pygame.time.Clock()
    
    grid = Grid(rows=GRID_ROWS, cols=GRID_COLS)
    renderer = Renderer(surface=screen, cell_width_size=CELL_WIDTH_SIZE, cell_height_size=CELL_HEIGHT_SIZE)
    panel = Panel(surface=screen, window_width=WINDOW_WIDTH, window_height=WINDOW_HEIGHT)

    running = True
    gerador = None
    while running:
        ev = pygame.event.get()
        x, y = pygame.mouse.get_pos()
        panel.get_speed()
        for event in ev:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                panel.handle_color_selection(x, y)
                row = int(y // CELL_HEIGHT_SIZE)
                col = int(x // CELL_WIDTH_SIZE)
                if event.button == 1 and row >= 0 and row < GRID_ROWS and col >= 0 and col < GRID_COLS:
                    print("Starting the algorithm...")
                    print(f"Mouse clicked on the cell ({row, col})")
                    gerador = flood_fill_bfs(grid, row, col, panel.get_selected_color())

            if pygame.mouse.get_pressed()[0]:
                panel.handle_slider(x, y)

            if pygame.mouse.get_pressed()[2]:
                row = int(y // CELL_HEIGHT_SIZE)
                col = int(x  // CELL_WIDTH_SIZE)
                if row >= 0 and row < GRID_ROWS and col >= 0 and col < GRID_COLS:
                    print("Drawing on the cell...")
                    print(f"Mouse clicked on the cell ({row, col})")
                    grid.set_color(row, col, (0, 0, 0))

            
        screen.fill(BACKGROUND_COLOR)
        if gerador:
            try:
                next(gerador)
            except StopIteration:
                gerador = None
                pass
        renderer.draw_grid(grid)
        panel.draw()
        pygame.display.flip()

        clock.tick(TARGET_FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()