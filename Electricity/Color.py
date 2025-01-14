def hex_color(color):
    color = color.lstrip('#')
    return int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16)
