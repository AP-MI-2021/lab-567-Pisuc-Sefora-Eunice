from Logic.CRUD import adaugaObiect, getById
from UI.console import uiUndo, uiRedo, uiAdaugareObiecte


def testUndoAndRedo():
    lista = []
    undo_list = []
    redo_list = []

    # adaugam un obiect
    lista = uiAdaugareObiecte("1", "ceas", "roz", 15, "market", lista, undo_list, redo_list)
    assert len(lista) == 1
    # adaugam un obiect
    lista = uiAdaugareObiecte("2", "creion", "albastru", 2, "compas", lista, undo_list, redo_list)
    assert len(lista) == 2
    # adaugam un obiect
    lista = uiAdaugareObiecte("3", "agenda", "mica", 8, "dm", lista, undo_list, redo_list)
    assert len(lista) == 3

    # undo
    lista = uiUndo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert getById("3", lista) is None
    assert getById("2", lista) is not None
    assert getById("1", lista) is not None

    # undo
    lista = uiUndo(lista, undo_list, redo_list)
    assert len(lista) == 1
    assert getById("2", lista) is None
    assert getById("1", lista) is not None

    # undo
    lista = uiUndo(lista, undo_list, redo_list)
    assert len(lista) == 0
    assert getById("1", lista) is None

    # undo
    assert len(lista) == 0

    # adaugam 3 cheltuieli
    lista = uiAdaugareObiecte("1", "ceas", "roz", 15, "market", lista, undo_list, redo_list)
    lista = uiAdaugareObiecte("2", "creion", "albastru", 2, "compas", lista, undo_list, redo_list)
    lista = uiAdaugareObiecte("3", "agenda", "mica", 8, "dm", lista, undo_list, redo_list)
    assert len(lista) == 3

    # redo
    lista = uiRedo(lista, undo_list, redo_list)
    assert len(lista) == 3
    assert getById("1", lista) is not None
    assert getById("2", lista) is not None
    assert getById("3", lista) is not None

    # undo undo
    lista = uiUndo(lista, undo_list, redo_list)
    lista = uiUndo(lista, undo_list, redo_list)
    assert len(lista) == 1
    assert getById("2", lista) is None
    assert getById("3", lista) is None
    assert getById("1", lista) is not None

    # redo
    lista = uiRedo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert getById("3", lista) is None
    assert getById("2", lista) is not None
    assert getById("1", lista) is not None

    # redo
    lista = uiRedo(lista, undo_list, redo_list)
    assert len(lista) == 3
    assert getById("1", lista) is not None
    assert getById("2", lista) is not None
    assert getById("3", lista) is not None

    # undo undo
    lista = uiUndo(lista, undo_list, redo_list)
    lista = uiUndo(lista, undo_list, redo_list)
    assert len(lista) == 1
    assert getById("3", lista) is None
    assert getById("2", lista) is None
    assert getById("1", lista) is not None

    # adaugam un obiect
    lista = uiAdaugareObiecte("4", "husa", "roz", 45, "altex", lista, undo_list, redo_list)
    assert len(lista) == 2
    assert getById("1", lista) is not None
    assert getById("2", lista) is None
    assert getById("3", lista) is None
    assert getById("4", lista) is not None

    # redo
    lista = uiRedo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert getById("1", lista) is not None
    assert getById("2", lista) is None
    assert getById("3", lista) is None
    assert getById("4", lista) is not None

    # undo
    lista = uiUndo(lista, undo_list, redo_list)
    assert len(lista) == 1
    assert getById("1", lista) is not None
    assert getById("4", lista) is None

    # undo
    lista = uiUndo(lista, undo_list, redo_list)
    assert len(lista) == 0
    assert getById("1", lista) is None

    # redo redo
    lista = uiRedo(lista, undo_list, redo_list)
    lista = uiRedo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert getById("1", lista) is not None
    assert getById("4", lista) is not None

    # redo
    lista = uiRedo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert getById("1", lista) is not None
    assert getById("4", lista) is not None
    assert getById("2", lista) is None
    assert getById("3", lista) is None




