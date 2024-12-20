# Energy-Optimization-of-Molecular-Structures
"This repository contains codes, input files, output data, and analyses related to the energy optimization of molecular structures using software such as Gaussian, Orca, PELE, and OPTIM."
## Gaussian 

## Wales Group ( GMIN, OPTIM and PATHSAMPLE )

### GMIN
A program for finding global minima and calculating thermodynamic properties.

This program employs the basin-hopping algorithm described by Wales and Doye (J. Phys. Chem. A, 101, 5111, 1997) to locate global minima on a potential energy surface. Many potentials are included. The latest version also includes implementations of basin-sampling and parallel tempering, along with free energy basin-hopping, generalised basin-hopping, and grand and semi-grand canonical basin-hopping. GMIN website for further information.

### OPTIM
A program for optimizing geometries and calculating reaction pathways

OPTIM includes a variety of methods for locating transition states and characterising the corresponding pathways. OPTIM has analytic first and second derivatives coded for dozens of empirical potentials, and can also treat systems involving periodic boundary conditions and solve general optimization problems, such as least squares fits. Visit the OPTIM website for further information.

### PATHSAMPLE
A driver for OPTIM to create stationary point databases using discrete path sampling and perform kinetic analysis

Visit the PATHSAMPLE website for further information.














## PELE
pele : Python Energy Landscape Explorer.

Tools for global optimization and energy landscape exploration.

Documentation: http://pele-python.github.io/pele/

pele is a python partial-rewriting of GMIN, OPTIM, and PATHSAMPLE: fortran programs written by David Wales of Cambridge University and collaborators (http://www-wales.ch.cam.ac.uk/software.html).

The initial version of Pele was developed by Jacob Stevenson and Stefano Martiniani. ( https://github.com/pele-python/pele )

Currently, the advanced version of this software is being developed by the Martiniani research group at New York University (NYU), incorporating new advancements and features that make it suitable for more complex analyses. ( https://github.com/martiniani-lab/pele )

## Orca
