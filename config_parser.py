import yaml,json
import os


def read_config_file(file):
    if file.endswith(".squareci.yaml"):
        return read_yaml(file)
    elif file.endswith(".squareci.json"):
        return read_json(file)


def read_yaml(file):
    with open(file, "r") as file:
        configs = yaml.load(file, Loader=yaml.FullLoader)
        return configs


def read_json(file):
    with open(file, "r") as file:
        configs = json.load(file, Loader=yaml.FullLoader)
        return configs


def parse_configs(config):
    before_runnables = []
    steps_runnables = []
    after_runnables = []
    for task in config["before"]:
        before_runnables.append(task["run"])
    for task in config["steps"]:
        steps_runnables.append(task["run"])
    for task in config["after"]:
        after_runnables.append(task["run"])

    return before_runnables, steps_runnables, after_runnables

# def run():
#     for runnable in before_runnables:
#         result = os.system(f"docker {runnable}")
#         if result is not 0:
#             continue
#         else:
#             return "X",
