"""
Qui andremo ad unire tutte le classi scritte negli altri file

in fondo al file troverete una funzione di test per controllare che tutto stia funzionando

"""
# %%
from studente import Studente
from casa import Casa

if __name__ == "__main__":

    print("Inizio test")

    print("\n \nTest 0: Creazione delle case di Hogwarts")
    grifondoro = Casa("Grifondoro")
    serpeverde = Casa("Serpeverde")
    try:
        politecnico = Casa("Politecnico")
    except AssertionError as e:
        print(e)
    for casa in Casa.get_all_case():
        print(casa)

    print("\n \nTest 1: Creazione degli studenti")
    harry = Studente("Harry", "Potter", "Grifondoro", 0, 0, "NC")
    draco = Studente("Draco", "Malfoy", "Serpeverde", 0, 0, "NC")
    hermione = Studente("Hermione", "Granger", "Grifondoro", 0, 0, "NC")
    ron = Studente("Ron", "Weasley", "Grifondoro", 0, 0, "NC")
    try:
        studente_sbagliato = Studente("Studente", "Sbagliato", "Politecnico", 0, 0, "NC")
    except AssertionError as e:
        print(e)
    for studente in Studente.get_all_studenti():
        print(studente)

    print("\n \nTest 2: Aggiunta degli studenti alle case")
    grifondoro.aggiungi_studente(harry)
    serpeverde.aggiungi_studente(draco)
    grifondoro.aggiungi_studente(hermione)
    grifondoro.aggiungi_studente(ron)
    print("Studenti in Grifondoro")
    grifondoro.elenca_studenti()
    print("Studenti in Gerpeverde")
    serpeverde.elenca_studenti()

    print("\n \nTest 3: Assegnazione dei punti")
    harry.andare_a_lezione()
    harry.giocare_a_quidditch()
    harry.giocare_a_quidditch()
    draco.giocare_a_quidditch()
    hermione.andare_a_lezione()
    hermione.andare_a_lezione()
    hermione.andare_a_lezione()
    hermione.andare_a_lezione()
    try:
        ron.punti = 100
    except AttributeError as e:
        print(e)
    print(f"Harry ha {harry.punti} punti")
    print(f"Draco ha {draco.punti} punti")
    print(f"Hermione ha {hermione.punti} punti")
    print(f"Ron ha {ron.punti} punti")


    print("\n \nTest 4: Assegnazione dei voti")
    Studente.giorno_dei_gufo()
    print(f"Harry ha preso {harry.gufo} nei G.U.F.O.")
    print(f"Draco ha preso {draco.gufo} nei G.U.F.O.")
    print(f"Hermione ha preso {hermione.gufo} nei G.U.F.O.")
    print(f"Ron ha preso {ron.gufo} nei G.U.F.O.")
    try:
        ron.gufo = "E"
    except AttributeError as e:
        print(e)


    print("\n \nTest 5: Calcolo dei punti")
    print(f"Grifondoro ha {grifondoro.calcola_punti()} punti")
    print(f"Serpeverde ha {serpeverde.calcola_punti()} punti")

    print("\n \nTest 6: Casa vincitrice")
    print(f"La casa vincitrice è {Casa.casa_vincitrice().nome}")






# %%
