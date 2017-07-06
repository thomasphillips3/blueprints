from tkinter import *
parent = Tk()
parent.title('ADB Tool')
Label(parent, text="Connected devices").grid(row=0, column=0, columnspan=2)
Label(parent, text="Available versions").grid(row=0, column=2, columnspan=2)
Entry(parent).grid(row=1, column=0, columnspan=2, rowspan=4)
Entry(parent).grid(row=1, column=2, columnspan=2, rowspan=4)
parent.button = Button(parent, text="Install", highlightbackground="green").grid(row=6, column=0)
parent.mainloop()
