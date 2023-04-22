from tkinter import *

root = Tk()
root.title("Калькулятор")

input_field = Entry(root, width=25, font=('Arial', 14), justify="right")
input_field.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

def button_click(number):
    current = input_field.get()
    input_field.delete(0, END)
    input_field.insert(0, str(current) + str(number))

button_1 = Button(root, text="1", width=5, height=2, font=('Arial', 14), command=lambda: button_click(1))
button_1.grid(row=1, column=0, padx=5, pady=5)

button_2 = Button(root, text="2", width=5, height=2, font=('Arial', 14), command=lambda: button_click(2))
button_2.grid(row=1, column=1, padx=5, pady=5)

button_3 = Button(root, text="3", width=5, height=2, font=('Arial', 14), command=lambda: button_click(3))
button_3.grid(row=1, column=2, padx=5, pady=5)

button_divide = Button(root, text="/", width=5, height=2, font=('Arial', 14), command=lambda: button_click("/"))
button_divide.grid(row=1, column=3, padx=5, pady=5)

button_4 = Button(root, text="4", width=5, height=2, font=('Arial', 14), command=lambda: button_click(4))
button_4.grid(row=2, column=0, padx=5, pady=5)

button_5 = Button(root, text="5", width=5, height=2, font=('Arial', 14), command=lambda: button_click(5))
button_5.grid(row=2, column=1, padx=5, pady=5)

button_6 = Button(root, text="6", width=5, height=2, font=('Arial', 14), command=lambda: button_click(6))
button_6.grid(row=2, column=2, padx=5, pady=5)

button_multiply = Button(root, text="*", width=5, height=2, font=('Arial', 14), command=lambda: button_click("*"))
button_multiply.grid(row=2, column=3, padx=5, pady=5)

button_7 = Button(root, text="7", width=5, height=2, font=('Arial', 14), command=lambda: button_click(7))
button_7.grid(row=3, column=0, padx=5, pady=5)

button_8 = Button(root, text="8", width=5, height=2, font=('Arial', 14), command=lambda: button_click(8))
button_8.grid(row=3, column=1, padx=5, pady=5)

button_9 = Button(root, text="9", width=5, height=2, font=('Arial', 14), command=lambda: button_click(9))
button_9.grid(row=3, column=2, padx=5, pady=5)

button_subtract = Button(root, text="-", width=5, height=2, font=('Arial', 14), command=lambda: button_click("-"))
button_subtract.grid(row=3, column=3, padx=5, pady=5)

button_0 = Button(root, text="0", width=5, height=2, font=('Arial', 14), command=lambda: button_click(0))
button_0.grid(row=4, column=0, padx=5, pady=5)

button_decimal = Button(root, text=".", width=5, height=2, font=('Arial', 14), command=lambda: button_click("."))
button_decimal.grid(row=4, column=1, padx=5, pady=5)

button_clear = Button(root, text="C", width=5, height=2, font=('Arial', 14), command=lambda: input_field.delete(0, END))
button_clear.grid(row=4, column=2, padx=5, pady=5)

button_add = Button(root, text="+", width=5, height=2, font=('Arial', 14), command=lambda: button_click("+"))
button_add.grid(row=4, column=3, padx=5, pady=5)

button_equals = Button(root, text="=", width=12, height=2, font=('Arial', 14), command=lambda: evaluate())
button_equals.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

def evaluate():
    result = eval(input_field.get())
    input_field.delete(0, END)
    input_field.insert(0, str(result))

root.mainloop()