class Casa():

    """
    Questa è la classe che descrive la una casa di Hogwarts

    Gli attributi principali che la caratterizzano sono:
    - nome della casa
    - punti della casa
    - studenti della casa               (default = None)[!]

    I metodi principali sono:
    - aggiungi_studente
    - calcola_punti
    - elenca_studenti
    - elenca_professori


    Un class method da implementare è:
    - get_all_case
    - casa vincitrice

    """

    __case_Hogwarts = []
    __case_possibili = ["Grifondoro", "Serpeverde", "Tassorosso", "Corvonero"]

    def __init__(self, nome : str, punti=0, studenti=None) -> None:
        
        assert nome in Casa.__case_possibili, f"La casa {nome} non è una casa di Hogwarts"

        self.__nome = nome
        self.__punti = punti
        self.__studenti = studenti

        Casa.__case_Hogwarts.append(self)

    def __str__(self) -> str:
        return f"Questa è la casa {self.__nome}"
    
    def __repr__(self) -> str:
        return f"Casa(nome = '{self.__nome}', punti = {self.__punti}, studenti = {self.__studenti})"
    
    @property
    def nome(self):
        return self.__nome

    def aggiungi_studente(self, studente):
        if self.__studenti is None:
            self.__studenti = []
        self.__studenti.append(studente)    


    def calcola_punti(self):
        self.__punti = 0
        for studente in self.__studenti:
            self.__punti += studente.punti
        return self.__punti
    
    def elenca_studenti(self):
        for studente in self.__studenti:
            print(studente)

    @classmethod
    def get_all_case(cls):
        return cls.__case_Hogwarts

    @classmethod
    def casa_vincitrice(cls):

        if len(cls.__case_Hogwarts) == 0:
            return "Non ci sono case di Hogwarts"

        casa_vincitrice = cls.__case_Hogwarts[0]
        for casa in cls.__case_Hogwarts:
            if casa.calcola_punti() > casa_vincitrice.calcola_punti():
                casa_vincitrice = casa
        return casa_vincitrice



