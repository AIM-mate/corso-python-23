"""
Qui andremo ad unire tutte le classi scritte negli altri file

in fondo al file troverete una funzione di test per controllare che tutto stia funzionando

"""

from studente import Studente
from professore import Professore
from casa import Casa

if __name__ == "__main__":

    piton = Professore("Severus", "Piton", "Pozioni")
    silente = Professore("Albus", "Silente", "Difesa contro le arti oscure")
    mcGranitt = Professore("Minerva", "McGranitt", "Trasfigurazione")

    print("Inizio test")

    print("Test 0: Creazione delle case di Hogwarts")
    grifondoro = Casa("Grifondoro")
    serpeverde = Casa("Serpeverde")
    tassorosso = Casa("Tassorosso")
    corvonero = Casa("Corvonero")
    print(Casa.get_all_case())

    print("Test 1: Creazione degli studenti")
    harry = Studente("Harry", "Potter", "Grifondoro", 0, "NC")
    draco = Studente("Draco", "Malfoy", "Serpeverde", 0, "NC")
    hermione = Studente("Hermione", "Granger", "Grifondoro", 0, "NC")
    ron = Studente("Ron", "Weasley", "Grifondoro", 0, "NC")
    print(Studente.get_all_studenti())

    print("Test 2: Aggiunta degli studenti alle case")
    grifondoro.aggiungi_studente(harry)
    serpeverde.aggiungi_studente(draco)
    grifondoro.aggiungi_studente(hermione)
    grifondoro.aggiungi_studente(ron)
    print("Studenti in grifondoro")
    print(grifondoro.elenca_studenti())
    print("Studenti in serpeverde")
    print(serpeverde.elenca_studenti())
    print("Studenti in tassorosso")
    print(tassorosso.elenca_studenti())
    print("Studenti in corvonero")
    print(corvonero.elenca_studenti())



