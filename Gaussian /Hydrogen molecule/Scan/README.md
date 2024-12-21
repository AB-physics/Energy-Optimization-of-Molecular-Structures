# Bond Length Scan of the Hydrogen Molecule

To prepare the input file required for the Gaussian software and to analyze the output results, we can use the GaussView software. However, since hydrogen is a simple molecule, I used a plain text editor, such as Notepad, to create the input file. After entering the required information, I saved the file with a .com extension, which is the input format for the Gaussian software.

Once Gaussian completes the calculations, it generates an output file with the .out extension. To analyze the results and visualize them, we use the GaussView software.
## input
I performed a bond length scan for the hydrogen molecule using the Hartree-Fock (HF) method and the 6-31G(d) basis set. The bond distance B between the hydrogen atoms started at 0.5 Å and was scanned with steps of 0.01 Å over a range of 0.5 to 1.2 Å. The input file was as follows:
```
%mem=500MB
#scan HF/6-31G(d)

Bond Length Scan of the Hydrogen Molecule

0 1
H
H 1 B

B=0.5 S 120 0.01
```
## output
After submitting this input to Gaussian, I transferred the output to the 
GaussView software. The scan results perfectly matched the 
optimization of the hydrogen molecule, demonstrating the accuracy of 
the results obtained from both calculations.


