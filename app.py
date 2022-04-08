from modules import (Dijkstra, choose_node, export_to_output_folder,
                     read_configs)

processed_configs = read_configs("configs")
export_to_output_folder(
    processed_configs,"processed_configs.json"
)

nodes = processed_configs.keys()

print("Choose a source from the list below:")
source = choose_node(nodes)

print("Choose a receiver from the list below:")
receiver = choose_node([node for node in nodes if node != source])

dijkstra = Dijkstra(source, processed_configs)
export_to_output_folder(dijkstra.tree, 'tree.json')

route = dijkstra.find_path_to_node(receiver)
export_to_output_folder(
    route,"route_path.json"
)

dijkstra.animate_route(route)

Dijkstra.print_route(route)

