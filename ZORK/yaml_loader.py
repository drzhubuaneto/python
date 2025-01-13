# yaml_loader.py

import yaml


def load_game_data(filename):
    with open(filename, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data
