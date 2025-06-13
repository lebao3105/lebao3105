## Dotfiles for Linux

### Past pack

* Hyprland
* Hyprpaper
* Waybar
* Swaync
* Wlogout
* Alacritty
* Ly (no configuration)
* NNN (file manager, no configuration)
* Rofi of course, theme modified from [here](https://www.reddit.com/r/unixporn/comments/18ktjh1/hyprland_asahilinux_made_my_mac_an_ultimate_dev/) (find OP's github link).

### Present pack

* AwesomeWM (*)
* Feh (as I somehow can't set the wallpaper using AwesomeWM's `gears`)
* Rofi, modified from old config + used colors from [here](https://github.com/refact0r/system24).
* Xfce Terminal
* Flameshot (no configuration)
* Conky (no configuration)
* Feh (no configuration)

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

Uncomment lines that import and use `nice` module.