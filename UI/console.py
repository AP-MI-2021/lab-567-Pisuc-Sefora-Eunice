from Domain.obiect import toString
from Logic.CRUD import adaugaObiect, stergeObiect, modificaObiect
from Logic.functionalitati import pretMaximLocatie, modificareLocatie, modificareDescriere, ordonareCrescatorDupaPret, \
    sumaPreturilorPtFiecareLocatie
import copy


def printMenu():
    print("1. Adaugare obiect")
    print("2. Stergere obiect")
    print("3. Modificare obiect")
    print("4. Mutarea tuturor obiectelor dintr-o locație în alta")
    print("5. Concatenarea unui string citit la toate descrierile obiectelor "
          "cu prețul mai mare decât o valoare citită")
    print("6. Determinarea celui mai mare preț pentru fiecare locație")
    print("7. Ordonarea obiectelor crescător după prețul de achiziție")
    print("8. Afișarea sumelor prețurilor pentru fiecare locație")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare toate obiectele")
    print("x. Iesire")


def uiAdaugareObiecte(lista, undoList, redoList):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        descriere = input("Dati descrierea: ")
        pret = input("Dati pretul: ")
        locatie = input("Dati locatia: ")

        rezultat = adaugaObiect(id, nume, descriere, pret, locatie, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergereObiect(lista, undoList, redoList):
    try:
        id = input("Dati id-ul obiectului de sters: ")
        rezultat = stergeObiect(id, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista



def uiModificareObiect(lista, undoList, redoList):
    try:
        id = input("Dati id-ul obiectului de modificat: ")
        nume = input("Dati noul numele: ")
        descriere = input("Dati noua descriere: ")
        pret = input("Dati noul pret: ")
        locatie = input("Dati noua locatie: ")
        rezultat = modificaObiect(id, nume, descriere, pret, locatie, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat

    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiModificareLocatie(lista, undoList, redoList):
    try:
        locatie = input("Introducem noua locatie: ")
        undoList.append(lista)
        redoList.clear()
        temp_list = copy.deepcopy(lista)
        rezultat = modificareLocatie(temp_list, locatie)
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiModificareDescriere(lista, undoList, redoList):
    try:
        descriere = input("Introducem descriere de adaugat: ")
        pret = input("Introducem pretul: ")
        undoList.append(lista)
        redoList.clear()
        temp_list = copy.deepcopy(lista)
        rezultat = modificareDescriere(temp_list, descriere, pret)
        return rezultat

    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiPretMaximLocatie(lista):
    dict = pretMaximLocatie(lista)
    for key in dict:
        print("Locatia {} are cel mai mare pret {}". format(key, dict[key]))


def uiOrdonareCrescatorDupaPret(lista):
    return ordonareCrescatorDupaPret(lista)

def uiSumaPreturilorPtFiecareLocatie(lista):
    dict = sumaPreturilorPtFiecareLocatie(lista)
    for key in dict:
        print("Locatia {} are suma preturilor {}.". format(key, dict[key]))


def showAll(lista):
    for obiect in lista:
        print(toString(obiect))

def ui_undo(lista, undo_list, redo_list) -> list:
    if len(undo_list) > 0:
        redo_list.append(lista)
        return undo_list.pop()
    return lista


def ui_redo(lista, undo_list, redo_list) -> list:
    if len(redo_list) > 0:
        undo_list.append(lista)
        return redo_list.pop()
    return lista


def runMenu(lista):
    undoList = []
    redoList = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugareObiecte(lista, undoList, redoList)
        elif optiune == "2":
            lista = uiStergereObiect(lista, undoList, redoList)
        elif optiune == "3":
            lista = uiModificareObiect(lista, undoList, redoList)
        elif optiune == "4":
            lista = uiModificareLocatie(lista, undoList, redoList)
        elif optiune == "5":
            lista = uiModificareDescriere(lista, undoList, redoList)
        elif optiune == "6":
            uiPretMaximLocatie(lista)
        elif optiune == "7":
            s_lista = uiOrdonareCrescatorDupaPret(lista)
            showAll(s_lista)
        elif optiune == "8":
            uiSumaPreturilorPtFiecareLocatie(lista)
        elif optiune == "u":
            if len(undoList) > 0:
                redoList.append(lista)
                lista = undoList.pop()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redoList) > 0:
                undoList.append(lista)
                lista = redoList.pop()
            else:
                print("Nu se poate face redo!")
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")