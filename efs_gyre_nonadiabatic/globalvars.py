"""Handles global variables"""
import numpy as np
import getpass
import os

# filenamepath = os.path.realpath(__file__)
# filepath = '/'.join(filenamepath.split('/')[:-1])
# configpath = '/'.join(filepath.split('/')[:-1])
# with open(f"{configpath}/.config", "r") as f:
#     dirnames = f.read().splitlines()
#----------------------------------------------------------------------
#                       All qts in CGS
# M_sol = 1.989e33 g
# R_sol = 6.956e10 cm
# B_0 = 10e5 G
# OM = np.sqrt(4*np.pi*R_sol*B_0**2/M_sol)
# rho_0 = M_sol/(4pi R_sol^3/3) = 1.41 ~ 1g/cc (for kernel calculation)
#----------------------------------------------------------------------


class globalVars():

    def __init__(self, fwindow=50, rmin=0.0, rmax=1.0, smax=5):

        with open(f".config", "r") as f:
            dirnames = f.read().splitlines()

        self.local_dir = dirnames[0]
        self.scratch_dir = dirnames[1]
        self.snrnmais = f"{self.scratch_dir}/snrnmais_files"
        self.datadir = f"{self.scratch_dir}/data"
        self.outdir = f"{self.scratch_dir}/output_files"
        self.progdir = self.local_dir
        self.eigdir = f"{self.snrnmais}/eig_files"
        self.data_filedir = f"{self.snrnmais}/data_files"

        #all quantities in cgs
        self.M_sol = 1.989e33 #gn,l = 0,200
        self.R_sol = 6.956e10 #cm
        self.B_0 = 10e5 #G
        self.OM = np.sqrt(4*np.pi*self.R_sol*self.B_0**2/self.M_sol) 
        # should be 2.096367060263202423e-05 for above numbers
