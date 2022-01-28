import os
import sys
import urllib.request
import time

cwd = os.getcwd()
sys.path.append(cwd)
NL = "\n"

def create_makefile():
    f = open(f"{cwd}/makefile", "w")
    f.write("# .PHONY defines parts of the makefile that ")
    f.write("are not dependant on any specific file\n")
    f.write(".PHONY = help setup test run clean environment\n\n")
    f.write("# Defines the default target that `make` will to try to make, ")
    f.write("or in the case of a phony target, execute the specified commands\n")
    f.write("# This target is executed whenever we just type `make`\n")
    f.write(".DEFAULT_GOAL = setup\n")

    f.write("# The @ makes sure that the command itself ")
    f.write("isnt echoed in the terminal\n")
    f.write("setup:\n")
    f.write(f"\t@mkdir {snrdir}/eig_files\n")
    f.write(f"\t@mkdir {snrdir}/data_files\n")
    f.write(f"\t@gfortran {cwd}/read_eigen.f90\n")
    f.write(f"\t@{cwd}/a.out\n")
    f.write(f"\t@rm {cwd}/a.out\n")
    f.write(f"\t@python {cwd}/mince_eig.py\n")
    f.write(f"\t@mv *.dat {snrdir}/data_files/.\n")
    f.write(f"\t@rm -rf {datadir}/dlfiles\n")
    f.write(f"\t@rm {snrdir}/data_files/eigU.dat\n")
    f.write(f"\t@rm {snrdir}/data_files/eigV.dat\n")
    f.write("\t@echo '---------------------------------------------------------------------'\n")
    f.write("\t@echo '       Eigenfrequency and Eigenfunciton SUCCESSFULLY GENERATED       '\n")
    f.write("\t@echo '---------------------------------------------------------------------'\n")
    f.write("help:\n")
    f.write("\t@echo '---------------------------------HELP--------------------------------'\n")
    f.write("\t@echo 'TO EXTRACT EIGENFREQUENCIES AND EIGENFUNCTIONS: python make_config.py'\n")
    f.write("\t@echo '-------------------------------------------------------------------'\n\n")
    f.write("clean:\n")
    f.write(f"\t@rm -rf {datadir}/snrnmais_files\n")
    f.write(f"\t@rm -rf {dldir}\n")
    # f.write(f"\t@rm -rf *.egg-info\n")
    return None


def create_dir(fulldirpath):
    if not os.path.isdir(fulldirpath):
        print(f"Creating directory {fulldirpath}")
        os.mkdir(fulldirpath)
    else:
        print(f"Directory {fulldirpath} exists")
    return None


def reporthook(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration))
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" %
                    (percent, progress_size / (1024 * 1024), speed, duration))
    sys.stdout.flush()

def urlsave(url, filename):
    urllib.request.urlretrieve(url, filename, reporthook)

def download_files():
    with open(f'{cwd}/.dl_files', 'r') as f:
        urlnames = f.read().splitlines()

    for url in urlnames:
        filename = url.split('/')[-1]
        # for dropbox downloads, filename is of the form /path/to/file/fname.ext?dl=1
        filename = filename.split('?')[0] 
        print(f"Downloading {url} to {dldir}/{filename}")
        urllib.request.urlretrieve(url, f"{dldir}/{filename}")
        urlsave(url, f"{dldir}/{filename}")
    return None


if __name__ == "__main__":
    datadir = input(f"Enter location to store the eigenfunctions and output files:" +
                    f"Default: {cwd} -- ") or f"{cwd}"
    get_scaled_efs = input(f"Do you want to use scaled (with sqt(rho)*r) eigenfunctions (y/n):")

    while(True):
        if(get_scaled_efs == 'y' or get_scaled_efs == 'Y'): 
            scale = True
            break
        elif(get_scaled_efs == 'n' or get_scaled_efs == 'N'):
            scale = False
            break
        else: continue

    dldir = f"{datadir}/dlfiles"
    snrdir = f"{datadir}/snrnmais_files"
    create_dir(datadir)
    create_dir(snrdir)
    create_dir(dldir)
    create_dir(f"{datadir}/data/w_s")
    # temporary directory to be deleted later
    # this is already created because of git cloning in the make file
    with open(f"{cwd}/.config", "w") as f:
        f.write(f"{cwd}{NL}")
        f.write(f"{datadir}{NL}")
        if(scale): f.write("scaled")
        else: f.write("unscaled")

    download_files()
    create_makefile()
    os.system("make")
