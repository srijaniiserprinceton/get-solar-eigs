import numpy as np
import os
import sys
from scipy.integrate import simps
#import matplotlib.pyplot as plt

cwd = os.getcwd()
sys.path.append(cwd)

# importing files containing the global variables
import globalvars as GV
# reading global variables --- user-dependent
gvar = GV.globalVars()

cwd = os.getcwd()
sd = f'{gvar.eigdir}' #storage directory

if(os.path.isdir(sd) == False):	os.mkdir(sd)

nl = np.loadtxt(f'{gvar.snrnmais}/data_files/nl.dat')
U_list = np.loadtxt(f'{gvar.snrnmais}/data_files/eigU.dat')
V_list = np.loadtxt(f'{gvar.snrnmais}/data_files/eigV.dat')
r = np.loadtxt(f'{gvar.snrnmais}/data_files/r.dat')
mode_count = len(nl)

l_pres = 0
l_prev = -1
for i in range(mode_count):
	l_pres = int(nl[i][1])
	if(l_prev != l_pres):
		print('l = '+str(l_pres))
		l_prev = l_pres
	Uname = 'U'+str(i)
	Vname = 'V'+str(i)

	U, V = U_list[i], V_list[i]

	# getting normalized efns
	norm_integrand = U*U + V*V
	norm = simps(norm_integrand, x=r)

	sqrt_norm = np.sqrt(norm)

	U = U/sqrt_norm
	V = V/sqrt_norm

	# unscaling by ell, does not apply to ell = 0
	if(l_pres > 0):
		L = np.sqrt(l_pres* (l_pres + 1))
		V = V/L

	np.savetxt(sd + '/' + Uname+'.dat', U)
	np.savetxt(sd + '/' + Vname+'.dat', V)
