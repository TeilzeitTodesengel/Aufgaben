from tkinter import *

root = Tk()
root.title('Hallo Welt')
root.geometry("300x300")

my_label = Label(root, text="Hallo Welt", fg="black", font=("arial", 12))
my_label.pack(pady=10)
root.mainloop()