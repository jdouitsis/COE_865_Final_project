import json
from os import listdir
from os.path import isfile, join


def read_configs(folder_path):
    result = {}
    config_files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    for config_file in config_files:
        config_path = join(folder_path, config_file)
        config = read_config(config_path)

        result = {
            **result,
            **generate_rc_to_rc_and_host_asn_connections(config),
            **generate_host_to_rc_asn_connections(config),
        }

    return result


def generate_host_to_rc_asn_connections(config):
    result = {}
    cur_asn = f"ASN{config['self']['ASN']}"
    for host in config["all_host_asn"].keys():
        result[host] = {cur_asn: config["all_host_asn"][host]}
    return result


def generate_rc_to_rc_and_host_asn_connections(config):
    return {f"ASN{config['self']['ASN']}": config["all_adj_asn"]}


def read_config(config_path):
    result = {}
    with open(config_path) as f:

        result["self"] = process_raw_rc_info(f.readline().strip().split(" "))

        result["all_adj_rc"] = {}
        adj_rc_count = int(f.readline())
        for _ in range(adj_rc_count):
            raw_data = f.readline().strip().split(" ")
            result["all_adj_rc"][
                get_ASN_name_from_raw_rc_ASN_info(raw_data)
            ] = process_raw_rc_info(raw_data)

        result["all_adj_asn"] = {}
        adj_ASN_count = int(f.readline())
        for _ in range(adj_ASN_count):
            raw_data = f.readline().strip().split(" ")
            raw_ASN_data = process_raw_ASN_info(raw_data)
            result["all_adj_asn"][
                get_ASN_name_from_raw_ASN_info(raw_data)
            ] = raw_ASN_data

        result["all_host_asn"] = {}
        for adj_asn in result["all_adj_asn"].keys():
            if adj_asn not in result["all_adj_rc"]:
                result["all_host_asn"][adj_asn] = result["all_adj_asn"][adj_asn]

    return result


def process_raw_rc_info(raw):
    return {
        "RCID": raw[0],
        "ASN": raw[1],
        "IP": raw[2],
    }


def process_raw_ASN_info(raw):
    return {
        "Mbps": raw[1],
        "cost": raw[2],
    }


def get_ASN_name_from_raw_ASN_info(raw):
    return f"ASN{raw[0]}"


def get_ASN_name_from_raw_rc_ASN_info(raw):
    return f"ASN{raw[1]}"
