import os
import sys
import subprocess

try:
	os.mkdir('/home/shraddha/temp11')
except OSError as e:
	print (e)
#to do install git
os.chdir('/home/shraddha/temp11')
ec= os.system('apt list --installed | grep git')
if ec != 0:
	os.system('sudo apt-get install git -y')
os.system('git init')
ec = os.system('git clone http://github.com/shraddha-koli/attribute-parser.git')
print(ec)

