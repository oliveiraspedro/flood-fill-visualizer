
from collections import deque

def flood_fill_bfs(grid, linha, coluna, cor_nova):
    cor_antiga = grid.get_color(linha, coluna)
    
    if cor_antiga == cor_nova:
        return

    fila = deque()
    visitados = set()

    fila.append((linha, coluna))
    visitados.add((linha, coluna))

    while fila:
        i, j = fila.popleft()

        grid.set_color(i, j, cor_nova)
   
        for di, dj in [(-1, 0), (1,0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj

            if ni < 0 or ni >= len(grid) or nj < 0 or nj >= len(grid[0]):
                continue

            if (ni, nj) in visitados:
                continue

            if grid.get_color(ni, nj) != cor_antiga:
                continue

            visitados.add((ni, nj))
            fila.append((ni, nj))

        yield grid