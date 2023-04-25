from typing import Union

import numpy as np
import networkx as nx

from scipy.sparse import spmatrix, issparse


def compute_graphormer_distances(
        adj: Union[np.ndarray, spmatrix], 
        num_nodes: int,
        cache: dict
) -> np.ndarray:
    """
    Compute Graphormer distance between node pairs.

    Parameters:
        adj [num_nodes, num_nodes]: Adjacency matrix
        num_nodes [int]: Number of nodes in the graph
        cache [dict]: Dictionary of cached objects
    Returns:
        dist [num_nodes, num_nodes]: 2D array with Graphormer distances between node pairs
        base_level [str]: Indicator of the output pos_level (node, edge, [node]pair, graph) -> here pair
        cache [dict]: Updated dictionary of cached objects
    """

    base_level = 'pair'

    if 'graphormer' in cache.keys():
        dist = cache['graphormer']

    else:
        if issparse(adj):
            adj = adj.toarray()

        G = nx.from_numpy_array(adj)
        paths = nx.all_pairs_shortest_path(G)
        
        dist_dict = {i: {j: len(path)-1 for j, path in paths_from_i.items()} for i, paths_from_i in paths}
        dist = np.asarray([[dist_dict[i][j] for j in range(num_nodes)] for i in range(num_nodes)])
        cache['graphormer'] = dist

    return dist, base_level, cache