from Logic.CRUD import adaugaObiect
from Tests.testAll import runAllTests
from UI.console import runMenu



def main():
    runAllTests()
    lista = []
    lista = adaugaObiect("1", "caiet", "A4", 10, "mall", lista)
    lista = adaugaObiect("2", "pix", "negru", 3, "dm", lista)

    runMenu(lista)

main()
