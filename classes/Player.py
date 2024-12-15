class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.cards = []

    def __str__(self):
        return self.name + " with $" + str(self.money)