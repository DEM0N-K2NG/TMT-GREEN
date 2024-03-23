import os, sys
os.system("git pull")
try:
    __import__("TMT").approval()
except Exception as e:
    exit(str(e))
 
 
