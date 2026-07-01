Color = tuple[int, int, int]

COLOR_WHITE: Color = (255, 255, 255)
COLOR_BLACK: Color = (0, 0, 0)

class Grid:
    def __init__(
        self,
        rows: int,
        cols: int,
        default_color: Color = COLOR_WHITE,
    ) -> None:
        self.rows = rows
        self.cols = cols
        self.default_color = default_color
        self._cells: list[list[Color]] = self._build_grid()

    def _build_grid(self) -> list[list[Color]]:
        """Cria a matriz 2D preenchida com a cor padrão."""
        return [
            [self.default_color for _ in range(self.cols)]
            for _ in range(self.rows)
        ]

    def get_color(self, row: int, col: int) -> Color:
        """Retorna a cor da célula na posição (row, col)."""
        return self._cells[row][col]

    def set_color(self, row: int, col: int, color: Color) -> None:
        """Define a cor da célula na posição (row, col)."""
        self._cells[row][col] = color

    def is_valid_position(self, row: int, col: int) -> bool:
        """Verifica se a posição (row, col) está dentro dos limites do grid."""
        return 0 <= row < self.rows and 0 <= col < self.cols

    def reset(self) -> None:
        """Restaura todas as células para a cor padrão."""
        self._cells = self._build_grid()