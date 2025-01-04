###  Compiling GMIN

I used the following versions of the tools and libraries for the compilation and setup:

##### GCC 7.5.0
##### OpenMPI 4.1.2 
##### CMake 3.22.1
```
rm -rf ~/Downloads/wales/GMIN/GMIN/build/gfortran
mkdir -p ~/Downloads/wales/GMIN/GMIN/build/gfortran
cd ~/Downloads/wales/GMIN/GMIN/build/gfortran
FC=mpif90 cmake ~/Downloads/wales/GMIN/source/ -DCOMPILER_SWITCH=gfortran
make -j$(nproc)
```
Then go to the folder ``` /Downloads/wales/GMIN/GMIN/build/gfortran ``` and run the following command:
```
ccmake .
```
[ccmake screenshot](https://github.com/AB-physics/Energy-Optimization-of-Molecular-Structures/blob/main/ccmake.png)

Next, configure the settings: turn on WITH_MPI and turn off WITH_ALIGN.

