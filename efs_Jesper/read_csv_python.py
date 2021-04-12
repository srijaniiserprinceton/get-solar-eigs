import numpy as np

# specifying file names to read in
ksir_file = open("ksir.csv")
etar_file = open("etar.csv")
lmode_file = open('l.csv')
nmode_file = open('n.csv')

# reading the .csv files into numpy arrays
ksir = np.loadtxt(ksir_file, delimiter=",")
etar = np.loadtxt(etar_file, delimiter=",")
ell = np.loadtxt(lmode_file, delimiter=',') 
n = np.loadtxt(nmode_file, delimiter=',')

# creating the nl array
nl = np.zeros((len(n),2),dtype='int')
nl[:,0] = n
nl[:,1] = ell

np.savetxt('eig_U.dat', ksir)
np.savetxt('eig_V.dat', etar)
np.savetxt('nl.dat', nl)

