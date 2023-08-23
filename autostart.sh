#!/bin/sh
wal -i /home/ejix/Downloads/269246.jpg
setxkbmap -option 'caps:super'
setxkbmap 'us,ru' -option 'grp:alt_shift_toggle'
picom --config /home/ejix/.config/picom/picom.conf -b
#picom & disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed

# Low battery notifier
~/.config/qtile/scripts/check_battery.sh & disown

# Start welcome
eos-welcome & disown

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME
