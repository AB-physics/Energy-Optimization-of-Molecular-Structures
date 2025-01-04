###  Compiling GMIN
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
![Description of Image](path/to/image.png)

Next, configure the settings: turn on WITH_MPI and turn off WITH_ALIGN.

