from Domain.obiect import toString
from Logic.CRUD import adaugaObiect, stergeObiect, modificaObiect


def printMenu():
    print("1. Adaugare obiect")
    print("2. Stergere obiect")
    print("3. Modificare obiect")
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
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")