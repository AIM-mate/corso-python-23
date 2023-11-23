from mago import Mago

class Studente(Mago):

    """
    Questa è la classe che descrive la un studente di Hogwarts
    Deriva dalla classe Mago che descrive un mago generico

    Gli attributi principali che la caratterizzano sono:
    - nome dello studente       (classe Mago)
    - cognome dello studente    (classe Mago)
    - casa dello studente
    - punti dello studente              (default = 0)
    - lezioni seguite                   (default = 0)
    - voto preso ai gufo dello studente (default = "NC")
    è importante che questi valori non possano essere modificati dall'esterno
    sarà necessario quindi creare dei metodi getter per tutti 
    in questo caso non creeremo nessun setter perché punti e valutazione gufo
    saranno modificati solo da metodi interni alla classe

    I seguenti dunder methods sono stati implementati:
    - __repr__
    - __str__

    I metodi principali sono:
    - andare a lezione      (aggiunge 20 punti)
    - giocare a quidditch   (aggiunge 5 punti)
    

 
    I class method da implementare sono:
    - get_all_studenti
    - giorno_dei_gufo        (assegna a tutti voto il ai gufo in base al numero di lezioni seguite)
            se le lezioni sono 0 il voto è NC
            se le lezioni sono 1 il voto è T
            se le lezioni sono 2 il voto è D
            se le lezioni sono 3 il voto è S
            se le lezioni sono 4 il voto è OOP
            se le lezioni sono 5 il voto è E

    """

    __studenti_Hogwarts = []

    __possibili_case = ["Grifondoro", "Serpeverde", "Tassorosso", "Corvonero"]
    __voti_possibili_gufo = ["NC", "T", "D", "S", "OOP", "E"]

    def __init__(self, nome : str, cognome : str, casa : str, punti : int, lezioni :int = 0, gufo : str = "NC") -> None:
        
        assert casa in Studente.__possibili_case, f"La casa {casa} non è una casa di Hogwarts"
        assert gufo in Studente.__voti_possibili_gufo, f"Il voto {gufo} non è un voto valido per i gufo"
        
        super().__init__(nome, cognome)
        self.__casa = casa
        self.__punti = punti
        self.__lezioni = lezioni
        self.__gufo = gufo

        Studente.__studenti_Hogwarts.append(self)

    def __repr__(self) -> str:
        return f"Studente(nome = '{self.nome}', cognome = '{self.cognome}', casa = '{self.__casa}', punti = {self.__punti}, lezioni = {self.__lezioni}, gufo = '{self.__gufo}')"
    
    def __str__(self) -> str:

        if self.nome == "Harry" and self.cognome == "Potter":
            return "Ma è Harry Potter!"

        return f"Studente {self.nome} {self.cognome} della casa {self.__casa} con {self.__punti} punti, ha seguito {self.__lezioni} lezioni e ha preso {self.__gufo} ai GUFO"
    
    @property
    def casa(self):
        return self.__casa
    
    @property
    def punti(self):
        return self.__punti
    
    @property
    def gufo(self):
        return self.__gufo
    
    def andare_a_lezione(self):
        self.__lezioni += 1
        self.__punti += 20

    def giocare_a_quidditch(self):
        self.__punti += 5

    def __sostieni_esame(self):
        self.__gufo = Studente.__voti_possibili_gufo[self.__lezioni]


    @classmethod
    def get_all_studenti(cls):
        return cls.__studenti_Hogwarts

    @classmethod
    def giorno_dei_gufo(cls):
        for studente in cls.__studenti_Hogwarts:
            studente.__sostieni_esame()