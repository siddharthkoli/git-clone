import os
import sys
import subprocess

'''try:
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
print(ec)'''

subprocess.Popen(['mkdir', 'SidRepo'])
print("Success: Made Directory")
temp = subprocess.Popen(['pwd'], stdout = subprocess.PIPE)
output = str(temp.communicate())
#print(output)
#print(len(output))
#print(output[2:27])
o = output[2:25] + '/SidRepo/'
os.chdir(o)
#subprocess.Popen(['git', 'init'])
#subprocess.Popen(['git remote add origin', 'http://github.com/shraddha-koli/attribute-parser.git'])
p=subprocess.Popen(['git', 'clone', 'https://github.com/siddharthkoli/CTF2020.git'])
p.wait()
print("Success: Repository Cloned")
o = o + 'CTF2020/lakshya/'
os.chdir(o)
print("Running server on LocalHost...")
subprocess.Popen(['python3', 'manage.py', 'runserver'])


