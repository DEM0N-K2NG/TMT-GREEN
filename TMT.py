import os, sys
os.system("git pull")
try:
    __import__("foxxxx").approval()
except Exception as e:
    exit(str(e))
 
 
