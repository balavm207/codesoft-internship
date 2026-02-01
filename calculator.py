import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("300x300")
window.resizable(False, False)

def calculate():
    a = num1.get()
    b = num2.get()
    op = choice.get()

    a = float(a)
    b = float(b)

    if op == "Add":
        ans = a + b
    elif op == "Sub":
        ans = a - b
    elif op == "Mul":
        ans = a * b
    elif op == "Div":
        if b == 0:
            result.config(text="Cannot divide by zero")
            return
        ans = a / b

    result.config(text="Result: " + str(ans))

tk.Label(window, text="Simple Calculator", font=("Arial", 14)).pack(pady=10)

num1 = tk.Entry(window)
num1.pack(pady=5)

num2 = tk.Entry(window)
num2.pack(pady=5)

choice = tk.StringVar()
choice.set("Add")

tk.OptionMenu(window, choice, "Add", "Sub", "Mul", "Div").pack(pady=10)

tk.Button(window, text="Calculate", command=calculate).pack(pady=10)

result = tk.Label(window, text="Result:")
result.pack(pady=10)

window.mainloop()
