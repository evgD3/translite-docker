from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal
import os

screens = [
    Screen(
        top=bar.Bar(
            [   widget.Sep(padding=3, linewidth=0, background="#16364d"),
                widget.Image(filename='~/.config/qtile/eos-c.png', margin=3, background="#16364d", mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -show combi")}),
                widget.Sep(padding=4, linewidth=0, background="#16364d"), 
                widget.GroupBox(
                                highlight_method='line',
                                this_screen_border="#5294e2",
                                this_current_screen_border="#5294e2",
                                active="#ffffff",
                                inactive="#848e96",
                                background="#16364d"),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#16364d'
                       ),    
                widget.Prompt(),
                widget.Spacer(length=5),
                widget.WindowName(foreground='#99c0de',fmt='{}'),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.CurrentLayoutIcon(scale=0.75),
                widget.Systray(icon_size = 20),
                volume,
                widget.Battery(
                    foreground = "#44ff44",
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
                widget.Clock(format=' %d-%m %a %I:%M',
                             foreground='#9bd689'),
                                                
                widget.TextBox(
                    text='',
                    mouse_callbacks= {
                        'Button1':
                        lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))
                    },
                    foreground='#e39378'
                ),

                widget.Spacer(length=12)
            ],
            30,  # height in px
            background="#001625"  # background color
        ), ),
]
