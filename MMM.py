def mean(lista):
    suma=0
    brojac=0
    for i in lista:
        suma+=i
        brojac+=1
    k=suma/brojac
    print(k)

def median(lista):
    brojac=0
    vrednost=0
    for i in lista:
        brojac+=1
    if brojac % 2 == 0:
        brojac=brojac/2
        brojac=int(brojac)
        vrednost=lista[brojac]
    else:
        brojac = (brojac + 1) / 2
        brojac=int(brojac)
        vrednost = lista[brojac]
    print(vrednost)

def mode(lista):
    print("Comming soon")

lista1=[11,25,16,43,55,75,25]
lista2=[3,5,5,5,5,5,5,6,10,12,13]
lista3=[]
mode(lista3)