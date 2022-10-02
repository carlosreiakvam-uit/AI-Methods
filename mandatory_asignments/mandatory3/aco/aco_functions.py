import random

__author__ = 'Carlos Reiakvam <cre032@uit.no>'


def gen_pheromone_matrix(graph: dict) -> list:
    pheromone_matrix = []
    for i in range(len(graph)):
        edges = {}
        node: dict = graph[str(i)]
        for _ in node:
            edges[str(_)] = 0
            # edges.append(0)
        pheromone_matrix.append(edges)
    return pheromone_matrix


def get_random_edge(graph: dict, from_node):
    edges: dict = graph[str(from_node)]
    random_edge: int = int((random.choice(list(edges))))
    random_edge_n = list(edges.keys()).index(str(random_edge))
    return random_edge_n


def get_to_node(from_node: int, graph: dict) -> list:
    edges: dict = graph[str(from_node)]
    to_node_n: int = int((random.choice(list(edges))))  # number of to_node
    to_node_i = list(edges.keys()).index(str(to_node_n))  # index of to_node
    return [to_node_n, to_node_i]


def update_nodes(nd: dict, graph: dict) -> None:
    edges: dict = graph[str(nd['from_node_n'])]
    nd['to_node_n'] = int((random.choice(list(edges))))  # number of to_node
    nd['to_node_i'] = list(edges.keys()).index(str(nd['to_node_n']))  # index of to_node


def update_pheromone(nd: dict, pheromone_matrix, graph):
    # decay = 0.001
    weight = graph[str(nd['from_node_n'])][str(nd['to_node_n'])]['weight']
    # update pheremone matrix
    pheromone_matrix[int(nd['from_node_n'])][int(nd['to_node_i'])] += (0.001 * 1 / weight)


def get_weight_from_graph(from_node, to_node, graph) -> int:
    return graph[from_node][to_node]['weight']


def get_summed_weights_from_path(path, graph) -> float:
    weight_sum = 0
    for i, _ in enumerate(path):
        from_n = str(path[i])
        to_n = str(path[i + 1])
        if to_n == '29':
            break
        else:
            weight_sum += graph[from_n][to_n]['weight']
    return weight_sum


def ant_run(graph) -> list:
    ant_path: list = [0]
    nd = {'from_node_n': 0, 'to_node_n': 0, 'to_node_i': 0}
    while nd['to_node_n'] != 29:
        nd['from_node_n'] = nd['to_node_n']
        update_nodes(nd, graph)  # choose random new node
        ant_path.append(nd['to_node_n'])  # step 3: keep store of ants path
    return ant_path


def update_pheromone_matrix(current_ap, pheromone, pheromone_matrix):
    i = 0
    for i, node in enumerate(current_ap):
        if node == 29: break
        from_n = current_ap[i]
        to_n = current_ap[i+1]
        pheromone_matrix[from_n][str(to_n)] += pheromone
