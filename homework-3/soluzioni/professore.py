from mago import Mago

class Professore(Mago):

    """
    Questa classe rappresenta un professore di Hogwarts
    
    Gli attributi principali che la caratterizzano sono:
    - nome del professore           (classe Mago)
    - cognome del professore        (classe Mago)
    - materia insegnata dal professore
    Tutti questi attributi sono privati e non possono essere modificati dall'esterno

    I metodi principali sono:
    - Aggiungi punti allo studente
    - Togli punti allo studente
    - Assegna voto ai GUFO

    Class methods da implementare sono:
    - get_all_professori
    
    """

    def __init__(self, name: str, surname: str, materia:str) -> None:
        super().__init__(name, surname)
        self.__materia = materia

    def __repr__(self) -> str:
        return f"Professore(name = '{self.name}', surname = '{self.surname}', materia = '{self.__materia}')"
    
    def __str__(self) -> str:
        return f"Professore {self.name} {self.surname} che insegna {self.__materia}"
    
    @property
    def materia(self):
        return self.__materia
    
    def aggiungi_punti(self, studente, punti):
        studente.punti += punti

    def togli_punti(self, studente, punti):
        studente.punti -= punti

    def assegna_voto_gufo(self, studente, voto):
        studente.gufo = voto

    @classmethod
    def get_all_professori(cls):
        return cls.get_all_maghi()