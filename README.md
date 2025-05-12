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

### Heurística de Manhattan

Em labirintos 2D com movimentos permitidos apenas em direções ortogonais (cima, baixo, esquerda, direita), usa-se a Distância de Manhattan como heurística. Para duas células (x1,y1) e (x2, y2):

                                      h = | (x1 - x2) + |y1 - y2| 

Onde (x1,y1) é a posição do nó atual e (y1, y2) é a posição do objetivo. Essa heurística é admissível (nunca superestima o custo real) e consistente, garantindo que o A* encontre sempre o caminho ótimo.



- Inicialização: insere o nó inicial na lista aberta (open set) com g=0 e h calculado.

- Iteração:

    - Remove da lista aberta o nó de menor f = g + h.

    - Se for o objetivo, reconstrói o caminho e encerra.

    - Caso contrário, adiciona aos nós visitados e explora seus vizinhos livres.

    - Para cada vizinho, calcula  (custo atual + 1) e  (Manhattan), atualiza ou insere na lista aberta.

    - Reconstrução: usa ponteiros de "came_from" para traçar o caminho do objetivo até a origem.

    - Heurística de Manhattan: para duas células (x1,y1) e (x2, y2),


## Estrutura do Código

- Da linha 1 a linha 3: import das bibliotecas heapq, tkinter e random.
- Da linha 5 a linha 34: definição da função read_maze, responsável por ler e validar o labirinto, exibir exemplo dinâmico e capturar entrada do usuário.
- Da linha 36 a linha 43: funções heuristic e get_neighbors para cálculo da heurística de Manhattan e obtenção de vizinhos.
- Da linha 45 a linha 71: astar_generator, que implementa o algoritmo A* em forma de gerador, sinalizando visitas, fronteira e caminho.
- Da linha 73 a linha 122: função visualize, que cria a interface Tkinter, desenha o labirinto, legenda e animação passo a passo.
- Da linha 124 a linha 139: função main, contendo o prompt de escolha de modo (Manual ou Automático) e fluxo de execução.
- Linha 141: chamada do ponto de entrada 


## Como Executar o Projeto

### Pré-requisitos
- Python 3.6 ou superior
- Bibliotecas: tkinter (instalada por padrão em muitas distribuições)

### Instalação das Dependências

bash
pip install tkinterb


1. Clone o repositório:
   bash
   git clone https://github.com/nATHANnSil/FPAA-Trabalhos-em-Grupo/tree/main

   cd FPAA-Trabalhos-em-Grupo/TrabalhoGrupo1
   

2. Execute o código: 
    
    python main.py
    

3. Siga as instruções do terminal:

- Escolha se o labirinto será manual (M) ou automático (A);

### Para manual:

- Informe o número de linhas e colunas;

-  De acordo com o número de linhas e colunas inserido, um exemplo de matriz aparecerá;

- Digite cada linha no seguinte formato:
    
    S 0 1 0 0   # S = início, E = fim
    

### Para automático:

- Informe número de linhas e colunas;

- Defina a densidade de obstáculos (valor entre 0.0 e 1.0);

- O algoritmo posicionará S em (0,0), E em (n-1,m-1) e gerará obstáculos aleatoriamente.


## Exemplo de Entrada e Saída:

### Modo Manual

Entrada: 


Modo: M
Linhas: 3
Colunas: 4
S 0 1 0
0 0 1 E
0 0 0 0

Saída (no terminal):


Menor caminho: ['S(0,0)', '(1,0)', '(2,0)', '(2,1)', '(2,2)', '(2,3)', 'E(1,3)']
Labirinto com caminho marcado:
S * 1 0
* * 1 E
* * * *

Além disso, a janela gráfica mostra a sequência de cores conforme a legenda.


aqui vai um exemplo de labirinto manual

### Modo automático

Entrada: 


Modo: A
Linhas: 5
Colunas: 5
Densidade: 0.3


Saída: 

    No modo automático, apenas a janela gráfica é mostrada, com a sequência de cores conforme a legenda.

aqui vai um exemplo de labirinto automatico

### Legenda de cores da interface gráfica: 

- Branco: células livres

- Preto: obstáculos

- Verde: início (S)

- Vermelho: fim (E)

- Azul: célula visitada

- Ciano: fronteira

- Amarelo: caminho final

## Licença

Este projeto está licenciado sob a Licença MIT.