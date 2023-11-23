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

    

    def __init__(self, nome : str, punti=0, studenti=None) -> None:
        pass
        

    def __str__(self) -> str:
        return f"Questa è la casa {self.__nome}"
    
    def __repr__(self) -> str:
        return f"Casa(nome = '{self.__nome}', punti = {self.__punti}, studenti = {self.__studenti})"
    
    



