### GMIN
```
rm -rf ~/Downloads/wales/GMIN/GMIN/build/gfortran
mkdir -p ~/Downloads/wales/GMIN/GMIN/build/gfortran
cd ~/Downloads/wales/GMIN/GMIN/build/gfortran
FC=mpif90 cmake ~/Downloads/wales/GMIN/source/ -DCOMPILER_SWITCH=gfortran
make -j$(nproc)
```
