import numpy as np
import matplotlib.pyplot as plt
from pyscf import scf
from pyscf import gto

# Bond length settings
bond_lengths = np.arange(0.5, 0.5 + 120 * 0.01, 0.01)
ehf = []
dm = None

# Calculate energies for different distances
for b in bond_lengths:
    mol = gto.M(atom=[["H", 0., 0., 0.],
                      ["H", 0., 0., b]], basis='6-31G(d)', verbose=0)
    mf = scf.RHF(mol)
    ehf.append(mf.kernel(dm))
    dm = mf.make_rdm1()

# Print results to the console
print('R     E(HF)')
for i, b in enumerate(bond_lengths):
    print(f'{b:.2f}  {ehf[i]:.8f}')

# Find optimal bond length and minimum energy
optimal_bond_length = bond_lengths[np.argmin(ehf)]
minimum_energy = min(ehf)

# Print optimal bond length and minimum energy
print(f'Optimal bond length: {optimal_bond_length:.2f} Å')
print(f'Minimum energy: {minimum_energy:.8f} Hartree')

# Plot the graph
plt.figure(figsize=(8, 6))
plt.plot(bond_lengths, ehf, marker='o', linestyle='-', label='E(HF)')
plt.title('Scan of Total Energy (HF/6-31G(d))', fontsize=14)
plt.xlabel('Bond Length (Å)', fontsize=12)
plt.ylabel('Total Energy (Hartree)', fontsize=12)
plt.grid(True)
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()