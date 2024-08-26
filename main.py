import tkinter as tk
from tkinter import simpledialog, messagebox
import matplotlib.pyplot as plt
import numpy as np

# Initialize global variables
dosages = []

def add_dosage():
    """Function to add a dosage entry."""
    day = simpledialog.askinteger("Input", "Enter day of administration (1-10):")
    hour = simpledialog.askinteger("Input", "Enter hour of administration (0-23):")
    amount = simpledialog.askfloat("Input", "Enter dosage amount (mg):")
    half_life = simpledialog.askfloat("Input", "Enter half-life of the drug (hours):")
    
    if day is not None and hour is not None and amount is not None and half_life is not None:
        time = (day - 1) * 24 + hour
        dosages.append({'time': time, 'amount': amount, 'half_life': half_life})
        dosage_listbox.insert(tk.END, f"Day {day}, Hour {hour}: {amount} mg, Half-life: {half_life} hours")
        plot_concentration()

def modify_dosage():
    """Modify selected dosage."""
    selected_index = dosage_listbox.curselection()
    if not selected_index:
        messagebox.showwarning("Select Dosage", "Please select a dosage to modify.")
        return

    index = selected_index[0]
    day = simpledialog.askinteger("Input", "Enter new day of administration (1-10):")
    hour = simpledialog.askinteger("Input", "Enter new hour of administration (0-23):")
    amount = simpledialog.askfloat("Input", "Enter new dosage amount (mg):")
    half_life = simpledialog.askfloat("Input", "Enter new half-life of the drug (hours):")
    
    if day is not None and hour is not None and amount is not None and half_life is not None:
        time = (day - 1) * 24 + hour
        dosages[index] = {'time': time, 'amount': amount, 'half_life': half_life}
        dosage_listbox.delete(index)
        dosage_listbox.insert(index, f"Day {day}, Hour {hour}: {amount} mg, Half-life: {half_life} hours")
        plot_concentration()

def delete_dosage():
    """Delete selected dosage."""
    selected_index = dosage_listbox.curselection()
    if not selected_index:
        messagebox.showwarning("Select Dosage", "Please select a dosage to delete.")
        return

    index = selected_index[0]
    del dosages[index]
    dosage_listbox.delete(index)
    plot_concentration()

def calculate_concentration(times, dose_time, amount, half_life):
    """Calculate concentration at given times using exponential decay."""
    concentration = np.where(
        times >= dose_time, 
        amount * np.exp(-(times - dose_time) * np.log(2) / half_life),
        0
    )
    return concentration

def plot_concentration():
    """Plot the drug concentration over time."""
    times = np.linspace(0, 240, 240)  # 10 days in hours
    concentration = np.zeros_like(times)
    
    for dose in dosages:
        concentration += calculate_concentration(times, dose['time'], dose['amount'], dose['half_life'])
    
    plt.figure(figsize=(10, 5))
    plt.plot(times, concentration, label='Concentration (mg/L)')
    plt.xlabel('Time (hours)')
    plt.ylabel('Concentration (mg/L)')
    plt.title('Drug Concentration in Blood Over Time')
    
    # Set x-axis ticks for 24-hour intervals, with labels for each day
    plt.xticks(np.arange(0, 241, 24), [f'Day {i+1}' for i in range(11)])
    plt.grid(True)
    plt.show()


# Create the GUI window
root = tk.Tk()
root.title("Drug Concentration Monitor")

# Add buttons for adding, modifying, and deleting dosages
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_dose_button = tk.Button(button_frame, text="Add Dosage", command=add_dosage)
add_dose_button.grid(row=0, column=0, padx=5)

modify_dose_button = tk.Button(button_frame, text="Modify Dosage", command=modify_dosage)
modify_dose_button.grid(row=0, column=1, padx=5)

delete_dose_button = tk.Button(button_frame, text="Delete Dosage", command=delete_dosage)
delete_dose_button.grid(row=0, column=2, padx=5)

plot_button = tk.Button(button_frame, text="Plot Concentration", command=plot_concentration)
plot_button.grid(row=0, column=3, padx=5)

# Listbox to display current dosages
dosage_listbox = tk.Listbox(root, width=80, height=10)
dosage_listbox.pack(pady=10)

root.mainloop()
