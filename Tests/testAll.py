from Tests.testCRUD import testAdaugaObiect, testModificaObiect, testGetById, testStergeObiect
from Tests.testDomeniu import testObiect
from Tests.testFunctionalitati import testModificareLocatie, testModificareDescriere, testPretMaximLocatie, \
    testOrdonareCrescatorDupaPret, testSumaPreturilorPtFiecareLocatie
from Tests.testUndoAndRedo import testUndoAndRedo


def runAllTests():
    testObiect()
    testAdaugaObiect()
    testStergeObiect()
    testModificaObiect()
    testGetById()
    testModificareLocatie()
    testModificareDescriere()
    testPretMaximLocatie()
    testOrdonareCrescatorDupaPret()
    testSumaPreturilorPtFiecareLocatie()
    testUndoAndRedo()