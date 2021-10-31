def creeazaObiect(id, nume, descriere, pret, locatie):
    '''
    creeaza un dictionar ce retine un obiect
    :param id: id-ul obiectului - string
    :param nume: numele obiectului - string
    :param descriere: descrierea obiectului - string
    :param pret: pretul obiectului - float
    :param locatie: locatia obiectului - string
    :return: un dictionar ce retine un obiect
    '''
    return [id, nume,descriere,pret,locatie]

def getId(obiect):
    '''
    da id-ul unui obiect
    :param vanzare: un dictionar de tip obiect
    :return: id-il obiectului - string
    '''
    return obiect[0]

def getNume(obiect):
    return obiect[1]

def getDescriere(obiect):
    return obiect[2]

def getPret(obiect):
    return obiect[3]

def getLocatie(obiect):
    return obiect[4]

def toString(obiect):
    return "id: {}, nume: {}, descriere: {}, pret: {}, locatie: {}".format(
        getId(obiect),
        getNume(obiect),
        getDescriere(obiect),
        getPret(obiect),
        getLocatie(obiect)
    )