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

class CalculatorModel:
    def __init__(self):
        pass

    def calculate_initial_molar_concentration(self, Cp_init: float, d_init: float, M: float) -> float:
        """
        Calculates the molar concentration based on the initial percentage concentration (Cp_init) and density (d_init), and molar mass (M) of the concentrated acid.

        Parameters
        ----------
        Cp_init : float
            The initial percentage concentraion of the concetrated acid (%).
        d_init : float
            The initial density of the concentrated acid (g/mL).
        M : float
            The molar mass of the acid (g/mol).

        Returns
        -------
        Cm_init : float
            The initial molar concentration of the concentrated acid (mol/L).
        """
        Cm_init = (Cp_init*d_init*1000)/(M*100)

        return Cm_init

    def calculate_concentrated_acid_volume_from_molar_concentration(self, Cm_target: float, V_target: float, M: float, Cp_init: float, d_init: float) -> float:
        """
        Calculates the required volume of the concentrated acid that needs to be measured to obtain the target concentration solution.

        Parameters
        ----------
        Cm_target : float
            The specified molar concentration of the target solution (mol/L).
        V_target : float
            The specified volume of the target solution (L).
        M : float
            The molar mass of the acid (g/mol).
        Cp_init : float
            The initial percentage concentraion of the concetrated acid (%).
        d_init : float
            The initial density of the concentrated acid (g/mL).

        Returns
        -------
        V_init : float
        The initial volume of the concentrated acid (mL).
        """
        V_init = (Cm_target*V_target*M*100)/(Cp_init*d_init)

        return V_init

    def calculate_acid_density(self, acid_name: str, Cp_target: float) -> float:
        """ 
        Calculates solution density for a given percentage concentration.
        
        Parameters
        ----------

        acid_name : str
            The name of the acid from the following list:
            'Sulfuric acid (H2SO4)',
            'Nitric acid (HNO3)',
            'Hydrochloric acid (HCl)',
            'Acetic acid',
            'Formic acid',
            'Phosphoric acid (H3PO4)'.
        Cp_target : float
            The specified percentage concentration of the target solution (%).

        Returns
        -------
        
        d_target : float
            The density of the target solution (g/mL).    
        """  

        density_equations = {
            'Sulfuric acid (H2SO4)': lambda Cp_target: -1.3271614588727825e-12*Cp_target**6 + 4.270769173688816e-11*Cp_target**5 + 2.2057312908425277e-8*Cp_target**4 + -1.8668929790752503e-6*Cp_target**3 + 7.922240303408941e-5*Cp_target**2 + 0.005993338497597162*Cp_target + 0.9995913898688527,
            'Nitric acid (HNO3)' : lambda Cp_target: 6.862815816459436e-13*Cp_target**6 + -1.2697228396540591e-10*Cp_target**5 + 7.640363498330969e-9*Cp_target**4 + -6.567996559765774e-7*Cp_target**3 + 4.7712052043295685e-5*Cp_target**2 + 0.0050917095690252955*Cp_target + 0.9988275185822408,
            'Hydrochloric acid (HCl)' : lambda Cp_target: 0.0050322658941434366*Cp_target + 0.9976340980269341,
            'Acetic acid' : lambda Cp_target: -7.504256598247657e-13*Cp_target**6 + 1.7907080912827385e-10*Cp_target**5 + -1.588921550104791e-8*Cp_target**4 + 6.012059313607929e-7*Cp_target**3 + -1.5899935228223455e-5*Cp_target**2 + 0.0015853152962572738*Cp_target + 0.9979544523112467,
            'Formic acid' : lambda Cp_target: 2.0577873318333923e-13*Cp_target**6 + -5.226908528419914e-11*Cp_target**5 + 4.0987051486592555e-9*Cp_target**4 + -9.717523213898433e-8*Cp_target**3 + -2.8716862854509723e-6*Cp_target**2 + 0.002554645835061586*Cp_target + 0.9992397856913745,
            'Phosphoric acid (H3PO4)' : lambda Cp_target: 1.6766747256395337e-12*Cp_target**6 + -4.936408238432713e-10*Cp_target**5 + 5.3070106132837436e-8*Cp_target**4 + -2.4626622779071613e-6*Cp_target**3 + 8.133555077668619e-5*Cp_target**2 + 0.004721605753942872*Cp_target + 0.9998199290379468
        }

        d_target = density_equations[acid_name](Cp_target)
        
        return d_target

    def calculate_concentrated_acid_volume_from_percentage_concentration(self, Cp_target: float, d_target: float, V_target: float, Cp_init: float, d_init: float) -> float:
        """
        Calculates the required volume of the concentrated acid that needs to be measured to obtain the target concentration solution.

        Parameters
        ----------
        Cp_target : float
            The specified percentage concentration of the target solution (%).
        d_target : float
            The density of the target solution (g/mL).  
        V_target : float
            The specified volume of the target solution (L).
        Cp_init : float
            The initial percentage concentraion of the concetrated acid (%).
        d_init : float
            The initial density of the concentrated acid (g/mL).

        Returns
        -------
        V_init : float
        The initial volume of the concentrated acid (mL).
        """

        V_init = (Cp_target*d_target*V_target*1000)/(Cp_init*d_init)
        
        return V_init

