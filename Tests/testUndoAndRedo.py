from Logic.CRUD import adaugaObiect, getById


def testUndoAndRedo():
    lista = []
    undo_list = []
    redo_list = []

    # adaugam un obiect
    lista = adaugaObiect("1, ceas, roz, 15, market", lista, undo_list, redo_list)
    assert len(lista) == 1
    # adaugam un obiect
    lista = adaugaObiect("2, creion, albastru, 2, compas", lista, undo_list, redo_list)
    assert len(lista) == 2
    # adaugam un obiect
    lista = adaugaObiect("3, agenda, mica, 8, dm", lista, undo_list, redo_list)
    assert len(lista) == 3

    # undo
    lista = uiUndo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert getById(3, lista) is None
    assert getById(2, lista) is not None
    assert getById(1, lista) is not None

    # undo
    lista = uiUndo(lista, undo_list, redo_list)
    assert len(lista) == 1
    assert getById(2, lista) is None
    assert getById(1, lista) is not None

    # undo
    lista = uiUndo(lista, undo_list, redo_list)
    assert len(lista) == 0
    assert getById(1, lista) is not None

    # undo
    assert len(lista) == 0

    # adaugam 3 cheltuieli
    lista = adaugaObiect("1, ceas, roz, 15, market", lista, undo_list, redo_list)
    lista = adaugaObiect("2, creion, albastru, 2, compas", lista, undo_list, redo_list)
    lista = adaugaObiect("3, agenda, mica, 8, dm", lista, undo_list, redo_list)
    assert len(lista) == 3

    # redo
    lista = ui_redo(lista, undo_list, redo_list)
    assert len(lista) == 3
    assert getById(1, lista) is not None
    assert getById(2, lista) is not None
    assert getById(3, lista) is not None

    # undo undo
    lista = ui_undo(lista, undo_list, redo_list)
    lista = ui_undo(lista, undo_list, redo_list)
    assert len(lista) == 1
    assert getById(2, lista) is None
    assert getById(3, lista) is None
    assert getById(1, lista) is not None

    # redo
    lista = ui_redo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert getById(3, lista) is None
    assert getById(2, lista) is not None
    assert getById(1, lista) is not None

    # redo
    lista = ui_redo(lista, undo_list, redo_list)
    assert len(lista) == 3
    assert getById(1, lista) is not None
    assert getById(2, lista) is not None
    assert getById(3, lista) is not None

    # undo undo
    lista = ui_undo(lista, undo_list, redo_list)
    lista = ui_undo(lista, undo_list, redo_list)
    assert len(lista) == 1
    assert getById(3, lista) is None
    assert getById(2, lista) is None
    assert getById(1, lista) is not None

    # adaugam un obiect
    lista = adaugaObiect("4, husa, roz, 45, altex", lista, undo_list, redo_list)
    assert len(lista) == 2
    assert getById(1, lista) is not None
    assert getById(2, lista) is None
    assert getById(3, lista) is None
    assert getById(4, lista) is not None

    # redo
    lista = ui_redo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert getById(1, lista) is not None
    assert getById(2, lista) is None
    assert getById(3, lista) is None
    assert getById(4, lista) is not None

    # undo
    lista = ui_undo(lista, undo_list, redo_list)
    assert len(lista) == 1
    assert getById(1, lista) is not None
    assert getById(4, lista) is None

    # undo
    lista = ui_undo(lista, undo_list, redo_list)
    assert len(lista) == 0
    assert getById(1, lista) is None

    # redo redo
    lista = ui_redo(lista, undo_list, redo_list)
    lista = ui_redo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert getById(1, lista) is not None
    assert getById(4, lista) is not None

    # redo
    lista = ui_redo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert getById(1, lista) is not None
    assert getById(4, lista) is not None
    assert getById(2, lista) is None
    assert getById(3, lista) is None




