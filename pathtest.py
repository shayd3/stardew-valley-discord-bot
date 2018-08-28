# path test

import os
import sys

path = sys.argv[1]
basepath, fname = os.path.split(path)
print("directory:", basepath)
if os.path.exists(basepath):
    print("directory exists")
else:
    print("directory does not exist!")
    sys.exit()

if not fname:
    print("no filename provided!")
    sys.exit()
print("filename:", fname)
if os.path.exists(path):
    print("filename exists")
else:
    print("filename not found!")
    print("directory contents:")
    for fn in os.listdir(basepath):
        print(fn)