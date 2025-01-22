import tkinter 
from tkinter import *
from tkinter import scrolledtext
root=tkinter.Tk()
root.title('chatbox')
root.geometry('500x500')

def send_text():
    n=tect_scrol.get('1.0',END)# 1 is line and 0 is charecter
    disply.config(state=NORMAL)
    disply.insert(END,'you:'+n)
    disply.insert(END,'Bot:'+'yes'+'\n',)
    disply.config(state=DISABLED)
    tect_scrol.delete('1.0',END)



header= tkinter.Label(root,text='welcome my text box',font=('grick',30),bg='skyblue',fg='red')
header.pack(fill=tkinter.X , expand=True)

disply=scrolledtext.ScrolledText(root,wrap=tkinter.WORD,height=15,state=tkinter.DISABLED,bg='grey',fg='black')
disply.pack(fill=tkinter.BOTH,expand=True,)

tect_scrol=scrolledtext.ScrolledText(root,wrap=tkinter.WORD,height=3)
tect_scrol.pack(fill=tkinter.BOTH,expand=True)

send_button=tkinter.Button(root,text='send',font=('grick',12),fg='white',bg='black',command=send_text)
send_button.pack()


root.mainloop()