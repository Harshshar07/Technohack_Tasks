import tkinter as tk

exprsn = ""

def select(symbol):
    global exprsn
    exprsn += str(symbol)
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, exprsn)
    
def evaluate():
    global exprsn

    try:

        result = str(eval(exprsn))

        text_box.delete(1.0, tk.END)

        text_box.insert(tk.END, result)
        exprsn = str(result)

    except:

        text_box.delete(1.0, tk.END)

        text_box.insert(tk.END, "ERROR")
        exprsn = ""

def clear():
    global exprsn

    text_box.delete(1.0, tk.END)
    exprsn = ""


window = tk.Tk()

window.geometry("650x750")

window.title("CalC")


text_box = tk.Text(window, height=5, font=("Century", 14), width=3)

text_box.grid(columnspan=5, padx=15, pady=15, sticky="nsew")


button1 = tk.Button(window, text="1", font=("Century", 14), command=lambda: select(1), bg="Grey", width=10, height=3)

button1.grid(column=1, row=2, padx=5, pady=5)


button2 = tk.Button(window, text="2", font=("Century", 14), command=lambda: select(2),  bg="Grey" ,width=10, height=3)

button2.grid(column=2, row=2, padx=5, pady=5)


button3 = tk.Button(window, text="3", font=("Century", 14), command=lambda: select(3), bg="Grey" ,width=10, height=3)

button3.grid(column=3, row=2, padx=5, pady=5)


button4 = tk.Button(window, text="4", font=("Century", 14), command=lambda: select(4), bg="Grey" ,width=10, height=3)

button4.grid(column=1, row=3, padx=5, pady=5)


button5 = tk.Button(window, text="5", font=("Century", 14), command=lambda: select(5), bg="Grey" ,width=10, height=3)

button5.grid(column=2, row=3, padx=5, pady=5)


button6 = tk.Button(window, text="6", font=("Century", 14), command=lambda: select(6), bg="Grey" ,width=10, height=3)

button6.grid(column=3, row=3, padx=5, pady=5)


button7 = tk.Button(window, text="7", font=("Century", 14), command=lambda: select(7), bg="Grey" ,width=10, height=3)

button7.grid(column=1, row=4, padx=5, pady=5)


button8 = tk.Button(window, text="8", font=("Century", 14), command=lambda: select(8), bg="Grey" ,width=10, height=3)

button8.grid(column=2, row=4, padx=5, pady=5)


button9 = tk.Button(window, text="9", font=("Century", 14), command=lambda: select(9), bg="Grey" ,width=10, height=3)

button9.grid(column=3, row=4, padx=5, pady=5)


button0 = tk.Button(window, text="0", font=("Century", 14), command=lambda: select(0), bg="Grey" ,width=10, height=3)

button0.grid(column=2, row=5, padx=5, pady=5)


button_plus = tk.Button(window, text="+", font=("Century", 14), command=lambda: select("+"), width=10, height=3)

button_plus.grid(column=4, row=2, padx=5, pady=5)


button_minus = tk.Button(window, text="-", font=("Century", 14), command=lambda:  select("-"), width=10, height=3)

button_minus.grid(column=4, row=3, padx=5, pady=5)


button_mul = tk.Button(window, text="*", font=("Century", 14), command=lambda: select("*"), width=10, height=3)

button_mul.grid(column=4, row=4, padx=5, pady=5)


button_div = tk.Button(window, text="/", font=("Century", 14), command=lambda: select("/"), width=10, height=3)

button_div.grid(column=4, row=5, padx=5, pady=5)


button_rbr = tk.Button(window, text=")", font=("Century", 14), command=lambda: select(")"),bg="Grey", width=10, height=3)

button_rbr.grid(column=3, row=5, padx=5, pady=5)


button_rbl = tk.Button(window, text="(", font=("Century", 14), command=lambda: select("("), bg="Grey" ,width=10, height=3)

button_rbl.grid(column=1, row=5, padx=5, pady=5)


button_equ = tk.Button(window, text="Equal To", font=("Century", 14), command=evaluate, bg='Grey', width=51, height=3)

button_equ.grid(column=1, row=6, columnspan=5, padx=10, pady=10, sticky="nsew")


button_clear = tk.Button(window, text="Cancel", font=("Century", 14), command=clear, width=51, height=3)

button_clear.grid(column=1, row=7, columnspan=5, padx=10, pady=10, sticky="nsew")


window.grid_rowconfigure(0, weight=1)

window.grid_columnconfigure(0, weight=1)

window.mainloop()