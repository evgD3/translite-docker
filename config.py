import os
import subprocess

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

COLOUR1 = "#0009cf"
COLOUR2 = "#263238"
COLOUR3 = "#000000"


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

@hook.subscribe.client_new
def floating_dialogs(window):
    dialog = window.window.get_wm_type() == 'dialog'
    transient = window.window.get_wm_transient_for()
    if dialog or transient:
        window.floating = True

mod = "mod4"


keys = [    
    #move focus to 
    Key([mod], "h", lazy.layout.left(), desc="left"),
    Key([mod], "l", lazy.layout.right(), desc="right"),
    Key([mod], "j", lazy.layout.down(), desc="down"),
    Key([mod], "k", lazy.layout.up(), desc="up"),
    Key([mod], "space", lazy.layout.next(), desc="other window"),
    
    #move window to
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="up"),
    
    #grow windows to 
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all sizes"),
    
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="split and unsplit"),
    
    Key([mod], "Return", lazy.spawn("kitty")),
    Key([mod], "f", lazy.spawn("firefox")),
    Key([mod], "p", lazy.spawn("keepassxc")),
    Key([mod], "t", lazy.spawn("telegram-desktop")),
    Key([mod], "g", lazy.spawn("gajim")),
    Key([mod], "o", lazy.spawn("okular")),
    #Key([mod], "b", bar.Bar.show(is_show=False)),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    #Key([mod], "i", lazy.window.toggle_floating()),
    Key([mod], "u", lazy.window.toggle_fullscreen()),
]

groups = [                                                                 
    Group("1", label = "1"),
    Group("2", label = "2"),
    Group("3", label = "3"),
    Group("4", label = "4"),
    Group("5", label = "5"),
    Group("6", label = "6"),
    Group("7", label = "7"),
    Group("8", label = "8"),
    Group("9", label = "9"),
    Group("0", label = ""),
]                                                        

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    #- layout.Columns(border_focus_stack=["#d7ff5f", "#8f3d3d"], border_width=4),
    #- layout.Max(),
    
    #- layout.Stack(num_stacks=4),
    layout.Bsp(
        border_focus = COLOUR1,
        border_normal = COLOUR3,
        border_width = 1,
        margin = [2, 2, 2, 2]),

    #layout.Matrix(
     #   border_focus = COLOUR1,
     #   border_normal = COLOUR3,
     #   border_width = 1,
     #   margin = [2, 2, 2, 2]),
    #- layout.MonadTall(),
    #- layout.MonadWide(),
    #layout.RatioTile(
     #   border_focus = COLOUR1,
     #   border_normal = COLOUR3,
     #   border_width = 1,
     #   margin = [2, 2, 2, 2]),
    #+ layout.Tile(),
    #= layout.TreeTab(),
    #- layout.VerticalTile(),
    #- layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(
                    borderwidth=1,
                    highlight_method='block',
                    block_highlight_text_color='#263238',
                    this_current_screen_border='#f9f9f9',
                    rounded=True,),
                
                widget.Prompt(),

                #widget.Wallpaper(
                #    directory = '/home/ejix/Pictures/wallpapers/desktop/',),
                    #wallpaper_command = ['wal -i'],),
                
                widget.Chord(
                    chords_colors={
                        "launch": ("#00ff11", "#334433"),
                    },
                    name_transform=lambda name: name.upper(),),

                widget.Spacer(length=30),
                
                widget.PulseVolume(
                    padding = 5,
                    mute_command = None,
                    volume_up_command = None,
                    volume_down_command = None,),

#                widget.Backlight(
 #                   background = "#ff0000",
  #                  brightness_file = '/sys/class/backlight/intel_backlight',
   #                 change_command = f"brightnessctl s {0}%",
    #                step = 5,
     #               ),

                widget.Battery(
                    foreground = "#44ff44",
                    low_foreground = "#ff4444",
                    charge_char = "POW",
                    discharge_char = "DIS",
                    empty_char = "LOW",
                    full_char = "FULL",
                    format = '[{char} {percent:2.0%}]',
                    notify_bellow = 0.25,
                    low_percentage = 0.25),
                
                widget.Spacer(length=1350),
                
                # widget.StatusNotifier(),
                
                widget.Systray(),
                
                widget.Clock(format="[%d-%m    %a %I:%M]"),
                #widget.QuickExit(),

                widget.QuickExit(default_text=''),
            ],
            
            24,
            border_width=[5, 50, 5, 50],
            border_color=["263238", "263238", "263238", "263238"],
            margin=5,
            background="#263238",
            #opacity='0,9'
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),
        Match(wm_class="telegram-desktop"),
        Match(wm_class="gajim"),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = False

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "LG3D"
