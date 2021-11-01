from Domain.obiect import toString
from Logic.CRUD import adaugaObiect, stergeObiect, modificaObiect


def printMenu():
    print("1. Adaugare obiect")
    print("2. Stergere obiect")
    print("3. Modificare obiect")
    print("4. Mutarea tuturor obiectelor dintr-o locație în alta")
    print("5. Concatenarea unui string citit la toate descrierile obiectelor "
          "cu prețul mai mare decât o valoare citită")
    print("6. Determinarea celui mai mare preț pentru fiecare locație")
    print("a. Afisare toate obiectele")
    print("x. Iesire")


def uiAdaugareObiecte(lista):
    id = input("Dati id-ul: ")
    nume = input("Dati numele: ")
    descriere = input("Dati descrierea: ")
    pret = input("Dati pretul: ")
    locatie = input("Dati locatia: ")
    return adaugaObiect(id, nume, descriere, pret, locatie, lista)


def uiStergereObiect(lista):
    id = input("Dati id-ul obiectului de sters: ")
    return stergeObiect(id, lista)


def uiModificareObiect(lista):
    id = input("Dati id-ul obiectului de modificat: ")
    nume = input("Dati noul numele: ")
    descriere = input("Dati noua descriere: ")
    pret = input("Dati noul pret: ")
    locatie = input("Dati noua locatie: ")
    return modificaObiect(id, nume, descriere, pret, locatie, lista)

def uiModificareLocatie(lista):
    locatie = input("Introducem noua locatie: ")
    for obiect in lista:
        obiect[4] = locatie
    return lista

def uiModificareDescriere(lista):
    descriere = input("Introducem descriere de adaugat: ")
    pret = input("Introducem pretul: ")
    for obiect in lista:
        if int(obiect[3]) > int(pret):
            obiect[2] = obiect[2] + " " +descriere
    return lista

def uiPretMaximLocatie(lista):
    dict={}
    for obiect in lista:
        dict.update({obiect[4]: 0})
    for obiect in lista:
        if int(dict[obiect[4]]) < int(obiect[3]):
            dict[obiect[4]] = obiect[3]
    print(dict)

def showAll(lista):
    for obiect in lista:
        print(toString(obiect))


def runMenu(lista):

    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugareObiecte(lista)
        elif optiune == "2":
            lista = uiStergereObiect(lista)
        elif optiune == "3":
            lista = uiModificareObiect(lista)
        elif optiune == "4":
            lista = uiModificareLocatie(lista)
        elif optiune == "5":
            lista = uiModificareDescriere(lista)
        elif optiune == "6":
            uiPretMaximLocatie(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")