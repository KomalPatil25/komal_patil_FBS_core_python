from tkinter import *
from tkinter import messagebox

questions = [
    'What is the capital of India?', 
    'Which language is used for web apps?', 
    'Which planet known as the Red Planet?',
    'What is 5 + 7?'
    'Which is the largest ocean on Earth?']
opetion = [
    ['Mumbai', 'Delhi', 'Kolkata', 'Pune'], 
    ['Python', 'C++', 'HTML', 'Java'],
    ['Earth', 'Mars', 'Jupiter', 'Saturn'],
    ['10', '11', '12', '13'],
    ['Altantic', 'Pacific', 'Indian', 'Arctic']
    ]

answers = [2, 3, 2, 3, 2]

if __name__ == '__main__':
    window = Tk()
    window.title('Quize Game')
    window.geometry('300x400')
    window.config(bg='Pink')
    
    window.mainloop()