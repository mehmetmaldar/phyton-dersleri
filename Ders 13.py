
from tkinter import *
from tkinter import messagebox
def tıkla():
    if c.get()=="mehmet" and d.get()=="123":
        messagebox.showinfo("GİRİŞ","GİRİŞ YAPTINIZ")
    else:
        messagebox.showinfo("","DÜZGÜN GİRİNİZ")


pencere=Tk()
pencere.title("GİRİŞ")
pencere.geometry("200x200-200+10")
a=Label(pencere,text="Kullanıcı Adı")
a.grid(row=0,column=0)
b=Label(pencere,text="Şifre")
b.grid(row=1,column=0,stick=W)
c=Entry(pencere,width=20)
c.grid(row=0,column=1)
d=Entry(pencere,width=20)
d.grid(row=1,column=1)
f=Button(pencere,text="GİRİŞ",command=tıkla,width=10)
f.grid(row=9,column=1)

mainloop()
