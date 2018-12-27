# https://morvanzhou.github.io/tutorials/python-basic/tkinter/2-02-entry-text/
# https://github.com/MorvanZhou/tutorials/blob/master/tkinterTUT/tk3_entry_text.py
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

# e = tk.Entry(window, show='*') # show='*'默認不顯示, 像是密碼形式
e = tk.Entry(window, show=None)
e.pack()

def insert_point():
    var = e.get()
    t.insert('insert', var)

def insert_end():
    var = e.get()
    t.insert('end', var)
    t.insert(1.1, var)

b1 = tk.Button(window, text='insert point', width=15, height=2, command=insert_point)
b1.pack() # pack grid place 放置位置- 窗口Tkinter

b2 = tk.Button(window, text='insert end', command=insert_end)
b2.pack()

t = tk.Text(window, height=2)
t.pack()

window.mainloop()