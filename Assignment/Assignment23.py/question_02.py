from tkinter import *
from tkinter import ttk, messagebox

RATES = {
    'USD' : 1.0,
    'INR' : 83.20,
    'EUR' : 0.94,
    'GBP' : 0.79,
    'JPY' : 156.9,
    'AUD' : 1.53,
    'CAD' : 1.38,
    'CNY' : 7.23,
}
def convert_currency():
    try:
        amount = float(amt_entry.get())
        from_curr = from_currency.get()
        to_curr = to_currency.get()

        if from_curr == '' or to_curr == '':
            messagebox.showwarning('Warning', 'Please select both currencies!')
            return
        
        usd_amt = amount / RATES[from_curr]
        converted = usd_amt * RATES[to_curr]

        result_label.config(text=f'{amount: .2f}{from_curr} = {converted: .2f}{to_curr}')
    except ValueError:
        messagebox.showerror('ERROR', 'Please enter a valid number!')

if __name__ == '__main__':
    window = Tk()
    window.title('Currency Converted')
    window.config(background='pink')
    window.geometry('300x400')

    title = Label(window, text='Currency Converter', font=('Arial',16,'bold'), bg='#2196f3', pady=10)
    title.pack()

    frame = Frame(window, bg='#e3f2fd')
    frame.pack(pady=20)

    Label(frame, text='Enter Amount: ', font=('Arial', 12), bg='#e3f2fd').grid(row=0, column=0, padx=5, pady=5)
    # Label.grid(row=0, column=1, pady=10)
    amt_entry = Entry(frame, font=('Arial', 12))
    amt_entry.grid(row=0, column=1, pady=5)

    Label(frame, text='From:', font=('Arial', 12), bg='#e3f2fd').grid(row=1, column=0, pady=5)
    from_currency = ttk.Combobox(frame, values=list(RATES.keys()), font=('Arial', 11))
    from_currency.grid(row=1, column=1, pady=5)

    Label(frame, text='To:', font=('Arial', 12), bg='#e3f2fd').grid(row=2, column=0, pady=5)
    to_currency = ttk.Combobox(frame, values=list(RATES.keys()), font=('Arial', 11))
    to_currency.grid(row=2, column=1, pady=5)

    btn = Button(window, text='Convert', font=('Arial', 13, 'bold'), bg = '#4caf50', command=convert_currency)
    btn.pack(pady=10)
            
    result_label = Label(window, text='')
    result_label.pack(pady=10)

    window.mainloop()