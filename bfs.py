from graph import *


def bfs(g, node):
    visitados = []
    fila = []
    fila.append(node)
    visitados.append(node)
    while len(fila) > 0:
        n = fila[0]
        fila.pop(0)
        print(n, end=' ')
        for adjacente in sorted(g[n], reverse=False):
            if adjacente not in visitados:
                visitados.append(n)
                if adjacente not in fila:
                    fila.append(adjacente)


if __name__ == "__main__":
    g1 = Graph()

    g1.adicionaAresta(1, 2)
    g1.adicionaAresta(1, 3)
    g1.adicionaAresta(1, 4)
    g1.adicionaAresta(2, 5)
    g1.adicionaAresta(2, 6)
    g1.adicionaAresta(4, 7)
    g1.adicionaAresta(4, 8)
    g1.adicionaAresta(5, 9)
    g1.adicionaAresta(5, 10)
    g1.adicionaAresta(7, 11)
    g1.adicionaAresta(7, 12)

    print(g1)
    print('BFS Iterativo:')
    bfs(g1, 1)
    print('\n--------------')

    g2 = Graph()
    g2.adicionaAresta(1, 2)
    g2.adicionaAresta(1, 3)
    g2.adicionaAresta(2, 4)
    g2.adicionaAresta(2, 5)
    g2.adicionaAresta(3, 5)
    g2.adicionaAresta(4, 5)
    g2.adicionaAresta(4, 6)
    g2.adicionaAresta(5, 6)

    print(g2)
    print('Bfs Iterativo:')
    bfs(g2, 1)
