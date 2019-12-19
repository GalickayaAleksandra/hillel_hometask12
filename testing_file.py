from tkinter import *

root = Tk()
root.title("Моя программа Python")
root.geometry("500x500+300+100")

my_button = Button(text="Click",
                   background="#555",
                   foregraund="#ccc",
                   padx="50",
                   pady="8"
                   )
my_button.pack()

root.mainloop()
