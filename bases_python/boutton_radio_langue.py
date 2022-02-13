from tkinter import *

fen = Tk()
fen.geometry("200x200")
fen.title("boutonRadio")

u = IntVar(fen)
case1 = Radiobutton(fen, variable = u, value = 10, fg = "red")
case2 = Radiobutton(fen, variable = u, value = 20, fg = "blue")
case3 = Radiobutton(fen, variable = u, value = 30, fg = "orange")

case1.place(x = 0, y = 50)
case2.place(x = 0, y = 100)
case3.place(x = 0, y = 150)

case1.config(text = "Allemand")
case2.config(text = "Anglais")
case3.config(text = "Italien")

u.set(20)
print(u.get())

fen.mainloop()