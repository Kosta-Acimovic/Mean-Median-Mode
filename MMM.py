#br stands for counter
#vr stands for value
#s stands for sum

def mean(lista):
    s=0
    br=0
    for i in lista:
        s+=i
        br+=1
    vr=s/br
    print(vr)

def median(lista):
    br=0
    vr=0
    for i in lista:
        br+=1
    if br % 2 == 0:
        br=br/2
        br=int(br)
        vr=lista[br]
    else:
        br = (br + 1) / 2
        br=int(br)
        vr = lista[br]
    print(vr)

def mode(lista):
    vr=0
    for i in lista:
        vr2 = 0
        for j in lista:
            if i==j:
                vr2+=1
                if vr2>vr:
                    vr=vr2
    print(vr)

lista1=[11,25,16,43,55,75,25]
lista2=[3,5,5,5,5,5,5,6,10,12,13]
lista3=[150, 642, 343, 221, 560, 770, 853]