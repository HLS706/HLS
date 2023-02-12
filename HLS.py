import os, sys
try:
    __import__("HLS").Main()
except Exception as e:
    exit(str(e))