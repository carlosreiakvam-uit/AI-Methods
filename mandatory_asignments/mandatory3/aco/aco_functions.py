import random


# Author: Carlos Reiakvem, october 2022

def gen_pheromone_matrix(graph: dict) -> list:
    pheromone_matrix = []
    for i in range(len(graph)):
        edges = []
        node: dict = graph[str(i)]
        for _ in node:
            edges.append(0)
        pheromone_matrix.append(edges)
    return pheromone_matrix


def get_random_edge(graph: dict, from_node):
    edges: dict = graph[str(from_node)]
    random_edge: int = int((random.choice(list(edges))))
    random_edge_n = list(edges.keys()).index(str(random_edge))

    return random_edge_n


def get_to_node(from_node: int, graph: dict):
    edges: dict = graph[str(from_node)]
    to_node: int = int((random.choice(list(edges))))
    to_node_n = list(edges.keys()).index(str(to_node))
    return int(to_node_n)


def update_pheromone(from_node, to_node, pheromone_matrix, graph):
    to_node = str(to_node)
    weight = graph[str(from_node)][to_node]['weight']
    # update pheremone matrix
    pheromone_matrix[from_node][to_node] += 0.001 * 1 / weight
