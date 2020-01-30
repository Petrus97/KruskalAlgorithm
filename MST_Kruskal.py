import UnionFind
import operator
import time

def MST_Kruskal(graph):
	A = list()
	path_cost = 0
	path_step = 0
	union_find = UnionFind.UnionFind()
	for node in graph.nodes:
		union_find.make_set(node)
	for edge in sorted(graph.edges.items(), key=operator.itemgetter(1)):	# tips from stackoverflow, sort edge by weight 
		if (union_find.find_set(edge[0][0]) != union_find.find_set(edge[0][1])):
			A.append(edge)
			path_cost += edge[1]
			path_step += 1
			union_find.union(edge[0][0], edge[0][1])
	# print("MST found in ", path_step, "step. Total weight: ", path_cost)
	# return A