class ConcentratedAcidFrame(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text='Concentrated Acid')

        # Create widgets
        self.acid_lbl = tk.Label(self, text='Select acid')
        self.acid_lbl.grid(column=0, row=0, padx=3, pady=5)

        self.acid_combo = ttk.Combobox(self, values=[acid['name'] for acid in concentrated_acids])
        self.acid_combo.grid(column=1, row=0, padx=3, pady=3)
        self.acid_combo.bind('<<ComboboxSelected>>', self.set_default_values)

        self.density_lbl = tk.Label(self, text='Acid solution density (g/mL)')
        self.density_lbl.grid(column=0, row=1, padx=3, pady=3)

        self.density_entry = tk.Entry(self, width=10)
        self.density_entry.grid(column=1, row=1, padx=3, pady=3)

        self.percentage_concentration_lbl = tk.Label(self, text='Acid percentage concentration (%)')
        self.percentage_concentration_lbl.grid(column=0, row=2, padx=3, pady=3)

        self.percentage_concentration_entry = tk.Entry(self, width=10)
        self.percentage_concentration_entry.grid(column=1, row=2, padx=3, pady=3)

        self.molar_mass_lbl = tk.Label(self, text='Acid molar mass (g/mol)')
        self.molar_mass_lbl.grid(column=0, row=3, padx=3, pady=3)

        self.molar_mass_entry = tk.Entry(self, width=10)
        self.molar_mass_entry.grid(column=1, row=3, padx=3, pady=3)

        # Set a controller
        self.controller = None

    def set_controller(self, controller):
        """
        Sets the controller for this widget.

        Parameters
        ----------
        controller : object
            The controller instance managing this widget.
        """

        self.controller = controller

    def set_default_values(self, event):
        """
        Updates the entry fields with default values based on the selected acid.

        Parameters
        ----------
        event : Event
            The selection of the dropdown.
        """

        d_init = [acid['density'] for acid in concentrated_acids if acid['name'] == self.acid_combo.get()]  # Density of concentrated acid in g/mL
        cp_init = [acid['percentage concentration'] for acid in concentrated_acids if acid['name'] == self.acid_combo.get()]  # Percentage concentration in %
        M = [acid['molar mass'] for acid in concentrated_acids if acid['name'] == self.acid_combo.get()]  # Molar mass in g/mol

        self.density_entry.delete(0, tk.END)
        self.density_entry.insert(0, d_init[0])

        self.percentage_concentration_entry.delete(0, tk.END)
        self.percentage_concentration_entry.insert(0, cp_init[0])

        self.molar_mass_entry.delete(0, tk.END)
        self.molar_mass_entry.insert(0, M[0])

    def no_acid_selected_alert(self):
        """
        Displays a warning if no acid is selected.

        Raises
        ------
        tkinter.messagebox.showwarning
            A warning dialog if no acid is selected from the dropdown.
        """
        
        if not self.acid_combo.get():
            showwarning(title='Warning!!', message='No acid selected!')

class TargetSolutionFrame(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text='Target Solution')

        # Create widgets
        self.target_concentration_lbl = tk.Label(self, text='Target concentration')
        self.target_concentration_lbl.grid(column=0, row=0, padx=3, pady=3)

        self.target_concentration_entry = tk.Entry(self, width=10)
        self.target_concentration_entry.grid(column=1, row=0, padx=3, pady=3)

        self.radio_var = tk.IntVar()
        self.radio_var.set(1)

        self.radio1 = tk.Radiobutton(self, text='mol/L', variable=self.radio_var, value=1)
        self.radio1.grid(column=2, row=0, padx=3, pady=3)

        self.radio2 = tk.Radiobutton(self, text='%', variable=self.radio_var, value=2)
        self.radio2.grid(column=3, row=0, padx=3, pady=3)

        self.target_volume_lbl = tk.Label(self, text='Target solution volume (L)')
        self.target_volume_lbl.grid(column=0, row=1, padx=3, pady=3)

        self.target_volume_entry = tk.Entry(self, width=10)
        self.target_volume_entry.grid(column=1, row=1, padx=3, pady=3)

        # Set a controller
        self.controller = None

    def set_controller(self, controller):
        """
        Sets the controller for this widget.

        Parameters
        ----------
        controller : object
            The controller instance managing this widget.
        """

        self.controller = controller

    def no_target_concentration_alert(self):
        """
        Displays a warning if no target concentration is entered.

        Raises
        ------
        tkinter.messagebox.showwarning
            A warning dialog if no target concentration is entered.
        """
          
        if not self.target_concentration_entry.get():
            showwarning(title='Warning!!', message='No target concentration provided!')
    
    def no_target_volume_alert(self):
        """
        Displays a warning if no target volume is entered.

        Raises
        ------
        tkinter.messagebox.showwarning
            A warning dialog if no target volume is entered.
        """

        if not self.target_volume_entry.get():
            showwarning(title='Warning!!', message='No target volume provided!')

