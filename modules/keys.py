from libqtile.lazy import lazy
from libqtile.config import Key

mod = "mod4"
terminal = "kitty"

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
    Key([mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),
    Key([mod, "shift", "control"], "l", lazy.layout.swap_column_right()),
    Key([mod, "shift"], "space", lazy.layout.flip()),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"],
        "r",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    Key([], "XF86AudioRaiseVolume",lazy.spawn("amixer set Master 3%+")),
    Key([], "XF86AudioLowerVolume",lazy.spawn("amixer set Master 3%-")),
    Key([], "XF86AudioMute",lazy.spawn("amixer set Master toggle")),

    Key([mod], "Return", lazy.spawn("kitty")),
    Key([mod], "f", lazy.spawn("firefox")),
    Key([mod], "p", lazy.spawn("keepassxc")),
    Key([mod], "t", lazy.spawn("telegram-desktop")),
    Key([mod], "g", lazy.spawn("dino")),
    Key([mod], "o", lazy.spawn("okular")),
    Key([mod], "Print", lazy.spawn("flameshot")),
    Key([mod], "r", lazy.spawn("rofi -show combi"), desc="spawn rofi"),
]
