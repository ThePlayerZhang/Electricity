from .Log import log
import json
import os


def map_list():
    log(", ".join(os.listdir("./Map")))


class Map:
    def __init__(self):
        self.map = {"name": "None", "background": "#000000", "data": []}

    def load(self, name):
        with open("Map/%s.electricitymap" % name, "r") as file:
            self.map = json.loads(file.read())
