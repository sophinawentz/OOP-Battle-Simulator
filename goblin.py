import random
from enemy import enemy



class Goblin(Enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        super().__init__(name, 100, 7)
        self.gold = 0

    def stealGold(self, hero):
        print("Gimmie da bread")
        self.gold = self.gold + hero.gold
        hero.gold = 0
        print("Get hah")
        