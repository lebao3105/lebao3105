#!/usr/bin/env bash

run() {
    if ! pgrep -f "$1"; then
        "$@" &
    fi
}

export GTK_IM_MODULE=fcitx
export XMODIFIERS="@im=fcitx"
export QT_IM_MODULE=fcitx
export XCURSOR_PATH="$HOME/.local/share/icons"
export XCURSOR_THEME=Adwaita

alias sudo=doas

run picom --backend xrender
run fcitx5 -d
run flameshot
run blueman-applet
run feh --bg-scale --no-fehbg --randomize ~/.wallpaper/*
