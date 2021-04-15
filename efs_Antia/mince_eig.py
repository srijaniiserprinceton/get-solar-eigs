import numpy as np
import os
from scipy.integrate import simps
#import matplotlib.pyplot as plt

# importing files containing the global variables
import globalvars as GV
# reading global variables --- user-dependent
gvar = GV.globalVars()

cwd = os.getcwd()
sd = f'{gvar.eigdir}' #storage directory

if(os.path.isdir(sd) == False):	os.mkdir(sd)

# checking if efs should be scaled
with open(f".config", "r") as f:
	dirnames = f.read().splitlines()

get_scaled = dirnames[2]

nl = np.loadtxt('nl.dat')
U_list = np.loadtxt('eigU.dat')
V_list = np.loadtxt('eigV.dat')
mode_count = len(nl)

r = np.loadtxt('r.dat')
rho = np.loadtxt('rho.dat')

if(get_scaled == 'scaled'):
	sqrt_rho = np.sqrt(rho)
	U_list = U_list * (sqrt_rho * r)[np.newaxis, :]
	V_list = V_list * (sqrt_rho * r)[np.newaxis, :]

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

	L = np.sqrt(l_pres* (l_pres + 1))
	norm_integrand = U*U + L*L*V*V

	if(get_scaled): norm = simps(norm_integrand, x=r)
	else: norm = simps(norm_integrand * rho * r**2, x=r)

	# getting normalized efns
	sqrt_norm = np.sqrt(norm)

	U = U/sqrt_norm
	V = V/sqrt_norm

	np.savetxt(sd + '/' + Uname+'.dat', U)
	np.savetxt(sd + '/' + Vname+'.dat', V)
