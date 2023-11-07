class Battle:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def run(self):
        print(f"A battle starts between {self.pokemon1.name} and {self.pokemon2.name}!")

        while self.pokemon1.hp > 0 and self.pokemon2.hp > 0:
            # Pokemon 1's turn
            self.turn(self.pokemon1, self.pokemon2)
            if self.pokemon2.hp <= 0:
                print(f"{self.pokemon2.name} has been defeated! {self.pokemon1.name} wins the battle!")
                print(self.pokemon1)
                break

            # Pokemon 2's turn
            self.turn(self.pokemon2, self.pokemon1)
            if self.pokemon1.hp <= 0:
                print(f"{self.pokemon1.name} has been defeated! {self.pokemon2.name} wins the battle!")
                print(self.pokemon2)
                break

    def turn(self, attacker, defender):
        # Get user input for attack choice
        choice = input(f"{attacker.name}, do you want to use a (1) base attack or (2) special attack? Enter 1 or 2: ")
        
        if choice == "1":
            attacker.base_attack(defender)
            print(f"{attacker.name} attacks {defender.name} with a base attack! {defender.name} now has {defender.hp} HP.")
        elif choice == "2":
            attacker.special_attack(defender)
            print(f"{attacker.name} uses a special attack on {defender.name}! {defender.name} now has {defender.hp} HP.")
        else:
            print("Invalid choice, lost your turn!")