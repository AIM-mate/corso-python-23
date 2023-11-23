"""
Qui andremo ad unire tutte le classi scritte negli altri file

in fondo al file troverete una funzione di test per controllare che tutto stia funzionando

"""
# %%
from studente import Studente
from casa import Casa

if __name__ == "__main__":

    print("Inizio test")

    print("Test 0: Creazione delle case di Hogwarts")
    grifondoro = Casa("Grifondoro")
    serpeverde = Casa("Serpeverde")
    print(Casa.get_all_case())

    print("Test 1: Creazione degli studenti")
    harry = Studente("Harry", "Potter", "Grifondoro", 0, 0, "NC")
    draco = Studente("Draco", "Malfoy", "Serpeverde", 0, 0, "NC")
    hermione = Studente("Hermione", "Granger", "Grifondoro", 0, 0, "NC")
    ron = Studente("Ron", "Weasley", "Grifondoro", 0, 0, "NC")
    print(Studente.get_all_studenti())

    print("Test 2: Aggiunta degli studenti alle case")
    grifondoro.aggiungi_studente(harry)
    serpeverde.aggiungi_studente(draco)
    grifondoro.aggiungi_studente(hermione)
    grifondoro.aggiungi_studente(ron)
    print("Studenti in grifondoro")
    grifondoro.elenca_studenti()
    print("Studenti in serpeverde")
    serpeverde.elenca_studenti()

    print("Test 3: Assegnazione dei punti")
    harry.andare_a_lezione()
    harry.giocare_a_quidditch()
    harry.giocare_a_quidditch()
    draco.giocare_a_quidditch()
    hermione.andare_a_lezione()
    hermione.andare_a_lezione()
    hermione.andare_a_lezione()
    hermione.andare_a_lezione()
    hermione.andare_a_lezione()


    print("Test 4: Assegnazione dei voti")
    Studente.giorno_dei_gufo()
    print(f"Harry ha preso {harry.gufo} nei G.U.F.O.")
    print(f"Draco ha preso {draco.gufo} nei G.U.F.O.")
    print(f"Hermione ha preso {hermione.gufo} nei G.U.F.O.")
    print(f"Ron ha preso {ron.gufo} nei G.U.F.O.")


    print("Test 4: Calcolo dei punti")
    print(f"Grifondoro ha {grifondoro.calcola_punti()} punti")
    print(f"Serpeverde ha {serpeverde.calcola_punti()} punti")

    print("Test 5: Casa vincitrice")
    print(f"La casa vincitrice è {Casa.casa_vincitrice().nome}")






# %%
