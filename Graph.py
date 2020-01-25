import numpy as np
import random

class Graph(object):
	"""description of class"""
	def __init__(self, n_nodes):
		self.graph = np.zeros((n_nodes, n_nodes)) #Adjacency matrix full of zeros
		self.size = n_nodes
		self.edges = {} #dictionary  "edge" : "weight"
		self.nodes = []
		for i in range(n_nodes):
			self.nodes.append(i)

	def random_graph(self): #now should work...
		for u in range(self.size):
			for v in range(self.size):
				if u!=v :
					edge = random.uniform(0, 1)
					if edge > 0.85 :
						self.graph[u, v] = 1
						self.graph[v, u] = 1
						if ((u,v) not in self.edges or (v,u) not in self.edges): 
							self.edges.update({(u,v) : self.graph[u, v]})

	def random_weighted_graph(self):
		for u in range(self.size):
			for v in range(self.size):
				if u!= v:
					prob = np.random.uniform(0, 1)
					if prob > 0.85 :
						self.graph[u, v] = int(np.random.uniform(1, 20))
						if ((u,v) not in self.edges or (v,u) not in self.edges):
							self.edges.update({(u,v) : self.graph[u, v]})

	def show_edges(self):
		for key in self.edges:
			print(key, self.edges[key])

	def cormen_graph(self): #write to check if works
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
				print(self.graph[u][v])
				if self.graph[u][v] == 1:
					if ((u,v) not in self.edges or (v,u) not in self.edges): 
						self.edges.update({(u,v) : 1})


	def print_graph(self):
		print(self.graph)

	def sort_by_weight(self):
		self.edges = sorted(self.edges.values())

