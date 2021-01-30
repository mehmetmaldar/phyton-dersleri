"""
a=ekleme
r=okuma
w=yazma
r+=hemyazma hem okuma
"""
"""
a=open("rehber.dat","w")
c=input("bir isim giriniz:")
a.write("\t"c)
a.close()
"""
"""
a=open("rehber.dat","r")
c=a.read()
b=a.readline()
a.seek(0)
d=a.readlines()
print(d)
a.close()
"""
"""
a=open("rehber.dat","a")
a.write("\n ahmet")
a.close()
b=open("rehber.dat","w")
b.close()
"""
"""
a=open("rehber.dat","r+")
a.write("mehmet\n")
a.write("ahmet\n")
a.write("yusuf\n")
c=a.readlines()
a.seek(0)
d=a.read()
print(d)
"""