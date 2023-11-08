from pokemon import Pokemon

class FirePokemon(Pokemon):
    special_attack_strength = 8
    fire_defense = 2
    water_defense = -5
    grass_defense = 5

    def __init__(self, name, hp, base_attack_strength):
        super().__init__(name, "Fire", hp, base_attack_strength)

    def special_attack(self, other):
        if isinstance(other, GrassPokemon):
            print("It's super effective!")
        elif isinstance(other, WaterPokemon):
            print("It's not very effective...")
        damage = self.special_attack_strength - other.fire_defense
        other.receive_attack(damage)


class WaterPokemon(Pokemon):
    special_attack_strength = 8
    fire_defense = 5
    water_defense = 2
    grass_defense = -5

    def __init__(self, name, hp, base_attack_strength):
        super().__init__(name, "Water", hp, base_attack_strength)
        
    def special_attack(self, other):
        if isinstance(other, FirePokemon):
            print("It's super effective!")
        elif isinstance(other, GrassPokemon):
            print("It's not very effective...")
        damage = self.special_attack_strength - other.water_defense
        other.receive_attack(damage)


class GrassPokemon(Pokemon):
    special_attack_strength = 8
    fire_defense = -5
    water_defense = 5
    grass_defense = 2

    def __init__(self, name, hp, base_attack_strength):
        super().__init__(name, "Grass", hp, base_attack_strength)

    def special_attack(self, other):
        if isinstance(other, WaterPokemon):
            print("It's super effective!")
        elif isinstance(other, FirePokemon):
            print("It's not very effective...")
        damage = self.special_attack_strength - other.grass_defense
        other.receive_attack(damage)
