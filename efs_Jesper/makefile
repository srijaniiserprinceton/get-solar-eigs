# .PHONY defines parts of the makefile that are not dependant on any specific file
.PHONY = help setup test run clean environment

# Defines the default target that `make` will to try to make, or in the case of a phony target, execute the specified commands
# This target is executed whenever we just type `make`
.DEFAULT_GOAL = setup
# The @ makes sure that the command itself isnt echoed in the terminal
setup:
	@mkdir /home/sbdas/Research/Helioseismology/get-solar-eigs/efs_Jesper/snrnmais_files/eig_files
	@mkdir /home/sbdas/Research/Helioseismology/get-solar-eigs/efs_Jesper/snrnmais_files/data_files
	@idl -e "efs"
	@python /home/sbdas/Research/Helioseismology/get-solar-eigs/efs_Jesper/read_csv_python.py
	@python /home/sbdas/Research/Helioseismology/get-solar-eigs/efs_Jesper/mince_eig.py
	@mv *.dat /home/sbdas/Research/Helioseismology/get-solar-eigs/efs_Jesper/snrnmais_files/data_files/.
	@mv /home/sbdas/Research/Helioseismology/get-solar-eigs/efs_Jesper/dlfiles/w_samarth.dat /home/sbdas/Research/Helioseismology/get-solar-eigs/efs_Jesper/data/w_s/.
	# generating the w_s data from data/w_s/w_samarth.dat
	@python /home/sbdas/Research/Helioseismology/get-solar-eigs/efs_Jesper/write_w.py
	@rm /home/sbdas/Research/Helioseismology/get-solar-eigs/efs_Jesper/data/w_s/w_samarth.dat
	@rm -rf /home/sbdas/Research/Helioseismology/get-solar-eigs/efs_Jesper/dlfiles
	@rm *.csv
	@rm /home/sbdas/Research/Helioseismology/get-solar-eigs/efs_Jesper/snrnmais_files/data_files/eigU.dat
	@rm /home/sbdas/Research/Helioseismology/get-solar-eigs/efs_Jesper/snrnmais_files/data_files/eigV.dat
	@echo '---------------------------------------------------------------------'
	@echo '       Eigenfrequency and Eigenfunciton SUCCESSFULLY GENERATED       '
	@echo '---------------------------------------------------------------------'
help:
	@echo '---------------------------------HELP--------------------------------'
	@echo 'TO EXTRACT EIGENFREQUENCIES AND EIGENFUNCTIONS: python make_config.py'
	@echo '-------------------------------------------------------------------'

clean:
	@rm -rf /home/sbdas/Research/Helioseismology/get-solar-eigs/efs_Jesper/snrnmais_files
	@rm -rf /home/sbdas/Research/Helioseismology/get-solar-eigs/efs_Jesper/dlfiles
