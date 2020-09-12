import numpy as np
import random
import pickle
import itertools


class Graph(object):
    def __init__(self, n_nodes=0):
        # Adjacency matrix full of zeros
        self.graph = np.zeros((n_nodes, n_nodes))
        self.size = n_nodes
        self.edges = {}  # dictionary  "edge" : "weight"
        for e in itertools.combinations(range(n_nodes), 2): # create all edges
            self.edges[e] = 1
        self.nodes = [i for i in range(n_nodes)]

    def random_graph(self, threshold):
        for edge in list(self.edges):
            prob = np.random.uniform(0, 1)
            if prob < threshold: # if prob is less then threshold add an edge. ie: threshold = 0.25 => prob to add an edge 25%
                u, v = edge
                self.graph[u, v] = 1
                self.graph[v, u] = 1
            else:
                self.edges.pop(edge)

    def random_weighted_graph(self, threshold):
        for edge in list(self.edges):
            prob = np.random.uniform(0, 1)
            if prob < threshold: # if prob is less then threshold add an edge. ie: threshold = 0.25 => prob to add an edge 25%
                u, v = edge
                weight = int(np.random.uniform(1, 10000))
                self.graph[u, v] = weight
                self.graph[v, u] = weight
                self.edges[edge] = weight
            else:
                self.edges.pop(edge)

    def show_edges(self):
        for key in self.edges:
            print(key, self.edges[key])

    def cormen_graph(self):  # write to check if union-find works
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

    def cormen_graph_2(self): # write to check if mst works
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
        # for array in self.graph:
        #     print(array)
        print(self.graph)

    def load_graph(self, file):
        self.graph = pickle.load(file)
