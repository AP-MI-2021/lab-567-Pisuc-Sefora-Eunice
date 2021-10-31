from Domain.obiect import getId, getNume, getDescriere, getPret, getLocatie
from Logic.CRUD import adaugaObiect, getById, stergeObiect


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