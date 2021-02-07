# .PHONY defines parts of the makefile that are not dependant on any specific file
.PHONY = help setup test run clean

# Defines the default target that `make` will to try to make, or in the case of a phony target, execute the specified commands
# This target is executed whenever we just type `make`
.DEFAULT_GOAL = setup

# The location of the current working directory
PWD=$(shell pwd)
F_EFN=${PWD}/egvt.sfopal5h5

# The @ makes sure that the command itself isn't echoed in the terminal
setup:
	@mkdir eig_files
	@mkdir data_files
	@gfortran read_eigen.f90
	@./a.out
	@rm a.out
	@python mince_eig.py
	@mv *.dat ./data_files/.
	@echo "---------------------------------------------------------------------"
	@echo "              EIGNEFUNCTIONS SUCCESSFULLY GENERATED                  "
	@echo "COPY data_files AND eig_files TO WORK REPOSITORY AND START USING THEM"
	@echo "---------------------------------------------------------------------"

help:
	@echo "---------------HELP-----------------"
	@echo "To generate and store Solar Eigenfunctions type: make setup"
	@echo "------------------------------------"

clean:
	@rm -r eig_files
	@rm -r data_files