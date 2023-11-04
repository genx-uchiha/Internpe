from tkinter import *
from time import *

Block=Tk()
Block.title("Python clock")

def clk_update():
    time_string= strftime('%I: %M: %S %p')
    time_lable.config(text=time_string)

    time_lable.after(1000,clk_update)

time_lable= Label(Block, font=("Arial bold",80), foreground="blue", background="black")
time_lable.pack()
clk_update()
Block.mainloop()
