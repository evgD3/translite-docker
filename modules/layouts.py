from libqtile import layout
from libqtile.config import Match

COLOR1 = '#5294e2'
COLOR2 = '#2c5380'

layouts = [
    #layout.MonadTall(margin=8, border_focus=COLOR1,
     #                border_normal=COLOR2),
    #layout.Columns(border_focus_stack='#d75f5f'),
    #layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    layout.Bsp(
        border_focus = COLOR1,
        border_normal = COLOR2,
        #border_width = 1,
        margin = [2, 2, 2, 2]),
    layout.Matrix(
        border_focus = COLOR1,
        border_normal = COLOR2,
        #border_width = 1,
        margin = [2, 2, 2, 2]),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

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
        Match(wm_class="Gajim"),
    ]
)
