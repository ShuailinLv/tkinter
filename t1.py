import tkinter as tk

window = tk.Tk()
window.title('first window')
window.geometry('200x100')

l = tk.Label(window, text='hello tkinter', bg='green', font=('Arial, 12'), width=15, height=2)
l.pack()
window.mainloop()



