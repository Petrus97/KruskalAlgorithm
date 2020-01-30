import Graph
import UnionFind
import numpy
import time
import MST_Kruskal as kruskal
import experiment
import pickle
import os


def main():
	experiment.start_experiment()
	# experiment.evaluate_experiment(1000)
	# graph = Graph.Graph(1000)
	# graph.random_weighted_graph(0.9)
	# start = time.perf_counter()
	# kruskal.MST_Kruskal(graph)
	# end = time.perf_counter()
	# print(end - start)
	# file = open('db/graph_50_prob_0.5.txt', 'rb')
	# graph = pickle.load(file)
	# print(graph)
	# graph.load_graph(file)
	# file.close()
	# graph.print_graph()
	# graph = Graph.Graph(9)
	# graph.cormen_graph_2()
	# print("Graph:")
	# graph.print_graph()
	# graph.show_edges()
	# # union_find = UnionFind.UnionFind()
	# # union_find.connected_components(graph)
	# # print("Union-find sets:")
	# # union_find.print_set()
	# #print("Representative of sets:")
	# #union_find.print_representative()
	# MST = list()
	# MST = kruskal.MST_Kruskal(graph)
	# print ("MST: ", MST)
	# experiment.start_experiment()



main()
