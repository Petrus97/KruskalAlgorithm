import Graph
import MST_Kruskal
import UnionFind
import os
import pickle
import time
import pandas as pd

# TODO fare un grafico con ascisse: tempo ordinate: probabilità
def evaluate_experiment(dim):
    df = pd.DataFrame(columns= ['Probabilities', 'MST_time'])
    df['Probabilities'] = [0.5, 0.75, 0.85, 0.9]
    graph = Graph.Graph()
    file_list = []
    file_name = 'graph_' + str(dim) + '_'
    for files in os.listdir('db'):
        if file_name in files:
            file_list.append(files)
    for files, prob in zip(file_list, df['Probabilities']):
        name = 'db/' + files
        print(name)
        file = open(name, 'rb')
        graph = pickle.load(file)  # load file and calculate MST
        file.close()
        start = time.perf_counter()
        MST_Kruskal.MST_Kruskal(graph)
        end = time.perf_counter()
        df['MST_time'] = end - start
    print(df)



# this function generate random graphs, takes in input probability 
def generate_random_graph(prob):
    n_nodes = [50, 100, 500, 1000]
    for node in n_nodes:
        graph = Graph.Graph(node)
        graph.random_weighted_graph(prob)
        file_name = "db/graph_" + str(node) + "_prob_" + str(prob) + ".txt"
        file = open(file_name, 'wb')
        pickle.dump(graph, file)
        file.close()
    


def start_experiment():
    try:
        os.mkdir("db")
    except FileExistsError:
        print("Directory already exist")
        pass
    probabilities = [0.5, 0.75, 0.85, 0.9] # list of probabilities
    for prob in probabilities:
        generate_random_graph(prob)