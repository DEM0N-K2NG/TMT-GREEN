import os, sys
os.system("git pull")
try:
    __import__("foxxx").approval()
except Exception as e:
    exit(str(e))
 
 