class CalculateButton(tk.Button):
    def __init__(self, parent):
        super().__init__(parent, text='Calculate', command=self.calculate_button_clicked)

        # Set a controller
        self.controller = None

    def set_controller(self, controller):
        """
        Sets the controller for this widget.

        Parameters
        ----------
        controller : object
            The controller instance managing this widget.
        """

        self.controller = controller

    def calculate_button_clicked(self):
        """
        Triggers the calculate action in the controller.

        This method calls the `calculate_button_clicked` method of the 
        associated controller, delegating the calculation logic.
        """
        if self.controller:
            self.controller.calculate_button_clicked()

class CalculatorController:
    def __init__(self, model, frm1, frm2, button):
        # Create variables for the App class
        self.model = model
        self.frm1 = frm1
        self.frm2 = frm2
        self.button = button
    
    def calculate_button_clicked(self):
        """
        Handles the calculation process for preparing an acid solution.

        This method:
        - Checks if required inputs are provided via alert messages.
        - Retrieves user inputs from UI elements.
        - Converts necessary values to floats.
        - Performs concentration and dilution calculations based on user selection.
        - Displays a warning if the target concentration is too high.
        - Shows a message box with the calculated volume of concentrated acid needed.
        """

        # Alerts
        self.frm1.no_acid_selected_alert()
        self.frm2.no_target_concentration_alert()
        self.frm2.no_target_volume_alert()

        # Import variables
        acid_name = self.frm1.acid_combo.get() # Get the acid name from the combobox
        d_init = self.frm1.density_entry.get()
        Cp_init = self.frm1.percentage_concentration_entry.get()
        M = self.frm1.molar_mass_entry.get()

        C_target = self.frm2.target_concentration_entry.get() # Either mol/L or %
        option = self.frm2.radio_var.get() # Get the option from the radiobutton
        V_target = self.frm2.target_volume_entry.get()

        # Convert data variables to floats
        d_init = float(d_init)
        Cp_init = float(Cp_init)
        M = float(M)

        C_target = float(C_target)
        V_target = float(V_target)
        
        # Calculate values
        Cm_init = self.model.calculate_initial_molar_concentration(Cp_init, d_init, M)
        
        if option == 1:  # Calculations for mol/L
            if C_target >= Cm_init:
                showwarning(title='Warning!!', message='Target concentration is greater or equal to the initial concentration!')
            else:
                V_init = self.model.calculate_concentrated_acid_volume_from_molar_concentration(C_target, V_target, M, Cp_init, d_init)
                if V_init:
                    showinfo(title='Result', message=f'To prepare a {acid_name} solution with a concentration of {C_target} mol/L and volume {V_target} L, measure {round(V_init, 1)} mL of concentrated acid and dilute to {V_target} L.')
                
        elif option == 2: # Calculations for % 
            if C_target >= Cp_init:
                showwarning(title='Warning!!', message='Target concentration is greater or equal to the initial concentration!')
            else:
                d_target = self.model.calculate_acid_density(acid_name, C_target)
                V_init = self.model.calculate_concentrated_acid_volume_from_percentage_concentration(C_target, d_target, V_target, Cp_init, d_init)
                if V_init:
                    showinfo(title='Result', message=f'To prepare a {acid_name} solution with a concentration of {C_target} % and volume {V_target} L, measure {round(V_init, 1)} mL of concentrated acid and dilute to {V_target} L.')

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window settings
        self.title('Acid Concentrations Calculator')
        self.resizable(0, 0)

        # Create a model
        model = CalculatorModel()

        # Create frames and button
        frm1 = ConcentratedAcidFrame(self)
        frm1.grid(column=0, row=0, padx=10, pady=5)

        frm2 = TargetSolutionFrame(self)
        frm2.grid(column=0, row=1, padx=10, pady=5)

        button = CalculateButton(self)
        button.grid(column=0, row=2, pady=5)

        # Create a controller
        controller = CalculatorController(model, frm1, frm2, button)

        # Set the controller to frm1, frm2 and button
        frm1.set_controller(controller)
        frm2.set_controller(controller)
        button.set_controller(controller)

if __name__ == '__main__':
    # Run the application
    App = CalculatorApp()
    App.mainloop()