# The equations used in the calculate_acid_density function were generated in plots.ipynb. 

import tkinter as tk
from tkinter.messagebox import showwarning, showinfo
from tkinter import ttk

# Concentrated acids database
concentrated_acids = [
    {'name': 'Nitric acid (HNO3)', 'density': 1.413, 'percentage concentration': 70, 'molar mass': 63.01},
    {'name': 'Hydrochloric acid (HCl)', 'density': 1.18, 'percentage concentration': 35, 'molar mass': 36.46},
    {'name': 'Sulfuric acid (H2SO4)', 'density': 1.83, 'percentage concentration': 95, 'molar mass': 98.08},
    {'name': 'Acetic acid', 'density': 1.04, 'percentage concentration': 100, 'molar mass': 60.05},
    {'name': 'Formic acid', 'density': 1.22, 'percentage concentration': 99, 'molar mass': 46.03},
    {'name': 'Phosphoric acid (H3PO4)', 'density': 1.685, 'percentage concentration': 99, 'molar mass': 98.00}
]

def set_default_values(event):
    dr0 = [acid['density'] for acid in concentrated_acids if acid['name'] == acid_combo.get()]  # Density of concentrated acid in g/mL
    Cp0 = [acid['percentage concentration'] for acid in concentrated_acids if acid['name'] == acid_combo.get()]  # Percentage concentration in %
    M = [acid['molar mass'] for acid in concentrated_acids if acid['name'] == acid_combo.get()]  # Molar mass in g/mol

    density_entry.delete(0, tk.END)
    density_entry.insert(0, dr0[0])

    percentage_concentration_entry.delete(0, tk.END)
    percentage_concentration_entry.insert(0, Cp0[0])

    molar_mass_entry.delete(0, tk.END)
    molar_mass_entry.insert(0, M[0])

def calculate_acid_density():  # Calculates solution density for a given percentage concentration
    Cp = float(target_concentration_entry.get())

    if acid_combo.get() == 'Sulfuric acid (H2SO4)':
        dr = -1.3271614588727825e-12*Cp**6 + 4.270769173688816e-11*Cp**5 + 2.2057312908425277e-8*Cp**4 + -1.8668929790752503e-6*Cp**3 + 7.922240303408941e-5*Cp**2 + 0.005993338497597162*Cp + 0.9995913898688527
        return float(dr)
    
    if acid_combo.get() == 'Nitric acid (HNO3)':
        dr = 6.862815816459436e-13*Cp**6 + -1.2697228396540591e-10*Cp**5 + 7.640363498330969e-9*Cp**4 + -6.567996559765774e-7*Cp**3 + 4.7712052043295685e-5*Cp**2 + 0.0050917095690252955*Cp + 0.9988275185822408
        return float(dr) 

    if acid_combo.get() == 'Hydrochloric acid (HCl)':
        dr = 0.0050322658941434366*Cp + 0.9976340980269341
        return float(dr)

    if acid_combo.get() == 'Acetic acid':
        dr = -7.504256598247657e-13*Cp**6 + 1.7907080912827385e-10*Cp**5 + -1.588921550104791e-8*Cp**4 + 6.012059313607929e-7*Cp**3 + -1.5899935228223455e-5*Cp**2 + 0.0015853152962572738*Cp + 0.9979544523112467
        return float(dr)
    
    if acid_combo.get() == 'Formic acid':
        dr = 2.0577873318333923e-13*Cp**6 + -5.226908528419914e-11*Cp**5 + 4.0987051486592555e-9*Cp**4 + -9.717523213898433e-8*Cp**3 + -2.8716862854509723e-6*Cp**2 + 0.002554645835061586*Cp + 0.9992397856913745
        return float(dr)

    if acid_combo.get() == 'Phosphoric acid (H3PO4)':
        dr = 1.6766747256395337e-12*Cp**6 + -4.936408238432713e-10*Cp**5 + 5.3070106132837436e-8*Cp**4 + -2.4626622779071613e-6*Cp**3 + 8.133555077668619e-5*Cp**2 + 0.004721605753942872*Cp + 0.9998199290379468
        return float(dr)

