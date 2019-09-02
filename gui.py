from tkinter import *
import database
def get_index(event):
    global t
    index=list1.curselection()[0]
    t=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,t[1])
    e2.delete(0,END)
    e2.insert(END,t[2])
    e3.delete(0,END)
    e3.insert(END,t[3])
    e4.delete(0,END)
    e4.insert(END,t[4])


def show():
    list1.delete(0,END)
    for i in database.view():
        list1.insert(END,i)

def find():
     list1.delete(0,END)
     for i in database.search(t_text.get(),a_text.get(),y_text.get(),i_text.get()):
        list1.insert(END,i)
def add():
    database.insert(t_text.get(),a_text.get(),y_text.get(),i_text.get())
    list1.delete(0,END)
    list1.insert(END,(t_text.get(),a_text.get(),y_text.get(),i_text.get()))

def erase():
    database.delete(t[0])
def change():
    database.update(t[0],t_text.get(),a_text.get(),y_text.get(),i_text.get())

root=Tk()
root.title("Book Manager")
root.resizable(width=0,height=0)
l1=Label(root,text='Title',fg='blue')
l2=Label(root,text='Author',fg='blue')
l3=Label(root,text='Year',fg='blue')
l4=Label(root,text='ISBN',fg='blue')
l1.grid(row=0,column=0)
l2.grid(row=0,column=2)
l3.grid(row=1,column=0)
l4.grid(row=1,column=2)

t_text=StringVar()
a_text=StringVar()
i_text=StringVar()
y_text=StringVar()
e1=Entry(root,textvariable=t_text)
e1.grid(row=0,column=1)

e2=Entry(root,textvariable=a_text)
e2.grid(row=0,column=3)

e3=Entry(root,textvariable=y_text)
e3.grid(row=1,column=1)

e4=Entry(root,textvariable=i_text)
e4.grid(row=1,column=3)

list1=Listbox(root,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

s1=Scrollbar(root)
list1.configure(yscrollcommand=s1.set)
s1.configure(command=list1.yview)
s1.grid(row=2,column=2,rowspan=6)

list1.bind('<<ListboxSelect>>',get_index)

b1=Button(root,text="View all", width=12,fg='red',command=show)
b1.grid(row=2,column=3)

b2=Button(root,text="Search", width=12,fg='red',command=find)
b2.grid(row=3,column=3)

b3=Button(root,text="Add", width=12,fg='red',command=add)
b3.grid(row=4,column=3)

b4=Button(root,text="Update", width=12,fg='red',command=change)
b4.grid(row=5,column=3)

b5=Button(root,text="Delete", width=12,fg='red',command=erase)
b5.grid(row=6,column=3)

b6=Button(root,text="Close", width=12,fg='red',command=root.quit)
b6.grid(row=7,column=3)
root.mainloop()