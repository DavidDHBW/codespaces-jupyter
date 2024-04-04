from inventory import Inventory
#todo write player class
class Player:
    def __init__(self, name, enemy):
        self.name = name
        self.enemy = enemy
        self.inventory = Inventory()
    