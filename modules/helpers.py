import json


def export_to_output_folder(obj, export_file_name):
    with open(f"output/{export_file_name}", "w") as f:
        json.dump(obj, f, indent=2)

def choose_node(nodes):
    result = ""
    while result == "":
        print(", ".join(nodes))
        result = input("> ")
        if result not in nodes:
            print("*Invalid input*")
            result = ""
    return result
