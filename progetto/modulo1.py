def funzione_doppio(x):
    """Questa funzione restituisce il doppio del argomento passato alla funzione"""
    # TODO: Implementare la funzione per restituire il doppio di x
    return x*2

def funzione_quadrato(y):
    """
    Questa funzione dovrebbe prendere un numero e restituire il suo quadrato.
    Completa l'implementazione.
    """
    # TODO: Implementare la funzione per restituire il quadrato di y
    return y**2

class ClasseParzialmenteImplementata:
    def __init__(self, nome):
        self.nome = nome
        self.valore_interno = 13

    def metodo_esistente(self):
        return f"Ciao, sono {self.nome}!"

    def metodo_da_completare(self, valore:str):
        
        """
        Questo metodo dovrebbe aggiungere il 'valore' a un attributo interno
        e restituire il nuovo valore.
        """
        # TODO: Implementare l'aggiunta del valore e la restituzione
        return self.nome + valore
   