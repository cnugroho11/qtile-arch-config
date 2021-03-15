#!/bin/bash

# Power manager
xfce4-power-manager &

# Bluetooth tray
blueberry-tray &

# Compositro
picom &

# Wallpaper
nitrogen --restore &

# Notification daemon
dunst &
