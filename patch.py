import os
from os import path
import requests
cwd = os.getcwd()
path = path.expandvars(r'%localappdata%\Roblox\Versions')
print('roblox path')
print(path)
isExist = os.path.exists(path)
print('Does it exist?')
print(isExist)
print(os.listdir(path))
cwd = os.chdir(path)
ver = input('input the version-xxx folder and press <enter>')
print(ver)
verc = '\\'+ver
pathver = path+verc
finpath = pathver+r'\content\sounds'
oggpath = finpath+r'ouch.ogg'
print('downloading to')
print(finpath)
cwd = os.chdir(finpath)
os.rename('ouch.ogg','ouch.ogg.old')
url = "https://github.com/progamer63/py-oofpatch/blob/main/ouch.ogg"
r = requests.get(url)
with open('ouch.ogg','wb') as outfile:
    outfile.write(r.content)
print('delete ouch.ogg.old')
os.remove("ouch.ogg.old")
print('opening file explorer')
os.startfile(finpath)
input('finished, press <enter> to exit')

