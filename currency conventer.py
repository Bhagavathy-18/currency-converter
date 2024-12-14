import tkinter as tk
from tkinter import ttk, messagebox

# Predefined exchange rates (for demonstration purposes)
rates = {
    "USD": 1.0,
    "EUR": 0.85,
    "GBP": 0.75,
    "INR": 74.5,
    "JPY": 110.0
    "CAD": 1.42,
    "AUD": 1.57,
    "NZD": 1.73,
    "CHF": 0.89,
    "ZAR": 17.85,
    "RUB": 104.37,
    "BGN": 1.86,
    "SGD": 1.34,
    "HKD": 7.77,
    "SEK": 10.97,
    "THB": 34.05,
    "MXN": 20.11,
    "CNY": 7.27,
    "NOK": 11.14,
    "MYR": 4.45,
    "BRL": 6.04,
    "IDR": 15990.58,
    "PHP": 58.67,
    "KRW": 1434.54,
    "ILS": 3.60,
    "ARS": 1017.50,
    "EGP": 50.81,
    "SAR": 3.75,
    "PKR": 278.00,
    "NPR": 135.72,
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
