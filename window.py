from tkinter import *


def add_lable():
    label_3 = Label(my_window, text="YouClicked?")
    label_3.pack()


my_window = Tk()
my_window.title("Great fish")
my_window.configure(height=200, width=500)
my_window.geometry("300x500+500+500")
my_window.resizable(height=False, width=False)
button_1 = Button(my_window, text='click me', command=add_lable)
button_1.pack()
label_1 = Label(my_window, text="text", borderwidth=2, relief='solid',
                fg="white", background='blue', padx=12, justify='left')
label_1.pack()
# print atributes in a function
for item in label_1.keys():
    print(item, ":", label_1[item])
label_1['text'] = "Fish"
label_1['bd'] = 2
my_window.mainloop()
