import tkinter
root=tkinter.Tk()
root.title("student regestation form")
lable1=tkinter.Label(root,text='Enter your name')
lable1.pack()
textbox1=tkinter.Entry(root)
textbox1.pack()

lable2=tkinter.Label(root,text='Enter your mail')
lable2.pack()
textbox2=tkinter.Entry(root)
textbox2.pack()

lable3=tkinter.Label(root,text='Enter your mobile')
lable3.pack()
textbox3=tkinter.Entry(root)
textbox3.pack()

submit_button=tkinter.Button(root,text='Submit')
submit_button.pack()

root.mainloop()