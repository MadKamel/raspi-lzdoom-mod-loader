# raspi-lzdoom-mod-loader

I made this script to make LZDoom mods easier to load. This script was built with the Raspberry Pi 3 (4 too, I guess) in mind.


## How to use

To utilize this script, you have to modify moddata.py with entries for any mod you want to add. There are three lists to add to: name, description, and args. Name is the display name of the mod. Description is the display description of the mod. Args is the command-line param to use for the particular mod, such as "-file Zion/zionv08.pk3".


## Notes

This script is completely text-based and without a GUI. I don't plan to ever add a GUI on top of the script mechanics either.
