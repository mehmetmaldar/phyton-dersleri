from tkinter import *
from tkinter import messagebox
def tıkla():
    if c.get()=="" or d.get()==""or z.get()==""  :
        messagebox.showinfo("KAYDOL","TÜM ALANLARI DOLDURUNUZ")
    elif len(z.get())<11 and len(z.get())>11:
        messagebox.showinfo("KAYDOL", "TELEFONU DÜZGÜN GİRİNİZ")
    else:
        messagebox.showinfo("KAYDOL", "KAYIT BAŞARILI")




pencere=Tk()
pencere.title("GİRİŞ")
pencere.geometry("200x200-200+10")
a=Label(pencere,text="Kullanıcı Adı")
a.grid(row=0,column=0)
b=Label(pencere,text="Şifre")
b.grid(row=1,column=0,stick=W)
c=Entry(pencere,width=20)
c.grid(row=0,column=1)
z=Entry(pencere,width=20)
z.grid(row=1,column=1)
d=Entry(pencere,width=20)
d.grid(row=2,column=1)
e=Label(pencere,text="Telefon")
e.grid(row=2,column=0,stick=W)

f=Button(pencere,text="KAYDOL",command=tıkla,width=10)
f.grid(row=9,column=1)

mainloop()
