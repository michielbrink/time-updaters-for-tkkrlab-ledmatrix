import os
import subprocess
import time


while(1):
	output = subprocess.check_output(["date", "+%T"]);
	os.system("wget --spider 'http://10.42.2.104/~jawsper/led.php?action=text&text=MICHIEL zegt:  '" + output)
