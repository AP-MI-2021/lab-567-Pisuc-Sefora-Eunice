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
    updated_object = getById("1", lista)
    assert getId(updated_object) == "1"
    assert getNume(updated_object) == "penar"
    assert getDescriere(updated_object) == "mic"
    assert getPret(updated_object) == 15
    assert getLocatie(updated_object) == "compas"
    out_dated_object = getById("2", lista)
    assert getId(out_dated_object) == "2"
    assert getNume(out_dated_object) == "pix"
    assert getDescriere(out_dated_object) == "negru"
    assert getPret(out_dated_object) == 3
    assert getLocatie(out_dated_object) == "dm"
    lista = []
    lista = adaugaObiect("1", "caiet", "A4", 10, "mall", lista)
    lista = modificaObiect("3", "penar", "mic", 15, "compas", lista)
    out_dated_object = getById("1", lista)
    assert getId(out_dated_object) == "1"
    assert getNume(out_dated_object) == "caiet"
    assert getDescriere(out_dated_object) == "A4"
    assert getPret(out_dated_object) == 10
    assert getLocatie(out_dated_object) == "mall"


def testGetById():
    lista = []
    lista = adaugaObiect("1", "caiet", "A4", 10, "mall", lista)
    lista = adaugaObiect("2", "pix", "negru", 3, "dm", lista)
    assert getId(getById(2, lista)) == 2
    assert getNume(getById(2, lista)) == "pix"
    assert getDescriere(getById(2, lista)) == "negru"
    assert getPret(getById(2, lista)) == 3
    assert getLocatie(getById(2, lista)) == "dm"