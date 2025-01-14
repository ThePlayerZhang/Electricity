import datetime
from .Config import *

with open("./latest.log", "w") as log_file:
    log_file.write("Electricity Log\n")


def log(message, state="Info"):
    now = datetime.datetime.now().strftime(log_strftime)
    with open("./latest.log", "a") as file:
        file.write(log_format % (now, state, message))
        print(log_format % (now, state, message), end="")
