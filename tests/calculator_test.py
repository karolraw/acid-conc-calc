import sys
import os

# Make sure the root directory is in the path variable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from calculator import CalculatorModel, concentrated_acids

model = CalculatorModel()

# Calculate the initial molar concentrations 
for acid in concentrated_acids:
    name = acid['name']
    d_init = float(acid['density'])
    Cp_init = float(acid['percentage concentration'])
    M = float(acid['molar mass'])
    print(f'{name}, Cm_init = {model.calculate_initial_molar_concentration(Cp_init, d_init, M):.2f} mol/L')

## Results: ##
# Nitric acid (HNO3), Cm_init = 15.70 mol/L
# Hydrochloric acid (HCl), Cm_init = 11.33 mol/L
# Sulfuric acid (H2SO4), Cm_init = 17.73 mol/L
# Acetic acid, Cm_init = 17.32 mol/L
# Formic acid, Cm_init = 26.24 mol/L
# Phosphoric acid (H3PO4), Cm_init = 17.02 mol/L

@pytest.mark.parametrize(
        'acid_name, option, C_target, V_target, expected_V_init',
        [
            # Nitric acid (HNO3)
            # Cm_target = 5, 8, 11 mol/L, Cp_target = 15, 35, 55 %, V_target = 0.2, 0.65 L
            ('Nitric acid (HNO3)', 1, 5, 0.2, 63.7),
            ('Nitric acid (HNO3)', 1, 8, 0.2, 101.9),
            ('Nitric acid (HNO3)', 1, 11, 0.2, 140.1),
            ('Nitric acid (HNO3)', 1, 5, 0.65, 207.0),
            ('Nitric acid (HNO3)', 1, 8, 0.65, 331.3),
            ('Nitric acid (HNO3)', 1, 11, 0.65, 455.5),
            ('Nitric acid (HNO3)', 2, 15, 0.2, 32.9),
            ('Nitric acid (HNO3)', 2, 35, 0.2, 85.9),
            ('Nitric acid (HNO3)', 2, 55, 0.2, 148.9),
            ('Nitric acid (HNO3)', 2, 15, 0.65, 106.9),
            ('Nitric acid (HNO3)', 2, 35, 0.65, 279.1),
            ('Nitric acid (HNO3)', 2, 55, 0.65, 483.9),

            # Hydrochloric acid (HCl)
            # Cm_target = 2, 4, 6 mol/L, Cp_target = 5, 15, 25 %, V_target = 0.2, 0.65 L
            ('Hydrochloric acid (HCl)', 1, 2, 0.2, 35.3),
            ('Hydrochloric acid (HCl)', 1, 4, 0.2, 70.6),
            ('Hydrochloric acid (HCl)', 1, 6, 0.2, 105.9),
            ('Hydrochloric acid (HCl)', 1, 2, 0.65, 114.8),
            ('Hydrochloric acid (HCl)', 1, 4, 0.65, 229.5),
            ('Hydrochloric acid (HCl)', 1, 6, 0.65, 344.3),
            ('Hydrochloric acid (HCl)', 2, 5, 0.2, 24.8),
            ('Hydrochloric acid (HCl)', 2, 15, 0.2, 78.0),
            ('Hydrochloric acid (HCl)', 2, 25, 0.2, 136.0),
            ('Hydrochloric acid (HCl)', 2, 5, 0.65, 80.5),
            ('Hydrochloric acid (HCl)', 2, 15, 0.65, 253.3),
            ('Hydrochloric acid (HCl)', 2, 25, 0.65, 442.0), 

            # Sulfuric acid (H2SO4)
            # Cm_target = 5, 10, 15 mol/L, Cp_target = 15, 45, 60 %, V_target = 0.2, 0.65 L
            ('Sulfuric acid (H2SO4)', 1, 5, 0.2, 56.4),
            ('Sulfuric acid (H2SO4)', 1, 10, 0.2, 112.8),
            ('Sulfuric acid (H2SO4)', 1, 15, 0.2, 169.2),
            ('Sulfuric acid (H2SO4)', 1, 5, 0.65, 183.4),
            ('Sulfuric acid (H2SO4)', 1, 10, 0.65, 366.7),
            ('Sulfuric acid (H2SO4)', 1, 15, 0.65, 550.1),
            ('Sulfuric acid (H2SO4)', 2, 15, 0.2, 19.0),
            ('Sulfuric acid (H2SO4)', 2, 45, 0.2, 69.7),
            ('Sulfuric acid (H2SO4)', 2, 60, 0.2, 103.4),
            ('Sulfuric acid (H2SO4)', 2, 15, 0.65, 61.8),
            ('Sulfuric acid (H2SO4)', 2, 45, 0.65, 226.6),
            ('Sulfuric acid (H2SO4)', 2, 60, 0.65, 336.1), 

            # Acetic acid
            # Cm_target = 5, 10, 15 mol/L, Cp_target = 15, 45, 60 %, V_target = 0.2, 0.65 L
            ('Acetic acid', 1, 5, 0.2, 57.7),
            ('Acetic acid', 1, 10, 0.2, 115.5),
            ('Acetic acid', 1, 15, 0.2, 173.2),
            ('Acetic acid', 1, 5, 0.65, 187.7),
            ('Acetic acid', 1, 10, 0.65, 375.3),
            ('Acetic acid', 1, 15, 0.65, 563.0),
            ('Acetic acid', 2, 15, 0.2, 29.4),
            ('Acetic acid', 2, 45, 0.2, 91.2),
            ('Acetic acid', 2, 60, 0.2, 122.8),
            ('Acetic acid', 2, 15, 0.65, 95.6),
            ('Acetic acid', 2, 45, 0.65, 296.3),
            ('Acetic acid', 2, 60, 0.65, 399.0),

            # Formic acid
            # Cm_target = 10, 15, 20 mol/L, Cp_target = 15, 45, 60 %, V_target = 0.2, 0.65 L
            ('Formic acid', 1, 10, 0.2, 76.2),
            ('Formic acid', 1, 15, 0.2, 114.3),
            ('Formic acid', 1, 20, 0.2, 152.4),
            ('Formic acid', 1, 10, 0.65, 247.7),
            ('Formic acid', 1, 15, 0.65, 371.6),
            ('Formic acid', 1, 20, 0.65, 495.4),
            ('Formic acid', 2, 15, 0.2, 25.8),
            ('Formic acid', 2, 45, 0.2, 82.6),
            ('Formic acid', 2, 60, 0.2, 113.6),
            ('Formic acid', 2, 15, 0.65, 83.7),
            ('Formic acid', 2, 45, 0.65, 268.4),
            ('Formic acid', 2, 60, 0.65, 369.2),

            # Phosphoric acid (H3PO4)
            # Cm_target = 5, 10, 15 mol/L, Cp_target = 15, 45, 60 %, V_target = 0.2, 0.65 L
            ('Phosphoric acid (H3PO4)', 1, 5, 0.2, 58.7),
            ('Phosphoric acid (H3PO4)', 1, 10, 0.2, 117.5),
            ('Phosphoric acid (H3PO4)', 1, 15, 0.2, 176.2),
            ('Phosphoric acid (H3PO4)', 1, 5, 0.65, 190.9),
            ('Phosphoric acid (H3PO4)', 1, 10, 0.65, 381.9),
            ('Phosphoric acid (H3PO4)', 1, 15, 0.65, 572.8),
            ('Phosphoric acid (H3PO4)', 2, 15, 0.2, 19.5),
            ('Phosphoric acid (H3PO4)', 2, 45, 0.2, 69.8),
            ('Phosphoric acid (H3PO4)', 2, 60, 0.2, 102.6),
            ('Phosphoric acid (H3PO4)', 2, 15, 0.65, 63.3),
            ('Phosphoric acid (H3PO4)', 2, 45, 0.65, 226.7),
            ('Phosphoric acid (H3PO4)', 2, 60, 0.65, 333.4), 
        ],
)
def test_calculator(acid_name, option, C_target, V_target, expected_V_init):
    """Verifies the output volumes for different input parameters declared using pytest.mark.parametrize."""
    
    # Load initial values
    d_init = [acid['density'] for acid in concentrated_acids if acid['name'] == acid_name][0]  # Density of concentrated acid in g/mL
    Cp_init = [acid['percentage concentration'] for acid in concentrated_acids if acid['name'] == acid_name][0]  # Percentage concentration in %
    M = [acid['molar mass'] for acid in concentrated_acids if acid['name'] == acid_name][0]  # Molar mass in g/mol

    # Convert data variables to floats
    d_init = float(d_init)
    Cp_init = float(Cp_init)
    M = float(M)
    C_target = float(C_target)
    V_target = float(V_target)

    # Calculate values
    if option == 1:  # Calculations for mol/L
        V_init = model.calculate_concentrated_acid_volume_from_molar_concentration(C_target, V_target, M, Cp_init, d_init)

    elif option == 2: # Calculations for % 
        d_target = model.calculate_acid_density(acid_name, C_target)
        V_init = model.calculate_concentrated_acid_volume_from_percentage_concentration(C_target, d_target, V_target, Cp_init, d_init)
    
    # Verify the output
    assert round(V_init,1) == expected_V_init