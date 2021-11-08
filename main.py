from Logic.CRUD import adaugaObiect
from Tests.testAll import runAllTests
from UI.command_line_console import runMenuCommandLine
from UI.console import runMenu



def main():
    runAllTests()
    lista = []
    lista = adaugaObiect("1", "caiet", "A4", 10, "mall", lista)
    lista = adaugaObiect("2", "pix", "negru", 3, "dm", lista)
    print("1. Console menu.")
    print("2. Command line menu.")
    tip_meniu = input("Alege tip meniu: ")
    if tip_meniu == "1":
        runMenu(lista)
    else:
        runMenuCommandLine(lista)

main()
