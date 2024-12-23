# Calculating the Geometric Optimization of the Hydrogen Molecule
To prepare the input file required for the Gaussian software and to analyze the output results, we can use the GaussView software. However, since hydrogen is a simple molecule, I used a plain text editor, such as Notepad, to create the input file. After entering the required information, I saved the file with a .com extension, which is the input format for the Gaussian software.

Once Gaussian completes the calculations, it generates an output file with the .out extension. To analyze the results and visualize them, we use the GaussView software.

## input
For the geometric optimization of the hydrogen molecule, I used the Hartree-Fock (HF) method with the 6-31G(d) basis set. I allocated 500 megabytes of memory for the calculations and optimized the hydrogen molecule's geometry using the opt command. The input file was as follows:
```
%mem=500MB
#opt HF/6-31G(d)

Optimization of the hydrogen molecule

0 1
H
H 1 B

B=0.7
```
## output
After submitting this input to Gaussian software, the output was 
received as a file with a .out extension. Interpretation of the output 
indicates that the total energy of the system after optimization is 
``` E(RHF)=−1.12682781103 Hartrees ```, and the optimized geometry 
corresponds to a bond length of ``` 0.7301 Å ``` between the two hydrogen 
atoms.

