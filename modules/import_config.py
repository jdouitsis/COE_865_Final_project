from os import listdir
from os.path import isfile, join


def read_configs(folder_path):
    result = {}
    config_files = [
        f for f in listdir(folder_path) 
        if isfile(join(folder_path, f))
    ]
    for config_file in config_files:
        config_name = config_file.split('.')[0]
        config_path = join(folder_path, config_file)
        result[config_name] = read_config(config_path)

    return result


def read_config(config_path):
    result = {}
    with open(config_path) as f:

        result["local_rc"] = process_raw_rc_info(
            f.readline().split(' ')
        )

        result["connected_rcs"] = []
        adj_rc_count = int(f.readline())
        for _ in range(adj_rc_count):
            result["connected_rcs"].append(
                process_raw_rc_info(f.readline().split(" "))
            )

        result["connected_ans"] = []
        adj_ans_count = int(f.readline())
        for _ in range(adj_ans_count):
            result["connected_ans"].append(
                process_raw_ans_info(f.readline().strip().split(" "))
            )

    print(result)
        
def process_raw_rc_info(raw):
    return {
        'RCID': raw[0],
        'ASN': raw[1],
        'IP': raw[2],
    }

def process_raw_ans_info(raw):
    return {
        'ANS': raw[0],
        'Mbps': raw[1],
        'cost': raw[2],
    }

    