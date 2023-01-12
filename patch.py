import os
import requests
import sys
import pathlib
from datetime import datetime as dt
from datetime import date
from pathlib import Path
print('''

               __             _       _     
              / _|           | |     | |    
   ___   ___ | |_ _ __   __ _| |_ ___| |__  
  / _ \ / _ \|  _| '_ \ / _` | __/ __| '_ \ 
 | (_) | (_) | | | |_) | (_| | || (__| | | |
  \___/ \___/|_| | .__/ \__,_|\__\___|_| |_|
                 | |                        
                 |_|                        
''')
cwd = os.getcwd()
path =(os.path.expanduser('~')+'\AppData\Local\Roblox\Versions')
url = 'https://github.com/progamer63/py-oofpatch/raw/main/ouch.ogg'
print('path '+path)
listsub = str(max(pathlib.Path(path).glob('*/'), key=os.path.getmtime))
pathf = (listsub+'\content\sounds\\')
os.chdir(pathf)
print('cwd '+cwd)
exist=Path('exists.txt')
exist.is_file()
if exist.is_file():
    print('already patched')
    input('press <enter> to exit')
    exit()
else:
    print('exists.txt does not exist, patching...')
print('downloading to')
print(pathf)
os.rename('ouch.ogg','ouch.ogg.old')
print(url)
print(pathf)
print(cwd)
r = requests.get(url).content
with open(pathf+'ouch.ogg','wb') as f:
    f.write(r)
    f.close()
print('delete ouch.ogg.old')
os.remove("ouch.ogg.old")
print('write exists file')
fp = open('exists.txt','w')
now=dt.now()
time=now.strftime("%H:%M:%S %m/%d/%Y")
with open('exists.txt','w') as f:
    f.write(time)
    f.close()
input('finished, press <enter> to exit')
exit()


