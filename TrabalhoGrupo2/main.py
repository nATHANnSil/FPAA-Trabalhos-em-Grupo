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