def calculate_required_acid_volume():
    # Main alerts
    if not acid_combo.get():
        showwarning(title='Warning!!', message='No acid selected')

    if not target_concentration_entry.get():
        showwarning(title='Warning!!', message='No target concentration provided')

    if not target_volume_entry.get():
        showwarning(title='Warning!!', message='No target volume provided')

    if var.get() == 1:  # Calculations for mol/L
        Cm = (float(percentage_concentration_entry.get()) * float(density_entry.get()) * 1000) / (float(molar_mass_entry.get()) * 100)  # Initial molar concentration in mol/L
        if float(target_concentration_entry.get()) >= Cm:  # Check if the target concentration is higher or equal to the initial concentration
            showwarning(title='Warning!!', message='Target concentration is greater or equal to the initial concentration')
            return
        else:
            n = float(target_concentration_entry.get()) * float(target_volume_entry.get())  # Calculate required moles
            ms = n * float(molar_mass_entry.get())  # Calculate required acid mass in grams
            mr = ms * 100 / float(percentage_concentration_entry.get())  # Calculate required solution mass
            V0r = mr / float(density_entry.get())  # Calculate initial concentrated solution volume in mL

            # Result for mol/L
            if V0r:
                showinfo(title='Result', message=f'To prepare a {acid_combo.get()} solution with a concentration of {target_concentration_entry.get()} mol/L and volume {target_volume_entry.get()} L, measure {round(V0r, 1)} mL of concentrated acid and dilute to {target_volume_entry.get()} L')

    if var.get() == 2:  # Calculations for %
        if float(target_concentration_entry.get()) >= float(percentage_concentration_entry.get()):  # Check if the target concentration is higher or equal to the initial concentration
            showwarning(title='Warning!!', message='Target concentration is greater or equal to the initial concentration')
            return
        else:
            mr = calculate_acid_density() * float(target_volume_entry.get()) * 1000  # Mass of acid solution at given % in g
            ms = float(target_concentration_entry.get()) * mr / 100  # Required acid mass in g
            mr = ms * 100 / float(percentage_concentration_entry.get())  # Required solution mass
            V0r = mr / float(density_entry.get())  # Initial volume in mL

            # Result for %
            if V0r:
                showinfo(title='Result', message=f'To prepare a {acid_combo.get()} solution with a concentration of {target_concentration_entry.get()} % and volume {target_volume_entry.get()} L, measure {round(V0r, 1)} mL of concentrated acid and dilute to {target_volume_entry.get()} L')

# User interface window
win = tk.Tk()
win.title('Acid Concentrations Calculator')
win.resizable(0, 0)

frm1 = tk.LabelFrame(win, text='Concentrated Acid')
frm1.grid(column=0, row=0, padx=10, pady=5)

acid_lbl = tk.Label(frm1, text='Select acid')
acid_lbl.grid(column=0, row=0, padx=3, pady=5)

acid_combo = ttk.Combobox(frm1, values=[acid['name'] for acid in concentrated_acids])
acid_combo.grid(column=1, row=0, padx=3, pady=3)
acid_combo.bind('<<ComboboxSelected>>', set_default_values)

density_lbl = tk.Label(frm1, text='Acid solution density (g/mL)')
density_lbl.grid(column=0, row=1, padx=3, pady=3)

density_entry = tk.Entry(frm1, width=10)
density_entry.grid(column=1, row=1, padx=3, pady=3)

percentage_concentration_lbl = tk.Label(frm1, text='Acid percentage concentration (%)')
percentage_concentration_lbl.grid(column=0, row=2, padx=3, pady=3)

percentage_concentration_entry = tk.Entry(frm1, width=10)
percentage_concentration_entry.grid(column=1, row=2, padx=3, pady=3)

molar_mass_lbl = tk.Label(frm1, text='Acid molar mass (g/mol)')
molar_mass_lbl.grid(column=0, row=3, padx=3, pady=3)

molar_mass_entry = tk.Entry(frm1, width=10)
molar_mass_entry.grid(column=1, row=3, padx=3, pady=3)

frm2 = tk.LabelFrame(win, text='Target Solution')
frm2.grid(column=0, row=1, padx=10, pady=5)

target_concentration_lbl = tk.Label(frm2, text='Target concentration')
target_concentration_lbl.grid(column=0, row=0, padx=3, pady=3)

target_concentration_entry = tk.Entry(frm2, width=10)
target_concentration_entry.grid(column=1, row=0, padx=3, pady=3)

var = tk.IntVar()
var.set(1)
radio1 = tk.Radiobutton(frm2, text='mol/L', variable=var, value=1)
radio1.grid(column=2, row=0, padx=3, pady=3)

radio2 = tk.Radiobutton(frm2, text='%', variable=var, value=2)
radio2.grid(column=3, row=0, padx=3, pady=3)

target_volume_lbl = tk.Label(frm2, text='Target solution volume (L)')
target_volume_lbl.grid(column=0, row=1, padx=3, pady=3)

target_volume_entry = tk.Entry(frm2, width=10)
target_volume_entry.grid(column=1, row=1, padx=3, pady=3)

button = tk.Button(win, text='Calculate', command=calculate_required_acid_volume)
button.grid(column=0, row=2, pady=5)

win.mainloop()