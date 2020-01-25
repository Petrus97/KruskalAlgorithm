'''
Esercizio F: Componenti connesse e MST
Per studiare gli algoritmi per trovare le componenti connesse si scrivano i seguenti programmi:
-> generazione di graﬁ casuali con un numero di nodi a scelta ed una determinata probabilità di presenza
   di archi tra vertici (es. partire da una matrice di adiacenza con tutti 0 e poi cambiare archi ad 1 con
  una certa probabilità )
-> generazione di graﬁ pesati casuali 
-> ricerca delle componenti connesse
-> algoritmo di Kruscal
	└-> struttura dati UNION-FIND
-> Un programma che permetta di condurre esperimenti su graﬁ casuali con dimensione crescente e con probabilità
   di presenza di archi crescente. Scrivere inoltre una relazione che descriva quanto fatto
'''
import Graph
import UnionFind
import numpy
import time
import MST_Kruskal as kruskal

def main():
	graph = Graph.Graph(200)
	graph.random_weighted_graph()
	#graph.cormen_graph()
	print("Graph:")
	graph.print_graph()
	#graph.show_edges()
	#union_find = UnionFind.UnionFind()
	#union_find.connected_components(graph)
	#print("Union-find sets:")
	#union_find.print_set()
	#print("Representative of sets:")
	#union_find.print_representative()
	MST = list()
	MST = kruskal.MST_Kruskal(graph);
	print ("MST: ", MST)


	


main()