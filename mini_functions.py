#n stands for counter
#vr stands for value
#s stands for sum
#c stands for condition

import math
def counter(lista):
    n = 0
    for i in lista:
        n += 1
    return n
def cdCounter(cd):
    br=0
    if cd == 80:
        cd = 1.282
        br += 1
    if cd == 85:
        cd = 1.440
        br += 1
    if cd == 90:
        cd = 1.645
        br += 1
    if cd == 95:
        cd = 1.960
        br += 1
    if cd == 99:
        cd = 2.576
        br += 1
    if cd == 99.5:
        cd = 2.807
        br += 1
    if cd == 99.9:
        cd = 3.291
        br += 1
    if br==1:
        return cd
    else:
        print("Not supported value, we will work as if it was 95%")
        return 1.960
def mean(lista):
    s=0
    n=counter(lista)
    for i in lista:
        s+=i
    vr=s/n
    return vr

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
def populationVariance(lista):
    s = 0
    s1 = 0
    k = mean(lista)
    n = counter(lista)
    for i in lista:
        s1 = i - k
        s1 = math.pow(s1, 2)
        s += s1
    s = s /n
    return s
def populationStandardDeviation(lista):
    vr = populationVariance(lista)
    vr = math.sqrt(vr)
    return vr
def sampleVariance(lista):
    s=0
    s1=0
    k=mean(lista)
    n=counter(lista)
    for i in lista:
        s1=i-k
        s1=math.pow(s1,2)
        s+=s1
    s=s/(n-1)
    return s
def sampleStandardDeviation(lista):
    vr=sampleVariance(lista)
    vr=math.sqrt(vr)
    return vr

def confidenceInterval(lista,cd):
    cd=cdCounter(cd)
    x=mean(lista)
    n=counter(lista)
    st=sampleStandardDeviation(lista)
    x1=x-cd*(st/math.sqrt(n))
    x2=x+cd*(st/math.sqrt(n))
    vr=[x1,x2]
    return vr

def sortOneTime(lista):
    n=counter(lista)-1
    n1=0
    n2=n1+1
    for i in lista:
        for j in lista:
            if n2<=n:
                if lista[n1]>lista[n2]:
                    pom=lista[n1]
                    lista[n1]=lista[n2]
                    lista[n2]=pom
                n2+=1
            n1+=1
    print(lista)
def sortMultiTime(lista):
    n=counter(lista)-1
    n1=0
    while n>=n1:
        sortOneTime(lista)
        n1+=1

def sortGeneral(lista):
    c = counter(lista) - 1
    c1 = 0
    while c >= c1:

        n = counter(lista) - 1
        n1 = 0
        n2 = n1 + 1
        for i in lista:
            for j in lista:
                if n2 <= n:
                    if lista[n1] > lista[n2]:
                        pom = lista[n1]
                        lista[n1] = lista[n2]
                        lista[n2] = pom
                    n2 += 1
                n1 += 1

        c1 += 1
    print(lista)

lista1=[11,25,16,43,55,75,25]
lista2=[3,5,5,5,5,5,5,6,10,12,13]
lista3=[150, 642, 343, 221, 560, 770, 853]
listav=[6,8,10,12]