#!/usr/bin/env python3
import sys
import collections
import pygame
import random
import time
import math

# Configurações de visualização
CELL_SIZE = 40   # pixels por célula
MARGIN    = 2    # margem entre células
FPS       = 30   # frames por segundo

# Espaço para legenda (pixels)
LEGEND_WIDTH = 150

# Paleta de cores para regiões
PALETTE = {1: (0, 0, 0)}  # 1 = obstáculo

# Gera grid randômico com probabilidade de obstáculo
def generate_random_grid(n, m, obstacle_prob=0.3):
    return [[1 if random.random() < obstacle_prob else 0 for _ in range(m)] for _ in range(n)]

# Lê dimensões e modo de geração do grid
def read_inputs():
    print('Bem-vindo ao FloodFill Interativo!')
    # dimensões
    while True:
        try:
            n = int(input('Número de linhas (n)? '))
            m = int(input('Número de colunas (m)? '))
            if n <= 0 or m <= 0:
                raise ValueError
            break
        except ValueError:
            print('Entrada inválida. Digite inteiros positivos para n e m.')
    # modo de geração
    mode = ''
    while mode not in ('A', 'M'):
        mode = input('Gerar grid automaticamente ou manualmente? [A/M]: ').strip().upper()
    if mode == 'A':
        print('Gerando grid aleatório...')
        grid = generate_random_grid(n, m)
        print('Grid gerado:')
        for row in grid:
            print(' '.join(str(cell) for cell in row))
    else:
        print(f'Insira o grid {n}×{m}, linha a linha:')
        print('0 = livre, 1 = obstáculo')
        grid = []
        for i in range(n):
            parts = input(f'Linha {i+1}: ').split()
            if len(parts) != m:
                print(f'Erro: esperava {m} valores, recebeu {len(parts)}.')
                sys.exit(1)
            try:
                row = [int(x) for x in parts]
            except:
                print('Erro: use somente 0 ou 1.')
                sys.exit(1)
            grid.append(row)
    # coordenadas iniciais
    while True:
        try:
            x, y = map(int, input('Coordenadas iniciais (linha coluna)? ').split())
            if x < 0 or x >= n or y < 0 or y >= m:
                raise ValueError
            if grid[x][y] != 0:
                print('Célula inicial deve ser 0 (livre).')
                continue
            break
        except ValueError:
            print('Entrada inválida. Tente novamente.')
    return grid, x, y

# Flood fill BFS ortogonal
def flood_fill(grid, sx, sy, color):
    n, m = len(grid), len(grid[0])
    queue = collections.deque([(sx, sy)])
    grid[sx][sy] = color
    while queue:
        i, j = queue.popleft()
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 0:
                grid[ni][nj] = color
                queue.append((ni, nj))

# Preenche todas regiões
def fill_all_regions(grid, sx, sy):
    color = 2
    flood_fill(grid, sx, sy, color)
    n, m = len(grid), len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                color += 1
                flood_fill(grid, i, j, color)
    return color

# Cor RGB para cada valor
def get_color(val):
    if val not in PALETTE:
        PALETTE[val] = (random.randrange(50,256), random.randrange(50,256), random.randrange(50,256))
    return PALETTE[val]

# Mostra gráfico com Pygame, incluindo legenda
def display_graphical(grid):
    n, m = len(grid), len(grid[0])
    pygame.init()
    window_width  = m*(CELL_SIZE+MARGIN)+MARGIN + LEGEND_WIDTH
    window_height = n*(CELL_SIZE+MARGIN)+MARGIN
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('FloodFill - Regiões Coloridas')
    clock = pygame.time.Clock()

    pygame.font.init()
    font = pygame.font.SysFont(None, 24)

    running = True
    while running:
        clock.tick(FPS)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
        # fundo branco
        screen.fill((255,255,255))
        # desenha grid
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                color = get_color(val)
                x = j*(CELL_SIZE+MARGIN) + MARGIN
                y = i*(CELL_SIZE+MARGIN) + MARGIN
                pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))
        # desenha legenda
        legend_x = m*(CELL_SIZE+MARGIN) + 2*MARGIN
        heading = font.render('Legenda:', True, (0,0,0))
        screen.blit(heading, (legend_x, MARGIN))
        for idx, val in enumerate(sorted(PALETTE.keys())):
            y = MARGIN + 30 + idx*30
            col_rect = pygame.Rect(legend_x, y, 20, 20)
            pygame.draw.rect(screen, get_color(val), col_rect)
            label = f"{val}: obst" if val == 1 else f"{val}"
            text = font.render(label, True, (0,0,0))
            screen.blit(text, (legend_x+30, y))
        pygame.display.flip()
    pygame.quit()

# Imprime grid
def print_grid(grid):
    print('\nGrid final:')
    for row in grid:
        print(' '.join(str(x) for x in row))

# Função principal
def main():
    grid, sx, sy = read_inputs()
    # mostra grid inicial
    print_grid(grid)
    display_graphical(grid)
    # executa flood fill
    fill_all_regions(grid, sx, sy)
    # mostra resultado final
    print_grid(grid)
    display_graphical(grid)

if __name__ == '__main__':
    main()
