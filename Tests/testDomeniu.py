from Domain import obiect
from Domain.obiect import creeazaObiect, getId, getNume, getDescriere, getPret, getLocatie


def testObiect():
    obiect = creeazaObiect("1", "caiet", "A4", 10, "mall")

    assert getId(obiect) == "1"
    assert getNume(obiect) == "caiet"
    assert getDescriere(obiect) == "A4"
    assert getPret(obiect) == 10
    assert getLocatie(obiect) == "mall"