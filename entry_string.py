from tkinter import *
window_1 = Tk()


def print_num():
    number1 = int(entry_1.get())  # This is how to enter as a integer
    label_2 = Label(window_1)
    x = number1 + 1
    label_2['text'] = (f'Your number{x}')
    label_2.grid(row=3, column=0, columnspan=3)


window_1.frame()
label_1 = Label(window_1, text="enter number")
# label_2 = Label(window_1, text="your number'is")
window_1.title('Number plus 1')
window_1.geometry("200x200+100+100")


entry_1 = Entry(window_1, border=4)
button_1 = Button(window_1, text='see number button',
                  command=print_num, activeforeground="blue", activebackground="red")

label_1.grid()

# label_2.grid(row=1, column=1)
entry_1.grid()
button_1.grid()

window_1.mainloop()
