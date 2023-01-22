import os
import networkit as nk
from networkit.generators import RmatGenerator
import networkx as nx
import numpy as np
from math import log2


__all__ = ['learn_and_generate', 'save_graph_edgelist']

def learn_and_generate(G):
    """
    Fits an R-MAT model to a given graph G and generates a networkx graph using that model

    args:
    G: A networkx undirected graph
    """

    nodes = sorted(list(G.nodes()))
    N = len(list(G.nodes()))
    A = nx.to_numpy_array(G, nodelist=nodes)
    edge_total = np.sum(A)

    scale = np.around(log2(N), decimals = 0)

    to_remove = 2**scale - N

    if to_remove <= 0:
        scale = scale + 1
        to_remove = 2**scale - N

    edgefactor = (edge_total / 2)  / N

    halfN = int(N/2)

    top_left = np.sum(A[:halfN, :halfN]) / edge_total
    top_right = np.sum(A[:halfN, halfN:]) / edge_total
    bottom_left = np.sum(A[halfN:, :halfN]) / edge_total
    bottom_right = np.sum(A[halfN:, halfN:]) / edge_total

    generator = nk.generators.RmatGenerator(scale,
                                            edgefactor,
                                            top_left,
                                            top_right,
                                            bottom_left,
                                            bottom_right,
                                            reduceNodes=to_remove)


    return nk.nxadapter.nk2nx(generator.generate())

def save_graph_edgelist(Glist, directory, data = False):
    for i, g in enumerate(Glist):
        path = os.path.join(directory, f"{i}.edgelist")
        nx.write_edgelist(g, path, delimiter = "\t", data = data)



