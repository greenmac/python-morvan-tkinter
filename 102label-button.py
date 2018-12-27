# https://morvanzhou.github.io/tutorials/python-basic/tkinter/2-01-label-button/
# https://github.com/MorvanZhou/tutorials/blob/master/tkinterTUT/tk2_label_button.py
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x100')

var = tk.StringVar()
l = tk.Label(window, textvariable=var, bg='green', font=('Arial', 12), width=15, height=2)
l.pack() # pack grid place 放置位置- 窗口Tkinter

on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')
b = tk.Button(window, text='hit me', width=15, height=2, command=hit_me)
b.pack() # pack grid place 放置位置- 窗口Tkinter

window.mainloop()