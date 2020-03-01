import os
import sys
import subprocess

try:
	os.mkdir('/home/shraddha/temp1')
except OSError as e:
	print (e)
#to do install git
os.chdir('/home/shraddha/temp1')
os.system('sudo apt-get install git -y')
os.system('git init --bare')
ec = os.system('git clone http://github.com/shraddha-koli/attribute-parser.git')
print(ec)

