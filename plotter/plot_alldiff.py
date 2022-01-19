import numpy as np
import matplotlib.pyplot as plt
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--n", help="radial order",
                    type=int, default=0)
parser.add_argument("--ell", help="angular degree",
                    type=int, default=200)
ARGS = parser.parse_args()

current_dir = os.path.dirname(os.path.realpath(__file__))
package_dir = os.path.dirname(current_dir)
r = np.loadtxt(f"{package_dir}/r_global.dat")

eftype_list = ["Jesper", "modelS", "gyre_adiabatic", "gyre_nonadiabatic"]
colors = ["red", "green", "blue", "black"]
plotlw = 1.0

nl = []
for eftype in eftype_list:
    nl.append(np.loadtxt(f"efs_{eftype}/snrnmais_files/data_files/nl.dat").astype('int'))


def get_eigs(n, ell):
    U = []
    V = []
    for ief, eftype in enumerate(eftype_list):
        idx = nl[ief].tolist().index([n, ell])
        U.append(np.loadtxt(f"efs_{eftype}/snrnmais_files/eig_files/U{idx}.dat", dtype="complex"))
        V.append(np.loadtxt(f"efs_{eftype}/snrnmais_files/eig_files/V{idx}.dat", dtype="complex")*np.sqrt(ell*(ell+1)))
    return U, V


def plot_eigs(n, ell):
    U, V = get_eigs(n, ell)
    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(6, 6))
    for iu, _U in enumerate(U):
        axs[0, 0].plot(r, _U, label=eftype_list[iu], color=colors[iu],
                       linewidth=plotlw)
    axs[0, 0].set_xlabel('$r/R_\odot$')
    axs[0, 0].set_title(f'$U_{{{n}}}^{{{ell}}}$')
    axs[0, 0].legend()

    for iv, _V in enumerate(V):
        axs[0, 1].plot(r, _V, label=eftype_list[iv], color=colors[iv],
                       linewidth=plotlw)
    axs[0, 1].set_xlabel('$r/R_\odot$')
    axs[0, 1].set_title(f'$V_{{{n}}}^{{{ell}}}$')
    axs[0, 1].legend()

    for iu, _U in enumerate(U[1:]):
        axs[1, 0].plot(r, _U - U[0], label=eftype_list[iu+1], color=colors[iu+1],
                       linewidth=plotlw)
    axs[1, 0].set_xlabel('$r/R_\odot$')
    axs[1, 0].set_title(f'$(U - U_j)_{{{n}}}^{{{ell}}}$')
    axs[1, 0].legend()

    for iv, _V in enumerate(V[1:]):
        axs[1, 1].plot(r, _V - V[0], label=eftype_list[iv+1], color=colors[iv+1],
                       linewidth=plotlw)
    axs[1, 1].set_xlabel('$r/R_\odot$')
    axs[1, 1].set_title(f'$(V - V_j)_{{{n}}}^{{{ell}}}$')
    axs[1, 1].legend()
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    n = ARGS.n
    ell = ARGS.ell
    fig = plot_eigs(n, ell)
    fig.show()
    
