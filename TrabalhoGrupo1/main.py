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

def get_neighbors(pos, maze):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []
    rows, cols = len(maze), len(maze[0])
    for dr, dc in directions:
        nr, nc = pos[0] + dr, pos[1] + dc
        if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '1':
            neighbors.append((nr, nc))
    return neighbors


def astar_generator(maze, start, end):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}
    while open_set:
        current = heapq.heappop(open_set)[1]
        yield ('visit', current)
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path = list(reversed(path))
            yield ('path', path)
            return
        for neighbor in get_neighbors(current, maze):
            tentative_g = g_score[current] + 1
            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, end)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
                yield ('open', neighbor)
    yield ('no_path', None)


def visualize(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    cell_size = min(600 // cols, 600 // rows)
    width, height = cols * cell_size, rows * cell_size

    # Definição da legenda
    legend_items = [
        ('Livre', 'white'),
        ('Obstáculo', 'black'),
        ('Início (S)', 'green'),
        ('Fim (E)', 'red'),
        ('Visitado', 'blue'),
        ('Fronteira', 'cyan'),
        ('Caminho', 'yellow'),
    ]
    legend_height = len(legend_items) * (cell_size // 2 + 5) + 10
    total_height = height + legend_height

    root = tk.Tk()
    root.title("Visualização A* em Tempo Real")
    canvas = tk.Canvas(root, width=width, height=total_height)
    canvas.pack()

    # Desenha o labirinto
    rects = {}
    for i in range(rows):
        for j in range(cols):
            x0, y0 = j * cell_size, i * cell_size
            x1, y1 = x0 + cell_size, y0 + cell_size
            color = 'white' if maze[i][j] != '1' else 'black'
            rects[(i, j)] = canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline='gray')

    # Destaca início e fim
    canvas.itemconfig(rects[start], fill='green')
    canvas.itemconfig(rects[end], fill='red')

   # Desenha legenda abaixo do labirinto
    y_text = height + 10
    box_size = cell_size // 2
    for label, color in legend_items:
        canvas.create_rectangle(10, y_text, 10 + box_size, y_text + box_size, fill=color, outline='gray')
        canvas.create_text(20 + box_size, y_text + box_size // 2, anchor='w', text=label)
        y_text += box_size + 5

    gen = astar_generator(maze, start, end)

    def step():
        try:
            action, pos = next(gen)
            if action == 'visit' and pos not in (start, end):
                canvas.itemconfig(rects[pos], fill='blue')
            elif action == 'open' and pos not in (start, end):
                canvas.itemconfig(rects[pos], fill='cyan')
            elif action == 'path':
                for p in pos:
                    if p not in (start, end):
                        canvas.itemconfig(rects[p], fill='yellow')
            root.after(50, step)
        except StopIteration:
            return

    root.after(500, step)
    root.mainloop()


def main():
    mode = input("\nModo de execução: Manual (digitar labirinto) [M] ou Automático (gerar labirinto) [A]? ").strip().upper()
    if mode == 'A':
        rows = int(input("Número de linhas do labirinto: "))
        cols = int(input("Número de colunas do labirinto: "))
        density = float(input("Densidade de obstáculos (0.0 a 1.0): "))
        maze = []
        for i in range(rows):
            row = []
            for j in range(cols):
                if (i, j) == (0, 0):
                    row.append('S')
                elif (i, j) == (rows - 1, cols - 1):
                    row.append('E')
                else:
                    row.append('1' if random.random() < density else '0')
            maze.append(row)
        start, end = (0, 0), (rows - 1, cols - 1)
        visualize(maze, start, end)
    else:
        maze, start, end = read_maze()
        visualize(maze, start, end)

if _name_ == '_main_':
    main()
