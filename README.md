# PathFinder - Resolvendo o Labirinto 2D com o Algoritmo A*

Este projeto implementa o algoritmo de busca A* para encontrar o menor caminho em um labirinto. Desenvolvido para a disciplina de Fundamentos de Projeto e Análise de Algoritmos da PUC Minas.

### Autores:

- Claudio Manoel Jansen de Oliveira
- Nathan Gonçalves de Oliveira
- Rafael Ferreira Fernandes

## Descrição do Projeto

O PathFinder é uma aplicação em Python que:

- Lê ou gera um labirinto 2D (matriz de células livres e obstáculos).

- Executa o algoritmo A* para encontrar o caminho mais curto entre S (início) e E (fim).

- Visualiza em tempo real as células visitadas, a fronteira de exploração e o caminho final.

- Permite execução manual (entrada pelo usuário) ou automática (labirinto aleatório).

## Sobre o funcionamento do Algoritmo

### Algoritmo A* 

O Algoritmo A* é um método de busca heurística que encontra o caminho mais curto em um grafo ao combinar dois componentes:

- g(n): custo exato do caminho percorrido desde o nó inicial até o nó atual n.

- h(n): heurística, estimativa admissível do custo restante de n até o nó objetivo.

A soma desses valores, f(n) = g(n) + h(n), define a prioridade de expansão dos nós. O A* se comporta como Dijkstra quando h(n)=0 e como busca gulosa quando g(n)=0.

#### Inicialização: insere o nó inicial na lista aberta (open set) com  e  calculado.

- Iteração:

    - Remove da lista aberta o nó de menor f = g + h.

    - Se for o objetivo, reconstrói o caminho e encerra.

    - Caso contrário, move-o para a lista fechada (visited set) e explora seus vizinhos livres.

- Para cada vizinho:

    - Calcula g = g(n) + 1.
    
    - Calcula h (Manhattan) e f = g + h .

Se o nó não estiver na lista aberta ou tiver um f menor, atualiza seus valores e ponteiro "came_from".

Insere ou reordena o nó na lista aberta conforme o novo f.

Reconstrução: quando o objetivo é extraído da lista aberta, percorre os ponteiros "came_from" de volta ao inicial para formar o caminho.
