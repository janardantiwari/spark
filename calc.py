from tkinter import *


def click(number):
    k=e.index(INSERT)
    e.insert(k,number)


def clear():
    e.delete(0,END)

def evaluate():
        r="123456789"
        p=""
        s=str(e.get())
        for i in range(len(s)):
                if (i==0 and s[i]=='0') or (s[i]=='0' and i+1<len(s) and (s[i-1] not in r) ):
                        continue
                else :
                        p+=s[i]
        #print(p)

        if(p[len(p)-2:]=='/0'):
            e.delete(0,END)
            e.insert(0,"INVALID INPUT")
        else:
            k=eval(p)
            e.delete(0,END)
            click(k)
        
def remove():
    k=e.index(INSERT)
    e.delete(k-1,k)

base=Tk()
base.title("Calculator")


base.resizable(height=0,width=0)
e=Entry(base,width=45,borderwidth=5,relief=SUNKEN,fg="blue")
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

b0=Button(base,text="0",padx=40,pady=20,  command= lambda : click(0))
b1=Button(base,text="1",padx=40,pady=20  , command= lambda : click(1))
b2=Button(base,text="2",padx=40,pady=20  , command= lambda : click(2))
b3=Button(base,text="3",padx=40,pady=20  , command= lambda : click(3))
b4=Button(base,text="4",padx=40,pady=20  , command= lambda : click(4))
b5=Button(base,text="5",padx=40,pady=20  , command= lambda : click(5))
b6=Button(base,text="6",padx=40,pady=20  , command= lambda : click(6))
b7=Button(base,text="7",padx=40,pady=20  , command= lambda : click(7))
b8=Button(base,text="8",padx=40,pady=20  , command= lambda : click(8))
b9=Button(base,text="9",padx=40,pady=20  , command= lambda : click(9))


b0.grid(row=4,column=0)
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)


a=Button(base,text="+",padx=37,pady=20 ,command= lambda : click("+"))
a.grid(row=1,column=3)
s=Button(base,text="-",padx=40,pady=20,command= lambda : click("-") )
s.grid(row=2,column=3)
m=Button(base,text="*",padx=40,pady=20,command= lambda : click("*") )
m.grid(row=3,column=3)
d=Button(base,text="/",padx=40,pady=20,command= lambda : click("/") )
d.grid(row=4,column=3)
clr=Button(base,text="c",padx=40,pady=20,command=clear )
clr.grid(row=4,column=2)
eq=Button(base,text="=",padx=185,pady=15,command= evaluate )
eq.grid(row=5,column=0,columnspan=4)
delete=Button(base,text="del",padx=35,pady=20,command=remove)
delete.grid(row=4,column=1)


base.mainloop()
