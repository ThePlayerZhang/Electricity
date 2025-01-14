import threading

import pygame

from Electricity.Color import *
from Electricity.Config import *
from Electricity.Map import *

log("Hello from Electricity engin! https://github.com/ThePlayerZhang/Electricity")

pygame.init()
log("Complete initiation pygame")

frame = pygame.display.set_mode(window_size)
log("Complete initiation window")


class Commandline(threading.Thread):
    def run(self):
        while True:
            try:
                command = input()
                try:
                    commandline_command[command]()
                except KeyError:
                    exec(command)
            except Exception as e:
                log("%s: %s" % (e.__class__.__name__, e), "commandline")


level = Map()


def map_load(name):
    level.load(name)


commandline = Commandline(daemon=True)
commandline.start()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    frame.fill(hex_color(level.map["background"]))
    pygame.display.update()
