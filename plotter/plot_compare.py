import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--n", help="radial order",
                    type=int, default=0)
parser.add_argument("--ell", help="angular degree",
                    type=int, default=200)
ARGS = parser.parse_args()

compare1 = "Jesper"
compare2 = "gyre_nonadiabatic"
eftype_list = ["Jesper", "Antia", "modelS", "gyre_adiabatic", "gyre_nonadiabatic"]

nl1 = np.loadtxt(f"efs_{compare1}/snrnmais_files/data_files/nl.dat").astype('int')
nl2 = np.loadtxt(f"efs_{compare2}/snrnmais_files/data_files/nl.dat").astype('int')
r = np.loadtxt(f"efs_{compare2}/snrnmais_files/data_files/r.dat")


def get_eigs(n, ell):
    idx1 = nl1.tolist().index([n, ell])
    idx2 = nl2.tolist().index([n, ell])
    U1 = np.loadtxt(f"efs_{compare1}/snrnmais_files/eig_files/U{idx1}.dat", dtype="complex")
    V1 = np.loadtxt(f"efs_{compare1}/snrnmais_files/eig_files/V{idx1}.dat", dtype="complex")
    U2 = np.loadtxt(f"efs_{compare2}/snrnmais_files/eig_files/U{idx2}.dat", dtype="complex")
    V2 = np.loadtxt(f"efs_{compare2}/snrnmais_files/eig_files/V{idx2}.dat", dtype="complex")
    return (U1, V1), (U2, V2)


def plot_eigs(n, ell):
    (U1, V1), (U2, V2) = get_eigs(n, ell)
    fig, axs = plt.subplots(nrows=2, figsize=(6, 6))
    axs = axs.flatten()
    axs[0].plot(r, U1, 'r')
    axs[0].plot(r, U2.real, '--k')
    axs[0].plot(r, U2.imag, '--b')
    axs[0].set_xlabel('radius')
    axs[0].set_title(f'U-{n}-{ell}')
    axs[1].plot(r, V1, 'r')
    axs[1].plot(r, V2.real, '--k')
    axs[1].plot(r, V2.imag, '--b')
    axs[1].set_xlabel('radius')
    axs[1].set_title(f'V-{n}-{ell}')
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    n = ARGS.n
    ell = ARGS.ell
    fig = plot_eigs(n, ell)
    fig.show()
    
