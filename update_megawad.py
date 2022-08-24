#! /usr/bin/python3

# This program will download the latest version of the
# daily megawad from soulsphere.org, and run_megawad.py
# will run it.

import datetime, os
today = datetime.date.today()

os.chdir('/home/pi/Desktop/Games/lzdoom') //change this to your working directory, or just comment out.
os.system('wget https://soulsphere.org/hacks/slige/megawad.zip')
os.system('mv megawad.zip megawads/megawad.zip')
os.chdir('megawads')
os.system('unzip megawad.zip')
os.system('sudo rm megawad.zip')
os.system('sudo rm megawad.txt')
os.system('mv megawad.wad megawad-' + str(today) + '.wad')
os.chdir('..')
