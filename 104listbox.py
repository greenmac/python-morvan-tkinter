# https://morvanzhou.github.io/tutorials/python-basic/tkinter/2-03-listbox/
# https://github.com/MorvanZhou/tutorials/blob/master/tkinterTUT/tk4_listbox.py
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

var1 = tk.StringVar() #创建变量
l = tk.Label(window, bg='yellow', width=4, textvariable=var1)
l.pack()

def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)

b1 = tk.Button(window, text='print selection', width=15, height=2, command=print_selection)
b1.pack() # pack grid place 放置位置- 窗口Tkinter

var2 = tk.StringVar()
var2.set((11, 22, 33, 44))
lb = tk.Listbox(window, listvariable=var2)
list_items = [1, 2, 3, 4]
for item in list_items:
    lb.insert('end', item)
lb.insert(1, 'first')
lb.insert(2, 'second')
lb.delete(2)
lb.pack()

window.mainloop()