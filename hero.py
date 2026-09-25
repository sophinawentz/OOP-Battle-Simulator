import random

class Hero:
    """The hero blueprint will be implemented later in the project."""
    def __init__(self, name): #Name will come from the code creating the hero
        self.name = name #Should be differerent for each hero
        self.health = 120 #Everyone hero will have 120 health
        self.attack_power = 20

    def attack(self): 
        return  random.randint(1, self.attack_power)

    def take_damage(self, damage):
        self.health = self.health - damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    
