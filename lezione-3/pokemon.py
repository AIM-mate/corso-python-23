import csv

class Pokemon:
    __all_pokemons = []

    def __init__(self, name: str, pokemon_type: str, hp: int, base_attack_strength: int):
        self.__name = name
        self.__hp = hp
        self.__pokemon_type = pokemon_type
        self.__base_attack_strength = base_attack_strength

        Pokemon.__all_pokemons.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty.")
        self.__name = value

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp = value

    @property
    def base_attack_strength(self):
        return self.__base_attack_strength

    @base_attack_strength.setter
    def base_attack_strength(self, value):
        if value <= 0:
            raise ValueError("Base attack strength must be greater than 0.")
        self.__base_attack_strength = value

    def base_attack(self, other):
        dmg = self.base_attack_strength
        other.receive_attack(dmg)

    def receive_attack(self, damage):
        if damage > 0:
            self.hp -= damage
            if self.hp <= 0:
                self.die()
    
    def die(self):
        Pokemon.__all_pokemons.remove(self)

    @classmethod
    def get_all(cls):
        return cls.__all_pokemons

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', hp={self.hp}, attack={self.base_attack_strength})"

    def __str__(self):
        return f"{self.name} ({self.__pokemon_type}): \n" + disegna_pokemon(self.name)


def disegna_pokemon(name):
    fileName = "PokemonArt"
    image = R""" """
    file = open(f"{fileName}.txt", "r")
    text = file.readlines()
    add = False
    for line in text:
        if(line.strip() == name):
            add = True
        elif(add):
            if(line.strip() == "STOP"):
                return image
            else:
                image += line.rstrip()
                image += """\n"""
    return "Immagine non Trovata"