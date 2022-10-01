import random

__author__ = 'Carlos Reiakvam <cre032@uit.no>'


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


def get_to_node(from_node : int, graph: dict) -> list:
    edges: dict = graph[str(from_node)]
    to_node_n: int = int((random.choice(list(edges))))  # number of to_node
    to_node_i = list(edges.keys()).index(str(to_node_n))  # index of to_node
    return [to_node_n, to_node_i]


def update_pheromone(from_node, to_node, pheromone_matrix, graph):
    weight = graph[str(from_node)][str(to_node)]['weight']

    # update pheremone matrix
    pheromone_matrix[int(from_node)][int(to_node)] += 0.001 * 1 / weight
