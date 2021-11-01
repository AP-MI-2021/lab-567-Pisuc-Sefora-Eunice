from Domain.obiect import getId, getNume, getDescriere, getPret, getLocatie
from Logic.CRUD import adaugaObiect, getById, stergeObiect, modificaObiect


def testAdaugaObiect():
    lista=[]
    lista = adaugaObiect("1", "caiet", "A4", 10, "mall", lista)

    
    assert len(lista) == 1
    assert getId(getById("1", lista)) == "1"
    assert getNume(getById("1", lista)) == "caiet"
    assert getDescriere(getById("1", lista)) == "A4"
    assert getPret(getById("1", lista)) == 10
    assert getLocatie(getById("1", lista)) == "mall"

def testStergeObiect():
    lista = []
    lista = adaugaObiect("1", "caiet", "A4", 10, "mall", lista)
    lista = adaugaObiect("2", "pix", "negru", 3, "dm", lista)

    lista = stergeObiect("1", lista)

    assert len(lista) == 1
    assert getById("1") is None
    assert getById("2") is not None

    lista = stergeObiect("3", lista)

    assert len(lista) == 1
    assert getById("2") is not None

def testModificaObiect():
    lista = []
    lista = adaugaObiect("1", "caiet", "A4", 10, "mall", lista)
    lista = adaugaObiect("2", "pix", "negru", 3, "dm", lista)
    lista = modificaObiect("1", "penar", "mic", 15, "compas", lista)
    modificareObiect = getById("1", lista)
    assert getId(modificareObiect) == "1"
    assert getNume(modificareObiect) == "penar"
    assert getDescriere(modificareObiect) == "mic"
    assert getPret(modificareObiect) == 15
    assert getLocatie(modificareObiect) == "compas"



def testGetById():
    lista = []
    lista = adaugaObiect("1", "caiet", "A4", 10, "mall", lista)
    lista = adaugaObiect("2", "pix", "negru", 3, "dm", lista)

    assert getById("2", lista) is not None
    assert getById("3", lista) is None