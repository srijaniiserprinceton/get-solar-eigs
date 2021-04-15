import numpy as np
import os
#import matplotlib.pyplot as plt

# importing files containing the global variables
import globalvars as GV
# reading global variables --- user-dependent
gvar = GV.globalVars()

cwd = os.getcwd()
sd = f'{gvar.eigdir}' #storage directory

if(os.path.isdir(sd) == False):	os.mkdir(sd)

nl = np.loadtxt('nl.dat')
U_list = np.loadtxt('eigU.dat')
V_list = np.loadtxt('eigV.dat')
r = np.loadtxt('r.dat')
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
