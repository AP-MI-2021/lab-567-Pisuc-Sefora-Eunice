from Domain import obiect
from Domain.obiect import creeazaObiect, getId


def adaugaObiect(id, nume, descriere, pret, locatie, lista):
    '''
    adauga un obiect intr-o lista
    :param id:
    :param nume:
    :param descriere:
    :param pret:
    :param locatie:
    :param lista:
    :return: o lista continand lista veche + noul obiect
    '''

    obiect = creeazaObiect(id, nume, descriere, pret, locatie)
    return lista + [obiect]

def getById(id, lista):
    '''
    ia obiectul cu id-ul dat dintr-o lista
    :param id: string
    :param lista: lista de obiecte
    :return: obiect cu id-ul dat sau None, daca nu exista nici un obiect cu id-ul dat
    '''
    for obiect in lista:
        if getId(obiect) == id:
            return obiect
    return None

def stergeObiect(id, lista):
    '''
    sterge un obiect dintr-o  lista dupa id
    :param id:
    :param lista: lista de obiecte
    :return:
    '''
    return [obiect for obiect in lista if getId(obiect) != id]

def modificaObiect(id, nume, descriere, pret, locatie, lista):
    '''

    :param id: id-ul dupa care se face  modificarea
    :param nume: noul nume
    :param descriere: noua descriere
    :param pret:
    :param locatie:
    :param lista:
    :return:
    '''
    listaNoua = []
    for obiect in lista:
        if getId(obiect) == id:
            obiectNou= creeazaObiect(id, nume, descriere, pret, locatie)
            listaNoua.append(obiectNou)
        else:
            listaNoua.append(obiect)
    return listaNoua
