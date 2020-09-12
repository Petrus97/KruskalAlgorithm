import Graph
import MST_Kruskal
import UnionFind
import os
import pickle
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')


def evaluate_kruskal(probabilities, dim):
    df = pd.DataFrame(columns=['Probabilities', 'MST_time', 'Path_cost'])
    p = []
    for prob in probabilities:
        p.append(str(prob*100) + "%")
    df['Probabilities'] = p
    del p
    path_cost = []
    m_elapsed = []
    elapsed = []
    file_list = []
    file_name = 'graph_' + str(dim) + '_'
    for files in os.listdir('db'):
        if file_name in files:
            file_list.append(files)
    for files in file_list:
        for i in range(1, 11):
            logging.info("evaluating " + files + " " + str(i))
            name = 'db/' + files
            file = open(name, 'rb')
            graph = pickle.load(file)  # load file and calculate MST
            file.close()
            start = time.perf_counter()
            weight = MST_Kruskal.MST_Kruskal(graph)
            end = time.perf_counter()
            elapsed.append(end - start)
            logging.info(str(end - start) + " " + str(i))
        m_elapsed.append(sum(elapsed)/10)
        # don't calculate the average because is always the same
        path_cost.append(weight)
    df['MST_time'] = m_elapsed
    df['Path_cost'] = path_cost
    print(df)
    # plt.xlabel("Probability exists an edge between two nodes")
    # plt.ylabel("Time to find MST")
    plt.plot(df['Probabilities'], df['MST_time'], marker="o")
    plt.title("Algoritmo di Kruskal su grafo di " + str(dim) + " nodi")
    try:
        os.mkdir("figures")
    except FileExistsError:
        pass
    plt.savefig('figures/' + file_name + '.png')
    plt.clf()
    df.to_latex(buf="results/" + file_name + ".tex", index=False)

def evaluate_connected_components(dimension: int, probabilities: list):
    df = pd.DataFrame(columns=['Probabilità arco', 'Componenti connesse'])
    df['Probabilità arco'] = probabilities
    cc = []
    for prob in probabilities:
        logging.info("evaluating with %f prob of existance" % prob)
        union_find = UnionFind.UnionFind()
        graph = Graph.Graph(dimension)
        graph.random_graph(prob)
        union_find.connected_components(graph)
        # print(union_find.set)
        cc.append(union_find.get_number_of_cc())
    df['Componenti connesse'] = cc
    print(df)
    plt.plot(df['Probabilità arco'], df['Componenti connesse'], marker="o")
    plt.title("Componenti connesse su grafo di 500 nodi con probabilità d'arco crescente")
    try:
        os.mkdir("figures")
    except FileExistsError:
        pass
    plt.savefig('figures/connected_components.png')
    plt.clf()
    df.to_latex(buf="results/connected_components.tex", index=False)
    pass


# this function generate random graphs, takes in input probability and dimension
def generate_random_graph(probabilities, dimensions):
    for prob in probabilities:
        for n_nodes in dimensions:
            file_name = "db/graph_" + \
                str(n_nodes) + "_prob_" + str(prob) + ".pickle"
            if os.path.isfile(file_name):  # if exist don't create new files
                continue
            else:
                graph = Graph.Graph(n_nodes)
                graph.random_weighted_graph(prob)
                file = open(file_name, 'wb')
                pickle.dump(graph, file)
                file.close()
                del graph


def start_experiment():
    try:
        os.mkdir("db")
    except FileExistsError:
        print("Directory already exist")
        pass
    # list of probability threshold
    probabilities = [0.25, 0.5, 0.75, 0.85, 0.9]
    dimensions = [10, 50, 100, 500, 1000, 2500]
    generate_random_graph(probabilities, dimensions)
    for dim in dimensions:
        evaluate_kruskal(probabilities, dim)
    evaluate_connected_components(500, [p for p in np.arange(0.0005, 0.025, 0.0005)])
