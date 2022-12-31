from tkinter import *
window_1 = Tk()
label_1 = Label()


def color1():
    label_1['bg'] = 'red'


label_1 = Label(window_1, text='What Color')
button_1 = Button(window_1, text="Clinck Me", command=color1)


button_1.grid(column=0, row=1)
label_1.grid(column=0, row=0)
window_1.mainloop()
