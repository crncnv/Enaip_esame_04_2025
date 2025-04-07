import pytest
from progetto.modulo1 import funzione_doppio, funzione_quadrato, ClasseParzialmenteImplementata

def test_funzione_doppio():
    # TODO Aggiungere 2 o più test per coprire funzione_doppio
    assert funzione_doppio(4) == 8
    assert funzione_doppio(-5) == -10

def test_funzione_quadrato():
    # TODO Aggiungere 2 o più test per coprire funzione_quadrato
    assert funzione_quadrato(4) == 16
    assert funzione_quadrato(-5) == 25

def test_metodo_esistente_classe():
    istanza = ClasseParzialmenteImplementata("Test")
    assert istanza.metodo_esistente() == "Ciao, sono Test!"

def test_metodo_da_completare_classe():
    istanza = ClasseParzialmenteImplementata("Test")
    istanza.metodo_da_completare("Thomas") == "Test Thomas"
    # TODO: Aggiungere un'asserzione per verificare il comportamento del metodo
    