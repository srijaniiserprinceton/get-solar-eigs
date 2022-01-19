# .PHONY defines parts of the makefile that are not dependant on any specific file
.PHONY = help setup test run clean environment

# Defines the default target that `make` will to try to make, or in the case of a phony target, execute the specified commands
# This target is executed whenever we just type `make`
.DEFAULT_GOAL = setup
# The @ makes sure that the command itself isnt echoed in the terminal
setup:
	@mkdir /scratch/g.samarth/get-solar-eigs/efs_Antia/snrnmais_files/eig_files
	@mkdir /scratch/g.samarth/get-solar-eigs/efs_Antia/snrnmais_files/data_files
	@gfortran /scratch/g.samarth/get-solar-eigs/efs_Antia/read_eigen.f90
	@/scratch/g.samarth/get-solar-eigs/efs_Antia/a.out
	@rm /scratch/g.samarth/get-solar-eigs/efs_Antia/a.out
	@python /scratch/g.samarth/get-solar-eigs/efs_Antia/mince_eig.py
	@mv *.dat /scratch/g.samarth/get-solar-eigs/efs_Antia/snrnmais_files/data_files/.
	@mv /scratch/g.samarth/get-solar-eigs/efs_Antia/data/w_s /scratch/g.samarth/get-solar-eigs/efs_Antia/snrnmais_files/data_files/.
	@rm -rf /scratch/g.samarth/get-solar-eigs/efs_Antia/dlfiles
	@rm /scratch/g.samarth/get-solar-eigs/efs_Antia/snrnmais_files/data_files/eigU.dat
	@rm /scratch/g.samarth/get-solar-eigs/efs_Antia/snrnmais_files/data_files/eigV.dat
	@echo '---------------------------------------------------------------------'
	@echo '       Eigenfrequency and Eigenfunciton SUCCESSFULLY GENERATED       '
	@echo '---------------------------------------------------------------------'
help:
	@echo '---------------------------------HELP--------------------------------'
	@echo 'TO EXTRACT EIGENFREQUENCIES AND EIGENFUNCTIONS: python make_config.py'
	@echo '-------------------------------------------------------------------'

clean:
	@rm -rf /scratch/g.samarth/get-solar-eigs/efs_Antia/snrnmais_files
	@rm -rf /scratch/g.samarth/get-solar-eigs/efs_Antia/dlfiles
