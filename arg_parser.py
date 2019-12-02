import argparse
import os

supported_extensions = [".squareci.yaml", ".squareci.json"]


def check_extension(path):
    for supported_extension in supported_extensions:
        if path.endswith(supported_extension):
            return True
    return False


def file_checker(file, path):
    if file is not None:
        new_path = os.path.join(path, file)
        if os.path.isfile(new_path):
            if check_extension(new_path):
                return new_path
            else:
                raise argparse.ArgumentTypeError(f"Given file: {file} is not supported config file. Supported config "
                                                 f"files are {supported_extensions}")
        else:
            raise argparse.ArgumentTypeError(f"Given file: {file} is not found in path {path}")
    else:
        for file in os.listdir(path):
            new_path = os.path.join(path, file)
            if check_extension(new_path):
                return new_path
        raise argparse.ArgumentTypeError(f"Config file not found in path {path}")


def path_validation(path):
    if os.path.exists(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"Given path: {path} is not a valid path.")


def get_config_file():
    parser = argparse.ArgumentParser(prog="squareci", description="Square CI")
    parser.add_argument("--config", "-c", metavar="", default=None, required=False, help="Config file to read. It can "
                                                                                         "be a valid yml or json "
                                                                                         "file. It it is not provided "
                                                                                         "command tries to read "
                                                                                         ".squareci.yml file or "
                                                                                         ".squareci.json file in "
                                                                                         "current working directory. "
                                                                                         "If none of them have been "
                                                                                         "provided then it raises an "
                                                                                         "error.")
    parser.add_argument("--path", "-p", metavar="", default=os.getcwd(), type=path_validation, required=False,
                        help="Current working dir. The folder that mounted to the docker container. If it is not "
                             "provided then cwd is used.")

    args = vars(parser.parse_args())
    return file_checker(args["config"], args["path"]), args["path"]

