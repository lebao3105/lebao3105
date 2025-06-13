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
export GTK_THEME="Dracula-pink-accent"
export ICON_THEME="Tela-red-dark"
export PYTHONPATH="$HOME/.local/lib/python3.13/site-packages:$PYTHONPATH"

run fcitx5 -d
run flameshot
run conky
run feh --bg-scale --no-fehbg ~/.wallpaper/macOS_26_Dark.jpg
