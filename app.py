from modules import dijkstra, export_processed_configs, read_configs

processed_configs = read_configs("configs")

export_processed_configs(
    processed_configs=processed_configs, export_path="output/processed_configs.json"
)

nodes = processed_configs.keys()


def choose_node(nodes):
    result = ""
    while result == "":
        print(", ".join(nodes))
        result = input("> ")
        if result not in nodes:
            print("*Invalid input*")
            result = ""
    return result


# print("Choose a source from the list below:")
# source = choose_node(nodes)

# print("Choose a receiver from the list below:")
# receiver = choose_node([node for node in nodes if node != source])

dijkstra("ASN1", processed_configs)
