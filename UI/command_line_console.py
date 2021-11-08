from Logic.CRUD import adaugaObiect, stergeObiect
from UI.console import showAll


def printMenu():
    print("1. Adaugare obiect [add,id,nume,descriere,pret,locatie]")
    print("2. Stergere obiect [delete,id]")
    print("a. Afisare toate obiectele[showall]")
    print("x. Iesire")


def runMenuCommandLine(lista):

    while True:
        printMenu()
        optiune = input("Dati comenzile: ")
        optiune = optiune.split(";")
        for opt in optiune:

            opt = opt.split(",")
            if opt[0] == "add":
                lista = adaugaObiect(opt[1], opt[2], opt[3], opt[4], opt[5], lista)
            elif opt[0] == "delete":
                lista = stergeObiect(opt[1], lista)
            elif opt[0] == "showall":
                showAll(lista)
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati: ")