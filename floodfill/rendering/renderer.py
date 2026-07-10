"""
Módulo responsável por renderizar o estado do grid na tela usando Pygame.

Este módulo conhece o Pygame e a Surface de desenho, mas não conhece
a lógica do algoritmo Flood Fill — apenas "lê" o estado do Grid e
o traduz em pixels na tela (View na separação Model-View).
"""

import pygame

from floodfill.core.grid import Grid, Color

GRID_LINE_COLOR: Color = (50, 50, 50)
CELL_BORDER_WIDTH: int = 1


class Renderer:
    def __init__(self, surface: pygame.Surface, cell_width_size: int, cell_height_size: int) -> None:
        self.surface = surface
        self.cell_width_size = cell_width_size
        self.cell_height_size = cell_height_size

    def draw_grid(self, grid: Grid) -> None:
        """Desenha todas as células do grid na surface."""
        for row in range(grid.rows):
            for col in range(grid.cols):
                self._draw_cell(row, col, grid.get_color(row, col))

    def _draw_cell(self, row: int, col: int, color: Color) -> None:
        """Desenha uma única célula na posição (row, col) com a cor dada."""
        pixel_x = col * self.cell_width_size
        pixel_y = row * self.cell_height_size

        cell_rect = pygame.Rect(
            pixel_x,
            pixel_y,
            self.cell_width_size,
            self.cell_height_size,
        )

        pygame.draw.rect(self.surface, color, cell_rect)

        pygame.draw.rect(
            self.surface,
            GRID_LINE_COLOR,
            cell_rect,
            CELL_BORDER_WIDTH,
        )