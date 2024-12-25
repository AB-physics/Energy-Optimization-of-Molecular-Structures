import psi4
import numpy as np
import matplotlib.pyplot as plt

# Psi4 settings
psi4.set_memory('2 GB')
psi4.core.clean_options()
psi4.core.clean()

# Bond length settings
bond_lengths = np.arange(0.5, 0.5 + 120 * 0.01, 0.01)  # Bond lengths ranging from 0.5 to 1.7 Å
energies_HF = []  # List to store the energies

# Calculate energies for different bond lengths
print(f'R(Å) |  E_HF [a.u]')
print('-----|-------------')

for bond_length in bond_lengths:
    h2 = psi4.geometry(f"""
    0 1
    symmetry c1
    H 0.0 0.0 0.0
    H 0.0 0.0 {bond_length} 
    """)  # Define the molecule for the specified bond length
    
    psi4.core.set_output_file('dissociationcurve_HF.log', True)  # Output file
    psi4.set_options({'guess_mix': False, 'guess': 'sad'})  # HF settings
    energy = psi4.energy('hf/6-31G(d)', molecule=h2)  # Compute energy

    print(f'{bond_length:.2f}  | {energy:.8f}')  # Print energy
    energies_HF.append(energy)  # Store energy

# Find optimal bond length and minimum energy
optimal_bond_length = bond_lengths[np.argmin(energies_HF)]
minimum_energy = min(energies_HF)

# Print optimal bond length and minimum energy
print(f'\nOptimal bond length: {optimal_bond_length:.2f} Å')
print(f'Minimum energy: {minimum_energy:.8f} Hartree')

# Plot the energy curve using matplotlib
plt.figure(figsize=(8, 6))
plt.plot(bond_lengths, energies_HF, label='E(HF)', linestyle='-', marker='o')
plt.axvline(optimal_bond_length, color='red', linestyle='--', label=f'Optimal Bond Length: {optimal_bond_length:.2f} Å')
plt.title('Scan of Total Energy of H2 (HF/6-31G(d))', fontsize=14)
plt.xlabel('Bond Length (Å)', fontsize=12)
plt.ylabel('Total Energy (Hartree)', fontsize=12)
plt.grid(True)
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()
