from random import choices


class Aco:
    def __init__(self, graph):
        self.gg = {k: {e: w['weight'] for e, w in v.items()} for k, v in graph.items()}
        self.pher_g = {k: {e: 1.0 for e, w in v.items()} for k, v in self.gg.items()}

    def ant_run(self, current_node='0', goal='29'):
        path, n_set = [], set()
        while True:
            if current_node == goal:
                return path + [current_node]
            nodes, weights = zip(*[(k, v) for k, v in self.pher_g[current_node].items()])

            # current choice
            ch = choices(nodes, weights)[0]

            # avoid ant mill
            if ch not in n_set:
                path.append(current_node)
                n_set.add(current_node)
                current_node = ch
            else:
                return None

    def update_pheromone_matrix(self, n_ants):
        ant_paths = [self.ant_run() for _ in range(n_ants)]
        pher_n = 0.01

        for ap in ant_paths:
            path_cost = 0

            for i in range(len(ap) - 1):
                path_cost += self.gg[ap[i]][ap[i + 1]]

            pher_to_deposit = pher_n / path_cost

            for i in range(len(ap) - 1):
                self.pher_g[ap[i]][ap[i + 1]] += pher_to_deposit

    def ant_cost(self,best_path):
        ant_cost = 0
        for i in range(len(best_path) - 1):
            ant_cost += self.gg[best_path[i]][best_path[i + 1]]
        return ant_cost

    def get_best_path_from_ant(self):
        i, max_pher, best_path = 0, 0, []
        while i < len(self.pher_g):
            best_path.append(str(i))

            # ant wants edge with the most pheromones!
            max_pher = max(self.pher_g[str(i)], key=self.pher_g[str(i)].get)

            i = int(max_pher)  # iterates to next node
            if i == len(self.pher_g) - 1:  # if i == 29; append and break
                best_path.append(str(i))
                return best_path

    def generate_colors(self, best_path, c1='yellow', c2='lightgrey') -> list:
        colormap = []
        for i in range(len(self.gg)):
            if str(i) in best_path:
                colormap.append(c1)
            else:
                colormap.append(c2)
        return colormap
