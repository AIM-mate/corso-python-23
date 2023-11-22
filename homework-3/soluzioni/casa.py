class Casa():

    """
    Questa è la classe che descrive la una casa di Hogwarts

    Gli attributi principali che la caratterizzano sono:
    - nome della casa
    - punti della casa
    - studenti della casa

    I metodi principali sono:
    - aggiungi_studente
    - calcola_punti
    - elenca_studenti
    - elenca_professori


    Un class method da implementare è:
    - get_all_case
    - casa vincitrice

    """

    __case_Hogwats = []

    case_possibili = ["Grifondoro", "Serpeverde", "Tassorosso", "Corvonero"]

    def __init__(self, nome : str, punti=0, studenti=[], professori=[]) -> None:
        
        assert nome in Casa.case_possibili, f"La casa {nome} non è una casa di Hogwarts"

        self.__nome = nome
        self.__punti = punti
        self.__studenti = studenti
        self.__professori = professori

        Casa.__case_Hogwats.append(self)

    def __str__(self) -> str:
        return f"Casa {self.__nome} con {self.__punti} punti"
    
    def __repr__(self) -> str:
        return f"Casa(nome = '{self.__nome}', punti = {self.__punti}, studenti = {self.__studenti}, professori = {self.__professori})"
    
    def aggiungi_studente(self, studente):
        self.__studenti.append(studente)

    def calcola_punti(self):
        self.__punti = 0
        for studente in self.__studenti:
            self.__punti += studente.punti
        return self.__punti
    
    def elenca_studenti(self):
        for studente in self.__studenti:
            print(studente)

    def elenca_professori(self):
        for professore in self.__professori:
            print(professore)

    @classmethod
    def get_all_case(cls):
        return cls.__case_Hogwats

    @classmethod
    def casa_vincitrice(cls):

        if len(cls.__case_Hogwats) == 0:
            return "Non ci sono case di Hogwarts"

        casa_vincitrice = cls.__case_Hogwats[0]
        for casa in cls.__case_Hogwats:
            if casa.calcola_punti() > casa_vincitrice.calcola_punti():
                casa_vincitrice = casa
        return casa_vincitrice



