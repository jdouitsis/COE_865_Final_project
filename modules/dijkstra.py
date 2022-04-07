
class dijkstra:
    processed = []
    def __init__(self, source, nodes):
        self.source = source
        self.nodes = nodes


        self.result = {}
        for node in nodes:
            val = {"cost": None, 'prev': None}
            if node == source:
                val['cost'] = 0
            self.result[node] = val

        node_to_process = self.source
        while node_to_process:
            self.__process_node(node_to_process)

            self.processed.append(node_to_process)

            node_to_process = self.__choose_next_node()
            print('next to process: ', node_to_process)
            print()

        print(self.result)


    def __process_node(self, node):
        base_cost = self.result[node]['cost']
        adj_nodes_info = self.nodes[node]

        for adj_node, adj_node_info in adj_nodes_info.items():
            adj_node_cost = self.result[adj_node]['cost']
            potential_new_cost = base_cost + int(adj_node_info['cost'])

            if adj_node in self.processed:
                print("Processed already!")
                continue

            if adj_node_cost == None or adj_node_cost < potential_new_cost:
                self.result[adj_node] = {
                    'cost': base_cost + int(adj_node_info['cost']),
                    'prev': node
                }

    def __choose_next_node(self):
        next_node = None
        next_node_cost = None

        for node, value in self.result.items():
            if node in self.processed or value['cost'] == None:
                continue
            if next_node_cost is None or value['cost'] > next_node_cost:
                next_node = node
                next_node_cost = value['cost']

        return next_node


# def dijkstra(source, nodes):

#     print(nodes)


# def process_node(node)
