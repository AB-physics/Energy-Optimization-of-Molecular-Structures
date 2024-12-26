# Installing and Running PySCF
You can install and run PySCF using the Conda package manager or directly from the source. Below are the detailed steps for both methods:

## Steps to Install and Run PySCF Using Conda

### Create a Conda Environment
Create a new Conda environment for PySCF. Specify the Python version you want to use:
```
conda create -n pyscf python=3.9
```
This command creates a new environment named pyscf with Python 3.9.

### Activate the Conda Environment
Activate the newly created environment:
```
conda activate pyscf
```
This ensures all installations and executions occur within the pyscf environment.

### Install PySCF
Install PySCF from the Conda-Forge channel:
```
conda install pyscf -c conda-forge
```
This installs PySCF along with its dependencies.

### Install Additional Packages (Optional)
If you need additional libraries like Matplotlib for plotting or NumPy for data manipulation, install them:
```
conda install matplotlib numpy -c conda-forge
```
### Run Your Script
Execute your PySCF script (e.g., H2_scan.py) using Python:
```
python H2_scan.py
```
This runs your quantum chemistry calculations or analyses using PySCF.


