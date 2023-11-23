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
            se le lezioni sono 0 il voto è T
            se le lezioni sono 1 il voto è D
            se le lezioni sono 2 il voto è S
            se le lezioni sono 3 il voto è OOP
            se le lezioni sono 4 il voto è E

    """


    def __init__(self, nome : str, cognome : str, casa : str, punti : int, lezioni :int = 0, gufo : str = "NC") -> None:
        pass

    def __repr__(self) -> str:
        return f"Studente(nome = '{self.nome}', cognome = '{self.cognome}', casa = '{self.__casa}', punti = {self.__punti}, lezioni = {self.__lezioni}, gufo = '{self.__gufo}')"
    
    def __str__(self) -> str:

        if self.nome == "Harry" and self.cognome == "Potter":
            return "Ma è Harry Potter!"

        return f"Studente {self.nome} {self.cognome} della casa {self.__casa} con {self.__punti} punti, ha seguito {self.__lezioni} lezioni e ha preso {self.__gufo} ai GUFO"
    
    