## Dotfiles for Linux

Used softwares:
* Hyprland
* Hyprpaper
* Waybar
* Swaync
* Wlogout
* Ly (display manager)
* Alacritty
* NNN (file manager)
* AwesomeWM (*)
* Feh (as I somehow can't set the wallpaper using AwesomeWM's `gears`)
* Rofi of course, theme modified from [here](https://www.reddit.com/r/unixporn/comments/18ktjh1/hyprland_asahilinux_made_my_mac_an_ultimate_dev/) (find OP's github link).

\* For the application title bar, clone this [repository](https://github.com/mut-ex/awesome-wm-nice) to `~/.config/awesome/nice`, open `init.lua` and type in two lines:

```lua
lgi.require('Gtk', '3.0')
lgi.require('Gdk', '3.0')
```

Right after this line:
```lua
local lgi = require("lgi")
```

Note that the **edit** (not the clone) is only required if you have GTK 4 installed.
