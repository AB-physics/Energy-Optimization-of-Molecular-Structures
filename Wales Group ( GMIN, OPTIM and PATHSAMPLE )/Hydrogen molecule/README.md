# Configuration for Hydrogen Molecule Optimization
After optimizing the structure of the hydrogen molecule using the Gaussian software, I proceeded to use the PELE software. However, after several days of working with PELE, the results I obtained did not match those from Gaussian, indicating an issue in the process. Ultimately, after consulting the main developers of the software, I learned that PELE is primarily designed for energy functions that are smooth and can be minimized using standard optimization techniques. The developers were unsure whether the software could be adapted for small molecules like hydrogen, which are influenced by quantum effects. They suggested that I seek guidance directly from Professor David Wales for a definitive answer.
(PELE is a partial rewrite in Python of the GMIN, OPTIM, and PATHSAMPLE programs, which were originally written in Fortran by David Wales and his collaborators at the University of Cambridge.)

Based on the guidance provided by Professor David Wales, I learned that I needed to download the Wales group software, which includes GMIN, OPTIM, PATHSAMPLE, and several other programs, from their group's website. Furthermore, I needed to link and configure the Orca software with OPTIM, as it is compatible with several electronic structure packages, to ultimately determine the optimized structure of the hydrogen molecule using this method.
## input
To perform the geometric optimization of the hydrogen molecule ``` (H₂) ``` and related calculations, I prepared four main files that work together seamlessly:
#### odata File
This file contains the initial settings for starting the optimization process and instructs the OPTIM program to use Orca for calculations. It specifies the execution path for Orca and includes settings related to the computations. For example, in this file, I defined that OPTIM should utilize Orca to compute energy and gradients, and I provided the necessary input files, including the Orca path.

Contents of this file
```
BFGSMIN 1.0D-8
CONVERGE 0.01 1.0D-8
UPDATES 100 100 5 5
MAXERISE 1.0D-5 0.02D0
MAXBFGS 0.02 0.1
BFGSSTEPS 1000

DUMPDATA
ENDNUMHESS

RADIUS 2000.0
PERMDIST
ORCA 0 1 /home/ahmad/Downloads/orca_5_0_4_linux_x86-64_shared_openmpi411/orca

POINTS
H 0.0000 0.0000 0.0000
H 0.0000 0.0000 0.7400
```
#### orca.in File
This is the main input file for Orca, where the calculation settings are specified in greater detail. For the hydrogen molecule calculations, I used the RHF (Restricted Hartree-Fock) model and the DEF2-SVP basis set. Additionally, I instructed Orca to perform ENGRAD calculations (energy and gradients) and to carry out TightSCF computations with high accuracy.

Settings in this file:
```
! RHF ENGRAD DEF2-SVP TightSCF
%elprop
Dipole False
end

*xyz 0 1
H 0.0000000000 -0.0000000010 -0.0034650345
H 0.0000000000 0.0000000010 0.7444650345
*
```
#### ORCA.template File
This file is similar to orca.in but serves as a template for Orca settings. It is prepared specifically for OPTIM to perform optimizations based on  this template. The file includes similar settings for the calculation of energy and gradients as in orca.in.

Contents of this file:
```
! RHF ENGRAD DEF2-SVP TightSCF
%elprop
Dipole False
End
```
#### sbatch.optim File
This file is prepared for running parallel computations using SLURM. It instructs SLURM on how to manage parallel processes and allocate the necessary resources. In this setup, 10 processors (each with one core) are specified for the computations.

Contents of this file:
```
#!/bin/bash
#SBATCH -p WALES
#SBATCH --time=1-0:00:0
#SBATCH -J H2_Optimization
#SBATCH -o slurm.out
#SBATCH -e slurm.err

# Number of MPI tasks
#SBATCH -n 10
#
# Number of cores per task
#SBATCH -c 1

echo $SLURM_NTASKS > nodes.info
srun hostname >> nodes.info
echo $USER >> nodes.info
pwd >> nodes.info

/path/to/OPTIM > output
```
#### Overall Functionality
These four files work together in a coordinated manner:
##### odata:
Directs OPTIM to use Orca for computations and prepares the necessary input configurations.
##### orca.in and ORCA.template:
Define the detailed computational settings in Orca, such as the calculation method, basis set, and specific tasks like energy and gradient computations.
##### sbatch.optim:
Handles the allocation of computational resources and manages parallel processing using SLURM.

Together, these files ensure that the geometric optimization calculations for the hydrogen molecule are executed accurately and efficiently.
## output
After running OPTIM and Orca, the following outputs were generated:
### a) OPTIM Files
#### converged.xyz:
Contains the final optimized coordinates of the molecule.
```
H 0.00000000000000 -0.101163601140238E-08 -0.346503447254760E-02
H 0.00000000000000 0.101163601140238E-08 0.743465034472548
```
#### min.data.info:
Contains the final optimization information, including energy and coordinates.
```
Final energy: -1.1289285686 Eh
Final coordinates:
H1: 0.000000000000000 -0.000000001011636 -0.003465034472548
H2: 0.000000000000000 0.000000001011636 0.743465034472548
points.final: Final coordinates in a more compact format.
0.00000000000000 -0.101163601140238E-08 -0.373465034472548
0.00000000000000 0.101163601140238E-08 0.373465034472548
```
### b) Orca Files
#### ORCA.out:
Contains details of the SCF calculations, energy, and molecular analyses.
```
Total SCF Energy: -1.128927852814 Eh
Molecular Coordinates in Ångstroms:
H 0.000000 -0.000000 -0.003465
H 0.000000 0.000000 0.744465
Mayer Bond Order: 1.0000 (H-H bond)
```
#### ORCA.engrad:
Contains energy and gradients.
```
Total Energy: -1.128927852814 Eh
Gradients:
0.000000000000
-0.000000000042
-0.000756769147
```
#### ORCA_property.txt:
Contains computed properties such as energy and Mayer bond order analysis.
```
SCF Energy: -1.1289278528 Eh
Bond Order between atoms: 1.0000
```
#### Final Conclusion
I successfully optimized the hydrogen molecule using OPTIM and Orca.

Key output files include:

##### converged.xyz:
Contains the final optimized coordinates.
##### min.data.info:
Provides the final energy and optimization status.
##### ORCA.out and ORCA.engrad:
Include detailed energy and gradient calculations from Orca.

These outputs help analyze the optimized geometry and the total energy of the system.

### Comparison of Gaussian and OPTIM with Orca for Hydrogen Molecule Optimization

#### Total Energy

Gaussian: The total energy calculated is -1.1268 Hartrees.

OPTIM: The total energy reported is approximately -1.1289 Hartrees.

The small discrepancy arises due to differences in numerical methods and the choice of basis sets. Gaussian uses the 6-31G(d) basis set, while  Orca employs the more accurate DEF2-SVP basis set.

#### Bond Length

Gaussian: The optimized bond length is reported as 0.7301 Å.

Orca and OPTIM: The bond length is reported as 0.7435 Å.

The difference in bond lengths is due to the choice of basis sets and convergence parameters. Gaussian tends to report shorter bond lengths, while Orca and OPTIM provide more realistic bond lengths due to the higher accuracy of the basis set.

### Final Conclusion
In summary, the results obtained from Gaussian and Orca for the hydrogen molecule are nearly identical in terms of energy, coordinates, Mulliken charges, and molecular properties. The observed differences are primarily due to slight variations in optimization methods and computational algorithms of each software. Both Gaussian and Orca provide precise results for the hydrogen molecule, which can be utilized for further analyses.
