#if else
"""

a=int(input("yasınızı giriniz:"))
if a<18:
    print("reşit değil")
else:
    print("reşit bir birey")
    """

#örnek1 kullanıcının girdiği 2 not ortalamasını hesaplayıp kalıp kalmadığını söyleyen program
"""a=int(input("1.sınav notunu giriniz:"))
b=int(input("2.sınav notunu giriniz:"))
ortalama=(a+b)/2
if ortalama<50:
    print("KALDI")
else:
    print("geçti")
"""
#and kullanımı
""" 
a=int(input("1.sınav notunu giriniz:"))
b=int(input("2.sınav notunu giriniz:"))
ortalama=(a+b)/2
if ortalama<50:
    print("KALDI")
elif 50<=ortalama and ortalama <70:
    print("ortalama bir notla geçti")
else:
    print("yüksek notla geçti")
    """
#or kullanımı
"""
a=int(input("1.sınav notunu giriniz:"))
b=int(input("2.sınav notunu giriniz:"))
ortalama=(a+b)/2
if ortalama <=50 or ortalama==60:
    print("kaldı")

else:
    print("geçti")
"""
#örnek2 kullanıcının girdiği sayının tekmi çiftmi olduğunu kontrol eden program
a=int(input("bir sayı giriniz:"))
if a%2==0:
    print("çiftir")
else:
    print("tektir")