import numpy as np
import pygyre as pg
from tqdm import tqdm
from astropy.io import ascii
import globalvars as GV
from scipy import interpolate
from scipy.integrate import simps
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
package_dir = os.path.dirname(current_dir)
r_global = np.loadtxt(f"{package_dir}/r_global.dat")

GVARS = GV.globalVars()
eigdir = GVARS.eigdir
datadir = GVARS.data_filedir

if (not os.path.isdir(eigdir)): os.mkdir(eigdir)
if (not os.path.isdir(datadir)): os.mkdir(datadir)

# checking if efs should be scaled
with open(f".config", "r") as f:
    dirnames = f.read().splitlines()

get_scaled = dirnames[2]
eigtype = dirnames[3]


def create_metadata_file(ell, n):
    fname = f"{filedir}/{fname_prefix}.l{ell}.n+{n}.txt"
    with open(fname) as f:
        metalines = f.readlines()[:4]

    fname_meta = fname + ".meta"
    with open(fname_meta, "w") as f:
        f.writelines(metalines)
    return None


def read_metadata(ell, n):
    fname = f"{filedir}/{fname_prefix}.l{ell}.n+{n}.txt.meta"
    mdat = ascii.read(fname, data_start=2, delimiter='\s')
    if adiabatic:
        omega = mdat[0][4]
    else:
        omega = mdat[0][4] + 1j*mdat[0][5]
    return omega


def read_eigenfunctions(ell, n, idx):
    fname = f"{filedir}/{fname_prefix}.l{ell}.n+{n}.txt"
    data = pg.read_output(fname)
    xi_r = np.array(list(data['xi_r']))
    xi_h = np.array(list(data['xi_h']))

    if adiabatic:
        xi_r = xi_r.real
        xi_h = xi_h.real

    if get_scaled == "scaled":
        xi_r = xi_r * np.sqrt(rho) * r_local
        xi_h = xi_h * np.sqrt(rho) * r_local

    fU = interpolate.interp1d(r_local, xi_r, kind='linear', fill_value='extrapolate')
    fV = interpolate.interp1d(r_local, xi_h, kind='linear', fill_value='extrapolate')
    U = fU(r_global)
    V = fV(r_global)

    L = np.sqrt(ell*(ell+1))
    norm_integrand = U*U.conj() + L*L*V*V.conj()
    norm = simps(norm_integrand, x=r_global)

    U = U/np.sqrt(norm)
    V = V/np.sqrt(norm)

    np.savetxt(f"{eigdir}/U{idx}.dat", U)
    np.savetxt(f"{eigdir}/V{idx}.dat", V)
    return U, V


if __name__ == "__main__":
    if eigtype == "adiabatic": adiabatic = True
    outdir = "adiabatic" if adiabatic else "nonadiabatic"

    if adiabatic:
        fname_prefix = "adiabatic_detail"
        filedir = "dlfiles/adiabatic"
        fnamelist_file = "dlfiles/adiabatic/filenames.txt"
    else:
        fname_prefix = "nonadiabatic_detail"
        filedir = "dlfiles/nonadiabatic"
        fnamelist_file = "dlfiles/nonadiabatic/filenames.txt"

    r_local = np.loadtxt(f"{filedir}/r.dat")
    rho = np.loadtxt(f"{filedir}/rho.dat")

    with open(fnamelist_file) as f:
        fnamelist = f.readlines()
    num_files = len(fnamelist)

    nlist = []
    llist = []
    omegalist = []
    nl_arr = np.zeros((num_files, 2), dtype=np.int16)

    for fcount in tqdm(range(num_files), desc='creating nl, mu'):
        ell = int(fnamelist[fcount].strip('\n').split('.')[1][1:])
        n = int(fnamelist[fcount].strip('\n').split('.')[2][2:])
        nlist.append(n)
        llist.append(ell)
        create_metadata_file(ell, n)
        omega = read_metadata(ell, n)
        omegalist.append(omega)

    sorted_idx = np.argsort(llist)
    nl_arr[:, 0] = np.array(nlist)[sorted_idx]
    nl_arr[:, 1] = np.array(llist)[sorted_idx]
    omega_arr = np.array(omegalist)[sorted_idx]

    np.savetxt(f'{datadir}/nl.dat', nl_arr, fmt='%d')
    np.savetxt(f'{datadir}/muhz.dat', omega_arr, fmt='%.18e')

    for fcount in tqdm(range(num_files), desc='Creating U, V'):
        n = nl_arr[fcount, 0]
        ell = nl_arr[fcount, 1]
        create_metadata_file(ell, n)
        xi_r, xi_h = read_eigenfunctions(ell, n, fcount)
