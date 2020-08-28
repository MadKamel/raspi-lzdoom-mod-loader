#! /usr/bin/python3

import os
import moddata

while True:
	os.system('clear')
	for i in range(len(moddata.names)):
		print('\t' + str(i+1) + '.) ' + moddata.names[i], ': ' + moddata.desc[i])
	print('\n')
	cmd = input(' mod => ')
	if cmd == '0':
		quit()

	try:
		allargs = ''
		spl = cmd.split('+')
		for i in range(len(spl)):
			for c in range(len(moddata.names)):
				if spl[i] == str(c+1):
					allargs = allargs + ' ' + moddata.args[c]
		os.system('./lzdoom ' + allargs)
		
	except:
		for i in range(len(moddata.names)):
			if cmd == str(i+1):
				os.system('./lzdoom ' + moddata.args[i])
