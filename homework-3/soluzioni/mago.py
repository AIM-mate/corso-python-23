class Mago():

    """
    Questa classe rappresenta un mago di Hogwarts
    
    Gli attributi principali che la caratterizzano sono:
    - nome del mago
    - cognome del mago
    - patronus del mago         (viene scelto di default nella classe)
    Tutti questi attributi sono privati e non possono essere modificati dall'esterno
    Sarà necessario quindi creare dei metodi getter per tutti 
    Ma nessun setter

    Per questa classe non definiamo nessun metodo particolare

    Class methods da implementare sono:
    - get_all_maghi

    """

    __possibili_patronus = ["Cervo", "Volpe", "Lupo", "Gatto", "Cane", "Cavallo", "Fenice", "Lepre", "Orso", "Tasso", "Tigre", "Topo", "Unicorno", "Leone", "Serpente", "Tartaruga", "Aquila"]
    __maghi_Hogwarts = []

    def __init__(self, name : str, surname : str) -> None:
        self.__name = name
        self.__surname = surname
        self.__patronus = Mago.__possibili_patronus[hash(name) % len(Mago.__possibili_patronus)]

        Mago.__maghi_Hogwarts.append(self)

    def __repr__(self) -> str:
        return f"Mago(name = '{self.__name}', surname = '{self.__surname}')"
    
    def __str__(self) -> str:
        return f"Mago {self.__name} {self.__surname} with patronus {self.__patronus}"
    
    @property
    def name(self):
        return self.__name
    
    @property
    def surname(self):
        return self.__surname
    
    @property
    def patronus(self):
        return self.__patronus
    
    @classmethod
    def get_all_maghi(cls):
        return cls.__maghi_Hogwarts