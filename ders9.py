#faktöriyel alma
"""a=int(input("faktöriyeli alınacak sayıyı giriniz:"))
fak=1
for i in range(1,a+1):
    fak=fak*i

print(fak)"""

def faktör(s):
    fak=1
    for i in range(1,s+1):
        fak=fak*i
    return fak

print(faktör(4))


print(faktör(10))