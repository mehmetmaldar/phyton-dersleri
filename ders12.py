#buble sort
"""
import random
dizi=[]
for i in range(1,11):
    a=random.randrange(1,100)
    dizi.append(a)
print(dizi)

for i in range(len(dizi)-1,0,-1):
    for b in range(i):
        if dizi[b]>dizi[b+1]:
            dizi[b],dizi[b+1]=dizi[b+1],dizi[b]

print(dizi)
"""
#Selection sort
"""
dizi1=[2,1,11,4]
for i in range(len(dizi)):
    mini=i mini=0
    for j in range (i+1,len(dizi)):
        if dizi[mini]>dizi[j]:
            mini=j
    if mini!=i:
        dizi[mini],dizi[i]=dizi[i],dizi[mini]

"""


#selection sort
"""
dizi=[7,3,9,2,5]
for i in range(len(dizi)):
    key=i k=0
    for j in range(i+1,len(dizi)):
        if dizi[key]>dizi[j]:
            key=j



    if key!=i:
        dizi[key],dizi[i]=dizi[i],dizi[key]
print(dizi)

"""
"""
#marge sort
dizi=[1,4,2,11,9]
if len(dizi) > 1:
    orta=len(dizi)//2
    soldizi=dizi[:orta]
    sağdizi=dizi[orta:]
    i=0
    j=0
    k=0
    while i<len[soldizi]and j<len[sağdizi]:
       if soldizi[i]<sağdizi[j]:
           dizi[k]=soldizi[i]
           i=i+1
       else:
           dizi[k]=sağdizi[j]
           j=j+1
       k=k+1

    while i <len(soldizi):
        dizi[k]=soldizi[i]

    while j<len(sağdizi):
        dizi[k]=sağdizi[i]
        i=i+1
        k=k+1
"""

#inserion sort
"""
dizi=[1,4,2,11,9]
for i in range(1,len(dizi)): i=1 key=1 j=0
                              i=2 key=2 j=1
    key=dizi[i]
    j=i-1
    while j>=0 and key <dizi[j]:
        dizi[j+1]=dizi[j]
        j=j-1
    dizi[j+1]=key

"""


















