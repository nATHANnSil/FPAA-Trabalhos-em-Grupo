import heapq
import tkinter as tk
import random

def read_maze():
    """
    Lê o labirinto do usuário via stdin.
    Retorna:
      maze: lista de listas de strings ('0','1','S','E')
      start: tupla (linha, coluna) do ponto inicial
      end: tupla (linha, coluna) do ponto final

    Exemplo dinâmico conforme tamanho:
      Para um labirinto 5x5:
        S 0 0 0 0
        0 1 1 1 0
        0 1 0 1 0
        0 1 0 1 0
        0 0 0 0 E
    """
    rows = int(input("Número de linhas do labirinto: "))
    cols = int(input("Número de colunas do labirinto: "))

    print(f"\nExemplo para uma matriz {rows}x{cols}:")
    example = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if i == 0 and j == 0:
                row.append('S')
            elif i == rows - 1 and j == cols - 1:
                row.append('E')
            else:
                row.append('0')
        example.append(' '.join(row))
    for line in example:
        print('  ' + line)
    print()

    maze = []
    start = None
    end = None
    print("Insira cada linha usando S, E, 0 e 1 separados por espaço:")
    for i in range(rows):
        line = input(f"Linha {i+1}/{rows}: ").split()
        if len(line) != cols:
            raise ValueError(f"Linha {i+1} deve ter {cols} elementos, mas recebeu {len(line)}.")
        maze.append(line)
        for j, val in enumerate(line):
            if val == 'S':
                start = (i, j)
            elif val == 'E':
                end = (i, j)
    if start is None or end is None:
        raise ValueError("O labirinto deve conter exatamente um 'S' e um 'E'.")
    return maze, start, end


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])