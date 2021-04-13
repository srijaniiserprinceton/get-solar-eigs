# .PHONY defines parts of the makefile that are not dependant on any specific file
.PHONY = help setup test run clean environment

# Defines the default target that `make` will to try to make, or in the case of a phony target, execute the specified commands
# This target is executed whenever we just type `make`
.DEFAULT_GOAL = setup
# The @ makes sure that the command itself isnt echoed in the terminal
setup:
	@tar -xf /Users/srijanbharatidas/Documents/Research/Codes/Helioseismology/get-solar-eigs/efs_Jesper/dlfiles/efs_Jesper.tar.gz
	@mv /Users/srijanbharatidas/Documents/Research/Codes/Helioseismology/get-solar-eigs/efs_Jesper/dlfiles/w_samarth.dat /Users/srijanbharatidas/Documents/Research/Codes/Helioseismology/get-solar-eigs/efs_Jesper/data/w_s/.
	# generating the w_s data from data/w_s/w_samarth.dat
	@python /Users/srijanbharatidas/Documents/Research/Codes/Helioseismology/get-solar-eigs/efs_Jesper/write_w.py
	@rm /Users/srijanbharatidas/Documents/Research/Codes/Helioseismology/get-solar-eigs/efs_Jesper/data/w_s/w_samarth.dat
	@mv /Users/srijanbharatidas/Documents/Research/Codes/Helioseismology/get-solar-eigs/efs_Jesper/data/w_s /Users/srijanbharatidas/Documents/Research/Codes/Helioseismology/get-solar-eigs/efs_Jesper/snrnmais_files/data_files/.
	@rm -rf /Users/srijanbharatidas/Documents/Research/Codes/Helioseismology/get-solar-eigs/efs_Jesper/dlfiles
	@echo '---------------------------------------------------------------------'
	@echo '       Eigenfrequency and Eigenfunciton SUCCESSFULLY GENERATED       '
	@echo '---------------------------------------------------------------------'
help:
	@echo '---------------------------------HELP--------------------------------'
	@echo 'TO EXTRACT EIGENFREQUENCIES AND EIGENFUNCTIONS: python make_config.py'
	@echo '-------------------------------------------------------------------'

clean:
	@rm -rf /Users/srijanbharatidas/Documents/Research/Codes/Helioseismology/get-solar-eigs/efs_Jesper/snrnmais_files
	@rm -rf /Users/srijanbharatidas/Documents/Research/Codes/Helioseismology/get-solar-eigs/efs_Jesper/dlfiles
	@rm -rf /Users/srijanbharatidas/Documents/Research/Codes/Helioseismology/get-solar-eigs/efs_Jesper/data/w_s