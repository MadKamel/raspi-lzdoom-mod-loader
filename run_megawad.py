#! /usr/bin/python3
import os, datetime
today = str(datetime.date.today())

os.system(input('Which source port should run? ') + ' -iwad doom2.wad -file megawads/megawad-' + today + '.wad ' + input('Add additional params here: '))