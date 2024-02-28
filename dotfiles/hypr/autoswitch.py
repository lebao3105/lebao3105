"""
Made by @lebao3105: https://github.com/lebao3105
A small script changing between light & dark mode.
Used softwares:
* Hyprland
* Hyprpaper
* GSettings
* Python 3

(only one monitor is used)
Add the script to Hyprland exec-once section.
"""
import os
from datetime import datetime
from time import sleep

# Time of light&dark modes
LIGHT_TIME = 6
DARK_TIME = 18

# Themes
LIGHT_THEME = "adw-gtk3"
DARK_THEME = "adw-gtk3-dark"

## Some themes like Adwaita-GTK3 requires the color scheme
## to 'default', not 'prefer-light'.
## Only cares for light mode.
LIGHT_PREFER_DEFAULT = True

# Wallpaper
LIGHT_WALL = "/home/lebao3105/Pictures/Wallpapers/10-13-6k.jpg"
DARK_WALL = "/home/lebao3105/Pictures/Wallpapers/grid-magenta-6016x6016-10258.jpg"

def main():
    while True:
        now = datetime.now()
        currtime = now.strftime("%H")
        print("Current hour:", currtime)
        
        if DARK_TIME > int(currtime) >= 6:
            print("* Time to switch to light mode!")
            SCHEME = "prefer-light" if not LIGHT_PREFER_DEFAULT else "default"
            
            os.system(f"gsettings set org.gnome.desktop.interface color-scheme '{SCHEME}'")
            os.system(f"gsettings set org.gnome.desktop.interface gtk-theme '{LIGHT_THEME}'") 
            
            os.system(f"hyprctl hyprpaper wallpaper 'HDMI-A-1,{LIGHT_WALL}'")
        else:
            print("* Time to switch to dark mode!")
            os.system("gsettings set org.gnome.desktop.interface color-scheme 'prefer-dark'")
            os.system(f"gsettings set org.gnome.desktop.interface gtk-theme '{DARK_THEME}'")
            
            os.system(f"hyprctl hyprpaper wallpaper 'HDMI-A-1 {DARK_WALL}'")
        print("See you again in one hour!")
        sleep(3600)

if __name__ == "__main__":
    main()
