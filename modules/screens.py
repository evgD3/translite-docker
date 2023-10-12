from libqtile import bar
from .widgets import *

from colors import BAR_BACKGROUND
from colors import BAR_FONT
from colors import BAR_FONT_SECOND
from colors import BORDER_FOCUS

from libqtile.config import Screen
from modules.keys import terminal
import os

screens = [
    Screen(
        top=bar.Bar(
            [   widget.Sep(padding=3, linewidth=0, background=BAR_BACKGROUND),
                widget.Sep(padding=40, linewidth=0, background=BAR_BACKGROUND), 
                widget.GroupBox(
                                highlight_method='line',
                                this_screen_border=BORDER_FOCUS,
                                this_current_screen_border=BORDER_FOCUS,
                                active=BAR_FONT,
                                inactive=BAR_FONT_SECOND,
                                background=BAR_BACKGROUND),
                widget.Prompt(),
                widget.Spacer(length=5),
                widget.WindowName(foreground=BAR_FONT,fmt='{}'),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(icon_size = 20),
                volume,
                widget.Battery(
                    foreground = BAR_FONT,
                    low_foreground = "#ff4444",
                    charge_char = "󰚥",
                    discharge_char = "󰂆",
                    empty_char = "󰢟",
                    full_char = "󰂅",
                    format = '[{char} {percent:2.0%}]',
                    notify_bellow = 0.25,
                    low_percentage = 0.25,
                    fontsize=18,
                    font='Font Awesome 5 Free',),
                widget.Clock(format='  %d-%m %a %I:%M',
                             foreground=BAR_FONT),
                                                
                widget.TextBox(
                    text=' ',
                    mouse_callbacks= {
                        'Button1':
                        lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))
                    },
                    foreground=BAR_FONT
                ),

                widget.Spacer(length=12)
            ],
            30,  # height in px
            background=BAR_BACKGROUND
        ), ),
]
