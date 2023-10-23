#!/usr/bin/env python3

import os


home_path = os.path.expanduser('~')

with open(f'{home_path}/.cache/wal/colors', 'r') as file:
    colors = file.read()
    colors_list = colors.split()
text_to_write = f'''
BAR_BACKGROUND = '{colors_list[10]}'
BAR_FONT = '#fff'
BAR_FONT_SECOND = '{colors_list[15]}'
BORDER_NORMAL = '{colors_list[11]}'
BORDER_FOCUS = '{colors_list[8]}'
'''
with open(f'{home_path}/.config/qtile/modules/colors.py', 'w') as file:
    file.write(text_to_write)

