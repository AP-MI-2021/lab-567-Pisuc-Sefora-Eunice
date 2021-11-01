from Tests.testCRUD import testAdaugaObiect, testModificaObiect, testGetById, testStergeObiect
from Tests.testDomeniu import testObiect


def runAllTests():
    testObiect()
    testAdaugaObiect()
    testStergeObiect()
    testModificaObiect()
    testGetById()