# get-solar-eigs

**Repository to extract and store Model-S eigenfunctions and eigenfrequencies for normal-mode helioseismic studies**

User can clone this repository to use solar standard model eigenfunctions that we got from H.M.Antia (HMA) or Jesper Schou (JS). This provides a seamless way to access these SNRNMAIS data (nomenclature as used in Lavely & Ritzwoller, 1992).

The source of the generated data files are hosted in a OneDrive cloud location which is automatically retrieved during the course of running the ```make_config.py``` under ```efs_Antia``` or ```efs_Jesper```. Only the necessary files are retained and the rest is cleaned up automatically to prevent unnecessary memory occupation.

## Scaling and normalization of eigenfunctions
For ease of reference, let U be the radial eigenfunction and V be the horizontal eigenfunction. 
* *Unscaled eigenfunction*: U and V are unscaled and are actually the U_{nl}(r) and V_{nl}(r) respectively. This feature is only available in ```efs_Antia``` as of now.
* *Scaled eigenfunctions*: U and V are scaled by the factor sqrt(rho) * r. This feature is available in both ```efs_Antia``` and ```efs_Jesper```.

The eigenfunctions (scaled or unscaled) are stored after normalization. This means:
* For unscaled eigenfunctions: Integrating [U * U + l(l+1) * V * V] * rho * r * r over the solar radius should give 1.0.
* For scaled eigenfunctions: Integrating [U * U + l(l+1) * V * V] over the solar radius should give 1.0.

## How to use the package

Open the terminal and go to your local directory where you want to clone the repository and use ```git clone``` as follows
```bash
git clone https://github.com/srijaniiserprinceton/get-solar-eigs.git
```
Enter the directory ```get-solar-eigs```
```bash
cd get-solar-eigs
```
We recommend creating the ```helio``` environment from the ```environment.yml``` (incase all the dependencies are not already in your current conda environment), 
```bash
conda env create -f environment.yml
conda activate helio
```
After all the dependencies have been installed in the environment, simply run the ```make_config.py``` file using
```python
python make_config.py
```
A prompt will ask which set of eigenfunctions you want to use.

```bash
Select eigenfunctions (default 0): Enter
0 - Jesper
1 - Antia
2 - ModelS (adiabatic)
3 - GYRE-model (adiabatic)
4 - GYRE-model (nonadiabatic)
```
After, making a selection (say 0), a prompt asking for a preferential location for storing the final data files will be asked. The default location will be chosen as the current working directory. 
```
Enter location to store the eigenfunctions and output files:Default: /home/sbdas/Research/Helioseismology/get-solar-eigs/efs_Jesper --
```
If the user wants to store them elsewhere, the absolute path for that location should be entered at the prompt (this is useful when using ```\scratch``` storage in a cluster). If not, the user can press ```return``` key to proceed with the storage in the current working directory.

These will take around 5-7 minutes to finish the extraction of the (A) SNRNMAIS eigenfunctions, eigenfrequencies and (B) some other data files like the radius, density, frequency, list of n and l. (A) can be found in the directories ```snrnmais_files/data_files``` and (B) can be found in ```snrnmais_files/eig_files```. The description of the files and what they contain is as follows
* ```snrnmais_files/data_files/r.dat```: The 1D grid in radius in units of solar radius.
* ```snrnmais_files/data_files/rho.dat```: The 1D profile in density.
* ```snrnmais_files/data_files/nl.dat```: The ordered array in the form ```[n,l]```.
* ```snrnmais_files/data_files/muhz.dat```: The SNRNMAIS (unperturbed) eigenfrequencies for all the (n,l) multiplets ordered according to the multiplets stored in```nl.dat```.
* ```snrnmais_files/eig_files/UXXXX.dat```: The radial eigenfunctions belonging to the multiplets (n,l) in the same order as in ```nl.dat```.
* ```snrnmais_files/eig_files/VXXXX.dat```: The horizontal eigenfunctions belonging to the multiplets (n,l) in the same order as in ```nl.dat```.

## Dependencies
* Python Libraries required: numpy, os
* Python version >= 3.7
* Fortran version used: GNU Fortran 7.4.0
* IDL 8.6.1 (to be made optional)

***CAUTION: Running this code will generate data files of cumulative size ~ 5GB***
