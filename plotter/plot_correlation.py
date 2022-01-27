import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--n", help="radial order",
                    type=int, default=0)
parser.add_argument("--ell", help="angular degree",
                    type=int, default=200)
ARGS = parser.parse_args()


def get_eig_corr(i1list, i2list):
    corru = []
    corrv = []
    eigdir1 = f"efs_{compare1}/snrnmais_files/eig_files"
    eigdir2 = f"efs_{compare2}/snrnmais_files/eig_files"
    for i in tqdm(range(len(i1list)), desc='Computing correlation'):
        U1 = np.loadtxt(f"{eigdir1}/U{i1list[i]}.dat", dtype="complex")
        V1 = np.loadtxt(f"{eigdir1}/V{i1list[i]}.dat", dtype="complex")
        U2 = np.loadtxt(f"{eigdir2}/U{i2list[i]}.dat", dtype="complex")
        V2 = np.loadtxt(f"{eigdir2}/V{i2list[i]}.dat", dtype="complex")
        corru.append(np.corrcoef(U1, U2)[0, 1].real)
        corrv.append(np.corrcoef(V1, V2)[0, 1].real)
    return corru, corrv


def plot_corr(i1list, i2list):
    corru, corrv = get_eig_corr(i1list, i2list)
    fig = plt.figure()
    plt.plot(corru, '+k', label='U')
    plt.plot(corrv, 'xr', label='V')
    return fig


eftype_list = ["Jesper", "Antia", "modelS", "gyre_adiabatic", "gyre_nonadiabatic"]
compare1 = eftype_list[0]
compare2 = eftype_list[2]

nl1 = np.loadtxt(f"efs_{compare1}/snrnmais_files/data_files/nl.dat").astype('int')
nl2 = np.loadtxt(f"efs_{compare2}/snrnmais_files/data_files/nl.dat").astype('int')
r = np.loadtxt(f"efs_{compare2}/snrnmais_files/data_files/r.dat")

idx1list = []
idx2list = []

for i in tqdm(range(len(nl1)), desc='Finding common nl'):
    try:
        idx1 = i
        idx2 = np.where((nl1[i, 0] == nl2[:, 0]) *
                     (nl1[i, 1] == nl2[:, 1]))[0][0]
    except IndexError:
        idx1 = None
        idx2 = None

    if idx1 != None:
        idx1list.append(idx1)
        idx2list.append(idx2)

fig = plot_corr(idx1list, idx2list)
fig.show()
