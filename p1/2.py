from graph import *
from bfs import *
from dfs import *


def colorir(g, node):
    node_color = [-1 for _ in g.nodes]

    node_color[node] = 0

    disponivel = [False for _ in g.nodes]

    for n in list(g.nodes)[1:]:

        for n1 in g[n]:
            if node_color[n1] != -1:
                disponivel[node_color[n1]] = True

        cor = 0
        for n1 in g.nodes:
            if disponivel[n1] == False:
                cor = n1
                break

        node_color[n] = cor

        disponivel = [False for _ in g.nodes]

    return node_color


if __name__ == "__main__":
    g = Graph()
    g.adicionaAresta(0, 3)
    g.adicionaAresta(1, 2)
    g.adicionaAresta(1, 6)
    g.adicionaAresta(1, 5)
    g.adicionaAresta(1, 4)
    g.adicionaAresta(3, 6)
    g.adicionaAresta(3, 4)
    g.adicionaAresta(4, 6)
    g.adicionaAresta(4, 5)

    print(g.nodes)
    cores = colorir(g, 0)
    for node in g.nodes:
        print(f"Node {node} tem cor {cores[node]}")
