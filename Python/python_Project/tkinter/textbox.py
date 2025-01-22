import tkinter
root=tkinter.Tk()

lable=tkinter.Label(root,text='Enter your name: ')
lable.pack() #pack for organized
text_box=tkinter.Entry(root) # .entry for creating textbox
text_box.pack()

lable1=tkinter.Label(root,text='Enter your email: ')
lable1.pack() #pack for organized
text_box1=tkinter.Entry(root)
text_box1.pack()

root.mainloop()