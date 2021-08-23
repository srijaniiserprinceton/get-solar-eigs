import os
import sys
import urllib.request
import time

cwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(cwd)
NL = "\n"

ef_idx = int(input("Select eigenfunctions (default 0): Enter\n 0 - Jesper\n 1 - Antia\n") or "0")
if ef_idx == 0:
    os.chdir(f"{cwd}/efs_Jesper")
else:
    os.chdir(f"{cwd}/efs_Antia")
os.system('python make_config.py')
