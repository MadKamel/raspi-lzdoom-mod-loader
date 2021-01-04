#! /usr/bin/python3
import datetime, os
today = datetime.date.today()

os.chdir('/home/pi/Desktop/Games/lzdoom')
os.system('wget https://soulsphere.org/hacks/slige/megawad.zip')
os.system('mv megawad.zip megawads/megawad.zip')
os.chdir('megawads')
os.system('unzip megawad.zip')
os.system('sudo rm megawad.zip')
os.system('sudo rm megawad.txt')
os.system('mv megawad.wad megawad-' + str(today) + '.wad')
os.chdir('..')