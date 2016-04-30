from os import listdir
import time
import subprocess

import os
import time
import subprocess

a = listdir("C:\Users\Vipien\Downloads\Connect365\Connect365")
for script in a:
	script = script.split('.')
	if str(script[1]) == 'ui':
		os.system("pyuic4 "+str(script[0])+".ui -o "+str(script[0])+".py")
		time.sleep(1)