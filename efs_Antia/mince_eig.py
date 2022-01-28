import numpy as np
from scipy.integrate import simps
import globalvars as GV
from tqdm import tqdm
from scipy import interpolate
import os

gvar = GV.globalVars()
cwd = os.getcwd()
sd = f'{gvar.eigdir}' #storage directory

current_dir = os.path.dirname(os.path.realpath(__file__))
package_dir = os.path.dirname(current_dir)
r_global = np.loadtxt(f"{package_dir}/r_global.dat")


if(os.path.isdir(sd) == False):	os.mkdir(sd)

# checking if efs should be scaled
with open(f".config", "r") as f:
    dirnames = f.read().splitlines()

get_scaled = dirnames[2]

nl = np.loadtxt('nl.dat')
U_list = np.loadtxt('eigU.dat')
V_list = np.loadtxt('eigV.dat')
mode_count = len(nl)

r_local = np.loadtxt('r.dat')
rho = np.loadtxt('rho.dat')

if(get_scaled == 'scaled'):
    sqrt_rho = np.sqrt(rho)
    U_list = U_list * (sqrt_rho * r_local)[np.newaxis, :]
    V_list = V_list * (sqrt_rho * r_local)[np.newaxis, :]

l_pres = 0
l_prev = -1

for i in tqdm(range(mode_count), "Creating U, V"):
    l_pres = int(nl[i][1])
    if(l_prev != l_pres):
        #print('l = '+str(l_pres))
        l_prev = l_pres
    Uname = 'U'+str(i)
    Vname = 'V'+str(i)
    U, V = U_list[i], V_list[i]

    fU = interpolate.interp1d(r_local, U, kind='linear', fill_value='extrapolate')
    fV = interpolate.interp1d(r_local, V, kind='linear', fill_value='extrapolate')
    U = fU(r_global)
    V = fV(r_global)

    L = np.sqrt(l_pres* (l_pres + 1))
    norm_integrand = U*U + L*L*V*V
    norm = simps(norm_integrand, x=r_global)

    # getting normalized efns
    sqrt_norm = np.sqrt(norm)

    U = U/sqrt_norm
    V = V/sqrt_norm

    np.savetxt(sd + '/' + Uname+'.dat', U)
    np.savetxt(sd + '/' + Vname+'.dat', V)
