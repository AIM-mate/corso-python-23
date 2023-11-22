from mago import Mago

class Studente(Mago):

    """
    Questa è la classe che descrive la un studente di Hogwarts
    Deriva dalla classe Mago che descrive un mago generico

    Gli attributi principali che la caratterizzano sono:
    - nome dello studente       (classe Mago)
    - cognome dello studente    (classe Mago)
    - casa dello studente
    - punti dello studente
    - voto preso ai gufo dello studente (default = "NC")
    è importante che questi valori non possano essere modificati dall'esterno
    sarà necessario quindi creare dei metodi getter per tutti 
    e setter per gli attributi punti e voto gufo

    I seguenti dunder methods sono stati implementati:
    - __repr__
    - __str__

    I metodi principali sono:

 
    Un class method da implementare è:
    - get_all_studenti

    """

    __studenti_Hogwarts = []

    __possibili_case = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    __voti_possibili_gufo = ["NC", "T", "D", "S", "OOP", "E"]

    def __init__(self, name : str, surname : str, casa : str, punti : int, gufo : str = "NC") -> None:
        
        assert casa in Studente.__possibili_case, f"La casa {casa} non è una casa di Hogwarts"
        assert gufo in Studente.__voti_possibili_gufo, f"Il voto {gufo} non è un voto valido per i gufo"
        
        super().__init__(name, surname)
        self.__casa = casa
        self.__punti = punti
        self.__gufo = gufo

        Studente.__studenti_Hogwarts.append(self)

    def __repr__(self) -> str:
        return f"Studente(name = '{self.__name}', surname = '{self.__surname}', house = '{self.__casa}', points = {self.__punti}, gufo = '{self.__gufo}')"
    
    def __str__(self) -> str:

        if self.__name == "Harry" and self.__surname == "Potter":
            return "Ma è Harry Potter!"

        return f"Studente {self.__name} {self.__surname} from {self.__casa} with {self.__punti} points and {self.__gufo} GUFO mark"
    
    @property
    def house(self):
        return self.__casa
    
    @property
    def punti(self):
        return self.__punti
    
    @property
    def gufo(self):
        return self.__gufo
    
    @punti.setter
    def punti(self, value):
        # TODO fix this with professor assert
        self.__punti = value

    @gufo.setter
    def gufo(self, value):
        assert value in Studente.__voti_possibili_gufo, f"Il voto {value} non è un voto valido per i gufo"
        self.__gufo = value
    
    @classmethod
    def get_all_studenti(cls):
        return cls.__studenti_Hogwarts