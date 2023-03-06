#n stands for counter
#vr stands for value
#s stands for sum

def counter(lista):
    n = 0
    for i in lista:
        n += 1
    return n
def mean(lista):
    s=0
    n=counter(lista)
    for i in lista:
        s+=i
    vr=s/n
    print(vr)

def median(lista):
    n=counter(lista)
    vr=0
    if n % 2 == 0:
        n=(n+1)/2
        n=int(n)
        vr=lista[n]
    else:
        n = n / 2
        n=int(n)
        vr = lista[n]
    return vr

def mode(lista):
    vr=0
    for i in lista:
        vr2 = 0
        for j in lista:
            if i==j:
                vr2+=1
                if vr2>vr:
                    vr=vr2
                    trvr = i
    print(trvr, "appears ", vr, "times")
    return vr

lista1=[11,25,16,43,55,75,25]
lista2=[3,5,5,5,5,5,5,6,10,12,13]
lista3=[150, 642, 343, 221, 560, 770, 853]