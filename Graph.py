import numpy as np
import random
import pickle


class Graph(object):
    def __init__(self, n_nodes=0):
        # Adjacency matrix full of zeros
        self.graph = np.zeros((n_nodes, n_nodes))
        self.size = n_nodes
        self.edges = {}  # dictionary  "edge" : "weight"
        self.nodes = []
        for i in range(n_nodes):
            self.nodes.append(i)

    def random_graph(self):  
        for u in range(self.size):
            for v in range(self.size):
                if u != v:
                    edge = random.uniform(0, 1)
                    if edge > 0.85:
                        self.graph[u, v] = 1
                        self.graph[v, u] = 1
                        if ((u, v) not in self.edges or (v, u) not in self.edges):
                            self.edges.update({(u, v): self.graph[u, v]})

    def random_weighted_graph(self, threshold):
        for u in range(self.size):
            for v in range(self.size):
                if u != v:
                    prob = np.random.uniform(0, 1)
                    if prob > threshold:    # if prob is more that threshold add an edge. ie: threshold = 0.25 => prob to add an edge 75%
                        self.graph[u, v] = int(np.random.uniform(1, 100))
                        if ((u, v) not in self.edges or (v, u) not in self.edges):
                            self.edges.update({(u, v): self.graph[u, v]})

    def show_edges(self):
        for key in self.edges:
            print(key, self.edges[key])

    def cormen_graph(self):  # write to check if works
        self.graph = [
            [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        for u in range(len(self.graph)):
            for v in range(len(self.graph)):
                # print(self.graph[u][v])
                if self.graph[u][v] == 1:
                    if ((u, v) not in self.edges or (v, u) not in self.edges):
                        self.edges.update({(u, v): 1})

    def cormen_graph_2(self):
        self.graph = [
            [0, 4, 0, 0, 0, 0, 0, 8, 0],
            [4, 0, 8, 0, 0, 0, 0, 11, 0],
            [0, 8, 0, 7, 0, 4, 0, 0, 2],
            [0, 0, 7, 0, 9, 14, 0, 0, 0],
            [0, 0, 0, 9, 0, 10, 0, 0, 0],
            [0, 0, 4, 0, 10, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2,  0, 1, 6],
            [8, 11, 0, 0, 0, 0, 1, 0, 7],
            [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]
        for u in range(len(self.graph)):
            for v in range(len(self.graph)):
                # print(self.graph[u][v])
                if self.graph[u][v] >= 1:
                    if ((u, v) not in self.edges or (v, u) not in self.edges):
                        self.edges.update({(u, v): self.graph[u][v]})

    def print_graph(self):
        for array in self.graph:
            print(array)
        print(self.graph)

    def sort_by_weight(self):
        self.edges = sorted(self.edges.values())

    def load_graph(self, file):
        self.graph = pickle.load(file)
