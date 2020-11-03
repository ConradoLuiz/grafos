from graph import *

visitado = []


def dfsRecursivo(g, node):
    if node in visitado:
        return
    print(node)
    visitado.append(node)
    for adjacente in g[node]:
        if adjacente in visitado:
            continue
        dfsRecursivo(g, adjacente)


def dfs(g, node):
    visitados = []
    pilha = []
    pilha.append(node)
    while len(pilha) > 0:
        n = pilha[-1]
        pilha.pop(-1)
        if n not in visitados:
            print(n)
            visitados.append(n)
            for adjacente in sorted(g[n], reverse=True):
                if adjacente not in visitados:
                    pilha.append(adjacente)


if __name__ == "__main__":
    g1 = Graph()

    g1.adicionaAresta(0, 1)
    g1.adicionaAresta(0, 2)
    g1.adicionaAresta(1, 2)
    g1.adicionaAresta(2, 0)
    g1.adicionaAresta(2, 3)
    g1.adicionaAresta(3, 3)

    print(g1)
    print('DFS Recursivo:')
    dfsRecursivo(g1, 1)
    print('DFS Iterativo:')
    dfs(g1, 1)
    visitado = []
    print('--------------')

    g2 = Graph()
    g2.adicionaAresta(2, 0)
    g2.adicionaAresta(0, 2)
    g2.adicionaAresta(1, 2)
    g2.adicionaAresta(0, 1)
    g2.adicionaAresta(3, 3)
    g2.adicionaAresta(1, 3)

    print(g2)
    print('DFS Recursivo:')
    dfsRecursivo(g2, 2)
    print('DFS Iterativo:')
    dfs(g2, 2)
