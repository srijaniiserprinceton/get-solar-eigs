# .PHONY defines parts of the makefile that are not dependant on any specific file
.PHONY = help setup test run clean environment

# Defines the default target that `make` will to try to make, or in the case of a phony target, execute the specified commands
# This target is executed whenever we just type `make`
.DEFAULT_GOAL = setup
# The @ makes sure that the command itself isnt echoed in the terminal
setup:
	@mkdir /Users/srijanbharatidas/Documents/Research/Codes/Helioseismology/get-solar-eigs/efs_Antia/snrnmais_files/eig_files
	@mkdir /Users/srijanbharatidas/Documents/Research/Codes/Helioseismology/get-solar-eigs/efs_Antia/snrnmais_files/data_files
	@gfortran /Users/srijanbharatidas/Documents/Research/Codes/Helioseismology/get-solar-eigs/efs_Antia/read_eigen.f90
	@/Users/srijanbharatidas/Documents/Research/Codes/Helioseismology/get-solar-eigs/efs_Antia/a.out
	@rm /Users/srijanbharatidas/Documents/Research/Codes/Helioseismology/get-solar-eigs/efs_Antia/a.out
	@python /Users/srijanbharatidas/Documents/Research/Codes/Helioseismology/get-solar-eigs/efs_Antia/mince_eig.py
	@mv *.dat /Users/srijanbharatidas/Documents/Research/Codes/Helioseismology/get-solar-eigs/efs_Antia/snrnmais_files/data_files/.
	@mv /Users/srijanbharatidas/Documents/Research/Codes/Helioseismology/get-solar-eigs/efs_Antia/dlfiles/w_samarth.dat /Users/srijanbharatidas/Documents/Research/Codes/Helioseismology/get-solar-eigs/efs_Antia/data/w_s/.
	# generating the w_s data from data/w_s/w_samarth.dat
	@python /Users/srijanbharatidas/Documents/Research/Codes/Helioseismology/get-solar-eigs/efs_Antia/write_w.py
	@rm /Users/srijanbharatidas/Documents/Research/Codes/Helioseismology/get-solar-eigs/efs_Antia/data/w_s/w_samarth.dat
	@rm -rf /Users/srijanbharatidas/Documents/Research/Codes/Helioseismology/get-solar-eigs/efs_Antia/dlfiles
	@echo '---------------------------------------------------------------------'
	@echo '       Eigenfrequency and Eigenfunciton SUCCESSFULLY GENERATED       '
	@echo '---------------------------------------------------------------------'
help:
	@echo '---------------------------------HELP--------------------------------'
	@echo 'TO EXTRACT EIGENFREQUENCIES AND EIGENFUNCTIONS: python make_config.py'
	@echo '-------------------------------------------------------------------'

clean:
	@rm -rf /Users/srijanbharatidas/Documents/Research/Codes/Helioseismology/get-solar-eigs/efs_Antia/snrnmais_files
	@rm -rf /Users/srijanbharatidas/Documents/Research/Codes/Helioseismology/get-solar-eigs/efs_Antia/dlfiles
