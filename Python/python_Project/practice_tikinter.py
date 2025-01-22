import tkinter 
from tkinter import *
from tkinter import ttk, messagebox,scrolledtext
from openpyxl import load_workbook

root=tkinter.Tk()
root.title("practikce")
root.geometry('700x500')
root.configure(background='skyblue')

path=r"C:\Users\MD SHAFIUL ISLAM\OneDrive\문서\Book1.xlsx"
a=load_workbook(path)
b=a['Sheet1']

def main():
    n = name_gap.get()
    s = select.get()
    p = check.get()

    if n and s and p:
        b.append([n, s, p])
        a.save(path)
        messagebox.showinfo('congratulation', 'Submitted successfully')
    else:
        messagebox.showwarning("Warning", 'Please fill all the fields')


name=tkinter.Label(root,text='Enter name',fg='white',bg='black',font=('greek',20))
name.pack(anchor=tkinter.W,padx=50)
name_gap=tkinter.Entry(root,font=(20))
name_gap.pack(anchor=tkinter.W,padx=50,pady=5)

sub=tkinter.Label(root,text='select your choice',font=20)
sub.pack(anchor=tkinter.W,padx=50,pady=5)
choice=['csc','eee','me']
select=ttk.Combobox(values=choice,font=20)
select.pack(anchor=tkinter.W,padx=50,pady=5)

check=tkinter.IntVar()
checkbox=ttk.Checkbutton(root,text='agree all turms and conditions',variable=check)
checkbox.pack(anchor=tkinter.W,padx=50,pady=5)

button=tkinter.Button(root,text='submit',font=20,command=main)
button.pack(anchor=tkinter.W,padx=80,pady=5)

def text():
    p=book2.get('1.0',END)
    book.config(state=NORMAL)
    book.insert(END,"you: "+p)
    book.insert(END,"Bot :"+"thank you"+"\n")
    book.config(state=DISABLED)
    book2.delete('1.0',END)



book=scrolledtext.ScrolledText(root,wrap=tkinter.WORD,height=7,state=tkinter.DISABLED)
book.pack(fill=tkinter.BOTH,expand=True)

book2=scrolledtext.ScrolledText(root,wrap=tkinter.WORD,height=2)
book2.pack(fill=tkinter.BOTH,expand=True)

submit2=tkinter.Button(root,text='submit',command=text)
submit2.pack()


root.mainloop()