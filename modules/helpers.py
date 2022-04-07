import json


def export_to_output_folder(obj, export_file_name):
    with open(f"output/{export_file_name}", "w") as f:
        json.dump(obj, f, indent=2)
