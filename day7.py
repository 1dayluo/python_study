from tkinter import *

from pip import get_installed_distributions

app = Tk()
label = Label(text='Python Packages',font=('Hack',20,'bold'))
listbox = Listbox()

lists = get_installed_distributions()
for list in lists:
    listbox.insert(END,list)

label.pack()
listbox.pack()

app.mainloop()
