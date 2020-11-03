from collections import defaultdict


class Graph():
    """
    Grafo
    """

    def __init__(self):
        self.graph = defaultdict(list)

    def adicionaAresta(self, origem, destino):
        self.graph[origem].append(destino)

    def __str__(self):
        return_str = ''
        for node in self.graph:
            return_str += f"{node} -> {self.graph[node]}\n"
        return return_str

    def __getitem__(self, key):
        return self.graph[key]


if __name__ == "__main__":
    g = Graph()

    g.adicionaAresta(1, 5)
    g.adicionaAresta(5, 1)
    g.adicionaAresta(1, 4)
    g.adicionaAresta(4, 1)
    g.adicionaAresta(1, 2)
    g.adicionaAresta(2, 1)
    g.adicionaAresta(2, 7)
    g.adicionaAresta(7, 2)
    g.adicionaAresta(2, 6)
    g.adicionaAresta(6, 2)
    g.adicionaAresta(2, 3)
    g.adicionaAresta(3, 2)

    print(g)

    print(g[1])
