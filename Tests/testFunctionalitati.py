from Domain.obiect import getId, getLocatie
from Logic.CRUD import adaugaObiect
from Logic.functionalitati import pretMaximLocatie, ordonareCrescatorDupaPret, modificareLocatie, modificareDescriere, \
    sumaPreturilorPtFiecareLocatie


def testModificareLocatie():
    lista = []
    lista = adaugaObiect("1", "caiet", "A4", 10, "mall", lista)
    lista = adaugaObiect("2", "pix", "negru", 3, "dm", lista)
    lista = adaugaObiect("3", "penar", "mic", 15, "mall", lista)

    lista = modificareLocatie(lista, "market")
    assert getLocatie(lista[0]) == "market"
    assert getLocatie(lista[1]) == "market"
    assert getLocatie(lista[2]) == "market"

def testModificareDescriere():
    lista = []
    lista = adaugaObiect("1", "caiet", "A4", 10, "mall", lista)
    lista = adaugaObiect("2", "pix", "negru", 3, "dm", lista)
    lista = adaugaObiect("3", "penar", "mic", 15, "mall", lista)

    mod = modificareDescriere(lista, "descriere", 6)

    assert len(mod) == 3
    assert mod[0][2] == "A4 descriere"
    assert mod[2][2] == "mic descriere"


def testPretMaximLocatie():
    lista = []
    lista = adaugaObiect("1", "caiet", "A4", 10, "mall", lista)
    lista = adaugaObiect("2", "pix", "negru", 3, "dm", lista)
    lista = adaugaObiect("3", "penar", "mic", 15, "mall", lista)

    dict = pretMaximLocatie(lista)

    assert len(dict) == 2
    assert dict["mall"] == 15
    assert dict["dm"] == 3

def testOrdonareCrescatorDupaPret():
    lista = []
    lista = adaugaObiect("1", "caiet", "A4", 10, "mall", lista)
    lista = adaugaObiect("2", "pix", "negru", 3, "dm", lista)
    lista = adaugaObiect("3", "penar", "mic", 15, "mall", lista)
    s_lista = ordonareCrescatorDupaPret(lista)

    assert getId(s_lista[0]) == "2"
    assert getId(s_lista[1]) == "1"
    assert getId(s_lista[2]) == "3"

def testSumaPreturilorPtFiecareLocatie():
    lista = []
    lista = adaugaObiect("1", "caiet", "A4", 10, "mall", lista)
    lista = adaugaObiect("2", "pix", "negru", 3, "dm", lista)
    lista = adaugaObiect("3", "penar", "mic", 15, "mall", lista)

    sum = sumaPreturilorPtFiecareLocatie(lista)

    assert len(sum) == 2
    assert sum["mall"] == 25
    assert sum["dm"] == 3





