import tkinter as tk
from tkinter import messagebox

# Курси валют (hardcoded)
RATES = {
    "USD": 41.50,
    "EUR": 44.20,
    "PLN": 10.50
}

def convert_currency():
    try:
        amount = entry_amount.get()
        # ПОМИЛКА ФУНКЦІОНАЛЬНА 1: Немає перевірки на тип даних (crash при введенні літер)
        amount = float(amount) 
        
        # Отримуємо обрану валюту (але логіка вибору ігнорується)
        selected_currency = listbox_currency.get(tk.ACTIVE)
        
        # ПОМИЛКА ФУНКЦІОНАЛЬНА 2: Використовується неправильна математична формула
        # Замість множення (amount * rate) відбувається додавання
        rate = RATES["USD"] # ПОМИЛКА ФУНКЦІОНАЛЬНА 3: Завжди береться курс USD, незалежно від вибору
        result = amount + rate 
        
        label_result.config(text=f"Result: {result}")
        
    except ValueError:
        # Цей блок не спрацює коректно для користувача, бо програма просто впаде в консолі
        print("Error")

root = tk.Tk()
root.title("Best Converter 3000")
root.geometry("300x300")

# ПОМИЛКА UI/UX 1: Жахливий контраст (світло-жовтий текст на білому фоні)
root.configure(bg="white")

label_instruction = tk.Label(root, text="Enter amount in UAH:", bg="white", fg="#FFFF00") # Жовтий текст
label_instruction.pack(pady=10)

entry_amount = tk.Entry(root)
entry_amount.pack(pady=5)

label_currency = tk.Label(root, text="Select currency:", bg="white", fg="black")
label_currency.pack()

# Список валют
listbox_currency = tk.Listbox(root, height=3)
for currency in RATES:
    listbox_currency.insert(tk.END, currency)
listbox_currency.pack()

# ПОМИЛКА UI/UX 2: Кнопка має назву, яка не каже про дію ("Do it" замість "Convert")
btn_convert = tk.Button(root, text="Do it", command=convert_currency, bg="red", fg="black")
btn_convert.pack(pady=20)

# ПОМИЛКА UI/UX 3: Результат виводиться шрифтом 6px (майже нечитабельно)
label_result = tk.Label(root, text="Result: 0.00", bg="white", fg="black", font=("Arial", 6))
label_result.pack(side=tk.LEFT) # Вирівнювання зліва, хоча все інше по центру

root.mainloop()