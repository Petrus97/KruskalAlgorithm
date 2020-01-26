# KruskalAlgorithm
Esercizio F: Componenti connesse e MST
Per studiare gli algoritmi per trovare le componenti connesse si scrivano i seguenti programmi:
- generazione di graﬁ casuali con un numero di nodi a scelta ed una determinata probabilità di presenza
   di archi tra vertici (es. partire da una matrice di adiacenza con tutti 0 e poi cambiare archi ad 1 con
  una certa probabilità )
- generazione di graﬁ pesati casuali 
- ricerca delle componenti connesse
- algoritmo di Kruscal
    - struttura dati UNION-FIND
-  Un programma che permetta di condurre esperimenti su graﬁ casuali con dimensione crescente e con probabilità
   di presenza di archi crescente. 
   <br>
   Scrivere inoltre una relazione che descriva quanto fatto

# Cormen Graph
Per testare se il programma funzionasse correttamente ho scritto a mano le matrici di adiacenza dei grafi presenti nel CLRS(cap 21.1 e cap. 23.2) su cui applicare l'**Union-find** e l'algoritmo di **Kruskal**<br>
Per eseguire il test e verificare con il risultato del libro:<br>
- Union find
```Python
graph = Graph.Graph(10)
graph.cormen_graph()
union_find = UnionFind.UnionFind()
union_find.connected_components(graph)
print("Union-find sets:")
union_find.print_set()
```
- Kruskal
```Python
graph = Graph.Graph(9)
graph.cormen_graph_2()
MST = list()
MST = kruskal.MST_Kruskal(graph)
print ("MST: ", MST)
```
