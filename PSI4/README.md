# Steps to Install and Run Psi4 Using Conda

## Create a Conda Environment:

First, create a new Conda environment for Psi4. Specify the Python version you want to use:

‍``` conda create -n psi4 python=3.12 ```

This command creates a new environment named psi4 with Python 3.12.

## Activate the Conda Environment:

Activate the newly created environment:
```
conda activate psi4
```
This ensures all installations and executions occur within the psi4 environment.

## Install Psi4:

Install Psi4 from the Conda-Forge channel:
```
conda install psi4 -c conda-forge
```
This installs Psi4 along with its dependencies.

## Install Matplotlib (Optional):

If your project requires plotting capabilities, install Matplotlib:
```
conda install matplotlib -c conda-forge
```
This is useful for visualizing data, such as potential energy scans or molecular properties.

## Run Your Script:

Execute your Psi4 script (e.g., H2_scan.py) using Python:
```
python H2_scan.py
```
This runs your quantum chemistry calculations or analyses using Psi4.
