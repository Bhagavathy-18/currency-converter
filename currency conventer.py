import tkinter as tk
from tkinter import ttk, messagebox

# Predefined exchange rates (for demonstration purposes)
rates = {
    "USD": 1.0,
    "EUR": 0.85,
    "GBP": 0.75,
    "INR": 74.5,
    "JPY": 110.0
}

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_combobox.get()
        to_currency = to_currency_combobox.get()

        if from_currency not in rates or to_currency not in rates:
            messagebox.showerror("Error", "Please select valid currencies.")
            return

        converted_amount = amount * (rates[to_currency] / rates[from_currency])
        result_label.config(text=f"Converted Amount: {converted_amount:.2f} {to_currency}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
# Create the main window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")

# Labels and Entry fields
amount_label = tk.Label(root, text="Amount:")
amount_label.pack(pady=5)
amount_entry = tk.Entry(root)
amount_entry.pack(pady=5)

from_currency_label = tk.Label(root, text="From Currency:")
from_currency_label.pack(pady=5)
from_currency_combobox = ttk.Combobox(root, values=list(rates.keys()))
from_currency_combobox.pack(pady=5)

to_currency_label = tk.Label(root, text="To Currency:")
to_currency_label.pack(pady=5)
to_currency_combobox = ttk.Combobox(root, values=list(rates.keys()))
to_currency_combobox.pack(pady=5)

convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.pack(pady=10)

result_label = tk.Label(root, text="Converted Amount: ")
result_label.pack(pady=20)

# Run the application
root.mainloop()
