import Graph
import MST_Kruskal
import UnionFind
import os
import pickle
import time
import pandas as pd
import matplotlib.pyplot as plt

def evaluate_experiment(probabilities, dim):
    df = pd.DataFrame(columns= ['Probabilities', 'MST_time'])
    df['Probabilities'] = probabilities
    graph = Graph.Graph()
    m_elapsed = []
    elapsed = []
    file_list = []
    file_name = 'graph_' + str(dim) + '_'
    for files in os.listdir('db'):
        if file_name in files:
            file_list.append(files)
    for files in file_list:
        for i in range(1, 11):
            name = 'db/' + files
            print(name)
            file = open(name, 'rb')
            graph = pickle.load(file)  # load file and calculate MST
            file.close()
            start = time.perf_counter()
            MST_Kruskal.MST_Kruskal(graph)
            end = time.perf_counter()
            elapsed.append(end - start)
        m_elapsed.append(sum(elapsed)/10)
    df['MST_time'] = m_elapsed
    print(df)
    plt.xlabel("Probability")
    plt.ylabel("Time to find MST")
    plt.plot(df['Probabilities'], df['MST_time'], marker="o")
    plt.title("MST benchmark on graph with " + str(dim) + " nodes")
    try:
        os.mkdir("figures")
    except FileExistsError:
        pass
    plt.savefig('figures/' + file_name + '.png')
    plt.clf()


# this function generate random graphs, takes in input probability 
def generate_random_graph(prob, dimensions):
    n_nodes = dimensions
    for node in n_nodes:
        file_name = "db/graph_" + str(node) + "_prob_" + str(prob) + ".txt"
        if os.path.isfile(file_name): # if exist don't create new files
            continue
        else:
            graph = Graph.Graph(node)
            graph.random_weighted_graph(prob)
            file = open(file_name, 'wb')
            pickle.dump(graph, file)
            file.close()
    


def start_experiment():
    try:
        os.mkdir("db")
    except FileExistsError:
        print("Directory already exist")
        pass
    probabilities = [0.25, 0.5, 0.75, 0.85, 0.9] # list of probabilities
    dimensions = [10, 50, 100, 500, 1000]
    for prob in probabilities:
        generate_random_graph(prob, dimensions)
    for dim in dimensions:
        evaluate_experiment(probabilities, dim)
    