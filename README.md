# Energy-Optimization-of-Molecular-Structures
"This repository contains codes, input files, output data, and analyses related to the energy optimization of molecular structures using software such as Gaussian, Orca, PELE, and OPTIM."
## Gaussian

Gaussian is a computational chemistry software primarily used by chemists for molecular calculations, the synthesis of organic and inorganic compounds, as well as kinetics studies.

For downloading, installation, and further guidance regarding the software, please visit the official Gaussian website at ( https://gaussian.com/ ).

## Wales Group ( GMIN, OPTIM and PATHSAMPLE )

### GMIN
A program for finding global minima and calculating thermodynamic properties.

This program employs the basin-hopping algorithm described by Wales and Doye (J. Phys. Chem. A, 101, 5111, 1997) to locate global minima on a potential energy surface. Many potentials are included. The latest version also includes implementations of basin-sampling and parallel tempering, along with free energy basin-hopping, generalised basin-hopping, and grand and semi-grand canonical basin-hopping.

GMIN website ( https://www-wales.ch.cam.ac.uk/GMIN/ ) for further information.

### OPTIM
A program for optimizing geometries and calculating reaction pathways

OPTIM includes a variety of methods for locating transition states and characterising the corresponding pathways. OPTIM has analytic first and second derivatives coded for dozens of empirical potentials, and can also treat systems involving periodic boundary conditions and solve general optimization problems, such as least squares fits.

Visit the OPTIM website ( https://www-wales.ch.cam.ac.uk/OPTIM/ ) for further information.

### PATHSAMPLE
A driver for OPTIM to create stationary point databases using discrete path sampling and perform kinetic analysis.

Visit the PATHSAMPLE website ( https://www-wales.ch.cam.ac.uk/PATHSAMPLE/ ) for further information.














## PELE
pele : Python Energy Landscape Explorer.

Tools for global optimization and energy landscape exploration.

Documentation: http://pele-python.github.io/pele/

pele is a python partial-rewriting of GMIN, OPTIM, and PATHSAMPLE: fortran programs written by David Wales of Cambridge University and collaborators (http://www-wales.ch.cam.ac.uk/software.html).

The initial version of Pele was developed by Jacob Stevenson and Stefano Martiniani. ( https://github.com/pele-python/pele )

Currently, the advanced version of this software is being developed by the Martiniani research group at New York University (NYU), incorporating new advancements and features that make it suitable for more complex analyses. ( https://github.com/martiniani-lab/pele )

## ORCA

Orca is a quantum chemistry software used for calculating the electronic structure of molecules and their properties. This program includes modern quantum chemistry methods such as Density Functional Theory (DFT), Multi-Body Perturbation Theory (MP2), Coupled Cluster methods, and semi-empirical approaches. ORCA is widely utilized for studying larger molecules, transition metal complexes, and their spectroscopic properties.

Orca offers a variety of features for quantum chemical computations, including support for various density functional models (DFT) and quantum mechanical methods such as Hartree-Fock, Resolution of Identity MP2 (RI-MP2), and Time-Dependent Density Functional Theory (TDDFT). Additionally, Orca can simulate electronic spectra, molecular structures, molecular thermodynamics, and observable properties.

This software is developed by the University of Technology in Hamburg, Germany, and is used across various fields of chemistry, including computational chemistry, physical chemistry, organic chemistry, and more.

For downloading, installation, and further guidance regarding the software, please visit the official ORCA website at ( https://orcaforum.kofo.mpg.de/app.php/portal ).
