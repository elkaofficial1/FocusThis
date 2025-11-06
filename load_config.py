import yaml
import os

def load_config(config_path='config.yml'):
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_path, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)

    return config

def Load_patch():
    config = load_config()
    return config["patch"]["path"]

def Load_Color_Back():
    config = load_config()
    return config["application"]["HIGHLIGHT_COLOR_BACK"]

def Load_Color_Fore():
    config = load_config()
    return config["application"]["HIGHLIGHT_COLOR_FORE"]

def load_text():
    config = load_config()
    path = config["path"]["path"]
    with open(path, 'r', encoding='utf-8') as file:
                text_txt = file.read()
    return str(text_txt)
