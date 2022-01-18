import os
import sys
import urllib.request
import time

cwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(cwd)
NL = "\n"

ef_idx = int(input("Select eigenfunctions (default 0): Enter\n" +
                   "0 - Jesper\n" +
                   "1 - Antia\n" +
                   "2 - ModelS (adiabatic)\n" +
                   "3 - GYRE-model (adiabatic)\n" +
                   "4 - GYRE-model (nonadiabatic)\n" or "0"))
if ef_idx == 0:
    os.chdir(f"{cwd}/efs_Jesper")
elif ef_idx == 1:
    os.chdir(f"{cwd}/efs_Antia")
elif ef_idx == 2:
    os.chdir(f"{cwd}/efs_modelS")
elif ef_idx == 3:
    os.chdir(f"{cwd}/efs_gyre_adiabatic")
elif ef_idx == 4:
    os.chdir(f"{cwd}/efs_gyre_nonadiabatic")
os.system('python make_config.py')

if (ef_idx == 2) or (ef_idx == 3) or (ef_idx == 4):
    os.system('python mince_eig.py')
