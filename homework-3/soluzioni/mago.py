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

    def __init__(self, nome : str, cognome : str) -> None:
        self.__nome = nome
        self.__cognome = cognome
        self.__patronus = Mago.__possibili_patronus[hash(nome) % len(Mago.__possibili_patronus)]

        Mago.__maghi_Hogwarts.append(self)

    def __repr__(self) -> str:
        return f"Mago(nome = '{self.__nome}', cognome = '{self.__cognome}')"
    
    def __str__(self) -> str:
        return f"Mago {self.__nome} {self.__cognome} che ha come patronus {self.__patronus}"
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def cognome(self):
        return self.__cognome
    
    @property
    def patronus(self):
        return self.__patronus
    
    @classmethod
    def get_all_maghi(cls):
        return cls.__maghi_Hogwarts