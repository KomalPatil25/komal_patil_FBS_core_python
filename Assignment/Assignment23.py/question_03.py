from tkinter import *
from tkinter import messagebox

def click(value):
    entry.insert(END, value)
    
def main():
    entry = Entry(window)
    entry.grid(row=0, column=0, columnspan=4)


def clear():
    entry.delete(0, END)

def evaluate():
    try:
        result = eval(super.entry.get())
        global entry
        entry.delete(0, END)
        entry.insert(END, result)
    except:
        entry.delete(0, END)
        entry.insert(END, 'Error')

buttons = ['7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    '0', 'C', '=', '/'
    ]

row, col = 1, 0
for btn in buttons:
    Button(Entry, text=btn, width=5, command=lambda b = btn:
               clear() if b == 'C' else evaluate() if b == '=' else click(b)).grid(row = row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1
if __name__ == '__main__':  
    window = Tk()
    window.title('Calculator')
    window.geometry('300x400')
    window.config(bg='pink')

    main()
    window.mainloop()