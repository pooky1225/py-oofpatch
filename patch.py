import os
import requests
import sys
import pathlib
#vars
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
print(path)
listsub = [f.path for f in os.scandir(path) if f.is_dir()]
print(listsub)
listsub = ''.join(listsub)
pathf = (listsub+'\content\sounds\\')
os.chdir(pathf)
print(cwd)
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
input('finished, press <enter> to exit')

