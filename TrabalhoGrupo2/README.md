# FloodFill - Colorindo regiões de um terreno com obstáculos

Este projeto implementa de forma interativa o algoritmo Flood Fill (varredura em largura) para colorir regiões conectadas de um grid 2D, evitando obstáculos.

### Autores:

- Claudio Manoel Jansen de Oliveira
- Nathan Gonçalves de Oliveira
- Rafael Ferreira Fernandes

## Funcionalidades:

O FloodFill é uma aplicação em Python que:

- Entrada flexível: escolha entre geração automática de grid aleatório ou inserção manual linha a linha.

- Preenchimento de regiões: inicia em uma célula livre (0) e colore todas as células adjacentes ortogonalmente.

- Cores dinâmicas: cada região recebe uma cor única, exibida com legenda.

- Visualização em tempo real: mostra o grid antes e depois do preenchimento em janelas Pygame.

- Relatório no terminal: exibe o grid inicial e final em texto.

## Sobre o funcionamento do Algoritmo

O Flood Fill é uma técnica de varredura em largura (BFS) que colore regiões conectadas de um grid:

- Início: recebe coordenadas iniciais (sx, sy) em uma célula livre.

- Fila (queue): usa collections.deque para gerenciar células a processar.

- Processo:

    - Marca a célula inicial com a cor atual (inteiro ≥2).

    - Remove da fila a próxima célula (i, j).

    - Para cada vizinho ortogonal (acima, abaixo, esquerda, direita) com valor 0:

        - Define seu valor igual à cor atual.

        - Adiciona à fila para processamento posterior.

- Repetição até a fila esvaziar, garantindo que toda região conectada seja preenchida.

- Múltiplas regiões: após preencher a região inicial, varre o grid para cada célula ainda 0, incrementa a cor e repete o flood fill, garantindo cobertura completa.

- Esse método é garantido para colorir todas as células livres conectadas ortogonalmente e identificar regiões separadas.
