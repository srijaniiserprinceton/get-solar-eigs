# get-solar-eigs

** There is no need to clone or fork this repository. Just download it **

Repository contains fortran and python script for generating Solar Eigenfunctions and other necessary files to work with eigenfunctions and eigenfrequencies.

Local directory should contain the following data files:
* egvt.sfopal5h5: binary file containing eigenfunctions in compact form
* sfopal5h5: binary file containing r gridpoints and rho values

These files can be downloaded at: https://drive.google.com/drive/folders/1NmmWv6FUxNtKBKxxcV7TXYsE-4DEeVUP?usp=sharing

## Using the makefile

In the terminal, type **make** to generate the diretories *data_files* and *eig_files*. Copy these to your work repository to start using them.

* Python Libraries required: numpy, sympy, matplotlob, os
* Python version >= 2.7.15
* Fortran version used: GNU Fortran 7.4.0
* CAUTION: Running this code will generate data files of cumulative size ~ 2.5GB
