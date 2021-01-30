#dizi if  ve döngü kullanarak örnek
#örnek1:kullanıcının girdiği bir ifadede a harfinin sayısını bulunuz.
"""
a=input("bir ifade giriniz:")
sayac=0
for i in a:
    if i=="a":
        sayac+=1
print(f"ifadenizdeki a harfi sayısı: {sayac}")
"""
# örnek1:Birden 20ye kadar olan sayıların   beşin katı olan sayıları listeleyin.
"""
dizi=[]
for i in range (1,21):
    if i%5==0:
        dizi.append(i)
print(dizi)
"""
#örnek3 örnek2:Üçün katı dışındaki sayıların ekrana yazdırılması (continue örneği)
# break komutu
"""
 for i in range (1,10):
    print(i)
    if i==5:
        break
"""
#örneğin continue kullanılarak yapılmış hali
"""
for i in range (1,21):
    if i%3==0:
        continue
    print(i)
"""