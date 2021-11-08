from Domain.obiect import getPret


def modificareLocatie(lista, locatie):

    for obiect in lista:
        obiect[4] = locatie
    return lista

def modificareDescriere(lista, descriere, pret):
    for obiect in lista:
        if int(obiect[3]) > int(pret):
            obiect[2] = obiect[2] + " " +descriere
    return lista


def pretMaximLocatie(lista):
    '''

    :param lista:
    :return:
    '''
    dict = {}
    for obiect in lista:
        dict.update({obiect[4]: 0})
    for obiect in lista:
        if int(dict[obiect[4]]) < int(obiect[3]):
            dict[obiect[4]] = obiect[3]
    return dict

def ordonareCrescatorDupaPret(lista):
    return sorted(lista, key = lambda x: int(getPret(x)))

def sumaPreturilorPtFiecareLocatie(lista):
    dict = {}
    for obiect in lista:
        dict.update({obiect[4]: 0})
    for obiect in lista:
        dict[obiect[4]] += int(obiect[3])
    return dict
