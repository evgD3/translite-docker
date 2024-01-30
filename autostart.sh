#!/bin/sh
wal -i ~/wallpapers/wallhaven-8586my.png
setxkbmap -option 'caps:super'
setxkbmap 'us,ru' -option 'grp:alt_shift_toggle'
picom --config /home/ejix/.config/picom/picom.conf -b

# Low battery notifier
~/.config/qtile/scripts/check_battery.sh & disown

# Start welcome
eos-welcome & disown

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME
