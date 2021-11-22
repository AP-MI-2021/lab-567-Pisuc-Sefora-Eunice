from Logic.CRUD import adaugaObiect
from Tests.testAll import runAllTests
from UI.command_line_console import runMenuCommandLine
from UI.console import runMenu


def main():
    runAllTests()
    lista = []
    lista = adaugaObiect("1", "caiet", "A4", 10, "mall", lista)
    lista = adaugaObiect("2", "pix", "negru", 3, "dm", lista)
    runUi(lista)

def runUi(lista):
    while True == True:
        print("1. Console menu.")
        print("2. Command line menu.")
        print("x. Iesire")
        tip_meniu = input("Alege tip meniu: ")
        if tip_meniu == "1":
            runMenu(lista)
        elif tip_meniu == "2":
            runMenuCommandLine(lista)
        else:
            break


main()
