from modules import export_processed_configs, read_configs

processed_configs = read_configs("configs")

export_processed_configs(
    processed_configs=processed_configs, export_path="output/processed_configs.json"
)
