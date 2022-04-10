
from time import sleep


class Dijkstra:
    processed = []

    @staticmethod
    def print_route(route):
        route_string = ' => '.join([node for node, cost in route])
        route_cost = route[-1][1]
        print(f"The route cost was {route_cost} and the route taken was: {route_string}")


    def animate_route(self, route):
        prev = None
        for node, _ in route:
            if prev == None:
                print(node)
                prev = node
                continue
            
            for _ in range(int(self.nodes[prev][node]['cost'])):
                sleep(.2)
                print(".")
            print(node)    
            prev = node


    def __init__(self, source, nodes):
        self.source = source
        self.nodes = nodes

        self.setup_default_tree()
        
        node_to_process = self.source

        while node_to_process:
            self._process_node(node_to_process)
            self.processed.append(node_to_process)
            node_to_process = self._choose_next_node()

    def setup_default_tree(self):
        self.tree = {}
        for node in self.nodes:
            val = {"cost": None, 'prev': None, "route_cost": None}
            if node == self.source:
                val['cost'] = 0
                val['route_cost'] = 0
            self.tree[node] = val


    def _process_node(self, node):
        base_cost = self.tree[node]['cost']
        base_route_cost = self.tree[node]['route_cost']
        adj_nodes_info = self.nodes[node]

        for adj_node, adj_node_info in adj_nodes_info.items():
            adj_node_cost = self.tree[adj_node]['cost']
            adj_node_route_cost = self.tree[adj_node]['route_cost']

            potential_new_route_cost = base_route_cost + float(int(adj_node_info['cost']) / int(adj_node_info['Mbps']),)

            if adj_node in self.processed:
                continue

            if adj_node_cost == None or adj_node_route_cost > potential_new_route_cost:
                self.tree[adj_node] = {
                    'cost': base_cost + int(adj_node_info['cost']),
                    'route_cost': potential_new_route_cost,
                    'prev': node
                }

    def _choose_next_node(self):
        next_node = None
        next_node_cost = None

        for node, value in self.tree.items():
            if node in self.processed or value['route_cost'] == None:
                continue
            if next_node_cost is None or value['route_cost'] < next_node_cost:
                next_node = node
                next_node_cost = value['route_cost']

        return next_node

    def find_path_to_node(self, node):
        path = []
        cost = 0

        prev = node

        while prev != self.source:
            path.append((prev, self.tree[prev]['cost']))
            cost += self.tree[prev]['cost']
            prev = self.tree[prev]['prev']
    
        path.append((self.source, 0))
        path.reverse()

        return path
