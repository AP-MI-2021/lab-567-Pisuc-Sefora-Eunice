from Domain.obiect import getId
from Logic.CRUD import adaugaObiect
from Logic.functionalitati import pretMaximLocatie, ordonareCrescatorDupaPret


def testPretMaximLocatie():
    lista = []
    lista = adaugaObiect("1", "caiet", "A4", 10, "mall", lista)
    lista = adaugaObiect("2", "pix", "negru", 3, "dm", lista)
    lista = adaugaObiect("3", "penar", "mic", 15, "mall", lista)

    dict = pretMaximLocatie(lista)

    assert len[dict] == 2
    assert dict[lista["mall"]] == 15
    assert dict[lista["dm"]] == 3

def testOrdonareCrescatorDupaPret():
    lista = []
    lista = adaugaObiect("1", "caiet", "A4", 10, "mall", lista)
    lista = adaugaObiect("2", "pix", "negru", 3, "dm", lista)
    lista = adaugaObiect("3", "penar", "mic", 15, "mall", lista)
    s_lista = ordonareCrescatorDupaPret(lista)

    assert getId(s_lista[0]) == "2"
    assert getId(s_lista[1]) == "1"
    assert getId(s_lista[2]) == "15"



