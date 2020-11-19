from collections import defaultdict


class Graph():
    """
    Grafo
    """

    def __init__(self):
        self.graph = defaultdict(list)
        self.nodes = set()

    def adicionaArco(self, origem, destino):
        self.graph[origem].append(destino)
        self.nodes.add(origem)
        self.nodes.add(destino)

    def adicionaAresta(self, origem, destino):
        self.graph[origem].append(destino)
        self.graph[destino].append(origem)
        self.nodes.add(origem)
        self.nodes.add(destino)

    def __str__(self):
        return_str = ''
        for node in self.graph:
            return_str += f"{node} -> {self.graph[node]}\n"
        return return_str

    def __getitem__(self, key):
        return self.graph[key]


if __name__ == "__main__":
    g = Graph()

    g.adicionaArco(1, 5)
    g.adicionaArco(5, 1)
    g.adicionaArco(1, 4)
    g.adicionaArco(4, 1)
    g.adicionaArco(1, 2)
    g.adicionaArco(2, 1)
    g.adicionaArco(2, 7)
    g.adicionaArco(7, 2)
    g.adicionaArco(2, 6)
    g.adicionaArco(6, 2)
    g.adicionaArco(2, 3)
    g.adicionaArco(3, 2)

    print(g)

    print(g[1])
