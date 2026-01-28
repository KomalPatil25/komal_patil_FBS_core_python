from tkinter import *
from tkinter import messagebox

def login():
    uid = uid_entry.get()
    passw = passw_entry.get()
    if uid =='admin' and passw == '1234':
        messagebox.showinfo('Message', message='Login Successfully...')
    else:
        messagebox.showerror('Message', message='Username and Password is Invalid.')
def main():
    user_id_label = Label(window, text='USERID: ')
    global uid_entry
    uid_entry = Entry(window)
    passw_label = Label(window, text='PASSWORD')
    global passw_entry
    passw_entry = Entry(window)
    btn = Button(window, text='LOGIN', command=login)
    user_id_label.pack()
    uid_entry.pack()
    passw_label.pack()
    passw_entry.pack()
    btn.pack()

if __name__ == '__main__':
    window = Tk()
    window.title('Login')
    window.config(background='Pink')
    window.geometry('300x400')

    main()
    window.mainloop()