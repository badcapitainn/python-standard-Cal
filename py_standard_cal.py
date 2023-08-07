import tkinter as tk

root = tk.Tk()
root.title("calculator")
entry = tk.Entry(root, width = 40, borderwidth = 1 )
entry.grid(row = 0, column = 0, columnspan= 5, padx= 30, pady= 20)

#creating buttons
btn_1 = tk.Button(root, text = "1", padx=30, pady=20, command=lambda: btn_click(1))
btn_2 = tk.Button(root, text = "2", padx=30, pady=20, command=lambda: btn_click(2))
btn_3 = tk.Button(root, text = "3", padx=30, pady=20, command=lambda: btn_click(3))
btn_4 = tk.Button(root, text = "4", padx=30, pady=20, command=lambda: btn_click(4))
btn_5 = tk.Button(root, text = "5", padx=30, pady=20, command=lambda: btn_click(5))
btn_6 = tk.Button(root, text = "6", padx=30, pady=20, command=lambda: btn_click(6))
btn_7 = tk.Button(root, text = "7", padx=30, pady=20, command=lambda: btn_click(7))
btn_8 = tk.Button(root, text = "8", padx=30, pady=20, command=lambda: btn_click(8))
btn_9 = tk.Button(root, text = "9", padx=30, pady=20, command=lambda: btn_click(9))
btn_0 = tk.Button(root, text = "0", padx=30, pady=20, command=lambda: btn_click(0))
btn_add = tk.Button(root, text = "+", padx=30, pady=20, command=lambda: btn_click("+"))
btn_sub = tk.Button(root, text = "-", padx=30, pady=20, command=lambda: btn_click("-"))
btn_mul = tk.Button(root, text = "x", padx=30, pady=20, command=lambda: btn_click("*"))
btn_div = tk.Button(root, text = "/", padx=30, pady=20, command=lambda: btn_click("/"))
btn_equal = tk.Button(root, text = "=", padx=30, pady=20, command=lambda: btn_equate())#calls equate function when button is clicked
btn_clear = tk.Button(root, text = "CE", padx=30, pady=20, command=lambda: btn_clr())# calls clear function when button is clicked

#buttons on first row
btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)
btn_div.grid(row=1, column=3)

#buttons on second row
btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)
btn_mul.grid(row=2, column=3)

#buttons on third row
btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)
btn_add.grid(row=3, column=3)

#buttons on fourth row
btn_clear.grid(row=4, column=0)
btn_0.grid(row=4, column=1)
btn_equal.grid(row=4, column=2)
btn_sub.grid(row=4, column=3)

def btn_click(digit):
    current = entry.get()#recieves content of entry widget
    entry.delete(0, tk.END)#deletes content in entry widget
    entry.insert(tk.END,current +str(digit))#inserts the completed expression by combining the current content with the clicked number

def btn_clr():
    entry.delete(0, tk.END)#clears the entry

def btn_equate():
    try:
        expression = entry.get()
        result = eval(expression)#uses eval function to evaluate the str expression taken from entry widget
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)#inserts completed result
    except:
        btn_clr()
        entry.insert(0, "ERROR")
        pass

root.mainloop()