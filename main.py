import os

from arg_parser import get_config_file
from config_parser import read_config_file, parse_configs

file, path = get_config_file()
config = read_config_file(file)
before_tasks, steps_tasks, after_tasks = parse_configs(config)
image = config["image"]

# TODO run docker with given image with volume of host path
# TODO run each task
# os.system("docker run -it ")



# cmd = "git --version"
#
# returned_value = subprocess.call(cmd, shell=True, stdout=False)  # returns the exit code in unix
# print('returned value:', returned_value)

# try:
# except OSError:
#     print('wrongcommand does not exist')

# test = os.system("docker exec -it b3491b0b0eba python my_script.py")
# print(test)
#
# test = os.system("docker exec -it 137617d15fd6 python my_script.py")
# print(test)

# test = os.system("docker exec -it 137617d15fd6 ls")
# print(test)

