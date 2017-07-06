from tkinter import *
root = Tk()

menu_bar = Frame(root)
menu_bar.pack()

Menubutton(menu_bar).pack()
Menu(menu_bar)

frame_1 = Frame(root)
frame_1.pack()
Label(frame_1, text="label").pack()
Entry(frame_1).pack()
Checkbutton(frame_1).pack()
Radiobutton(frame_1, value=2).pack()
Radiobutton(frame_1, value=1).pack()
Button(frame_1, text="button").pack()
# Optionsmenu(frame_1).pack()
# BitmapImage(frame_1)

frame_2 = Frame(root).pack()
photo = PhotoImage(frame_2)
Listbox(frame_2).pack()
Spinbox(frame_2).pack()
Scale(frame_2).pack()
LabelFrame(frame_2, text="labelframe").pack()
Message(frame_2, text = "message").pack()

frame_3 = Frame(root).pack()
Text(frame_3).pack()
Scrollbar(frame_3).pack()

root.mainloop()
