import random
"""
a=random.randrange(1,15)
print(a)
"""
"""
dizi=[]
for i in range(1,4):
    a=random.randrange(1,5)
    if a in dizi:
        print("bu zaten var")
        a=random.randrange(1,5)
        if a in dizi:
            a = random.randrange(1, 5)
            if a in dizi:
                a = random.randrange(1, 5)
    else:
         dizi.append(a)

print(dizi)
"""
"""
a=random.randrange(1,20)
print(a)
hak=3
while hak>0:
    b=int(input("tahmininiz:"))
    if b==a:
        print("bildiniz")
        hak=0
    else:
        hak=hak-1
        print(f"{hak}hakkınız kaldı")
"""