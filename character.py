class Character:
    def __init__(self, *args):
        # JSON data object
        if len(args) == 1:
            self.name = args[0]['name']
            self.damage = args[0]['damage']
            self.health = args[0]['health']
            self.accuracy = args[0]['accuracy']

    def __str__(self):
        return f"{self.name}: Damage={self.damage} Health={self.health} Accuracy={self.accuracy}"

    def __repr__(self):
        return f"[{self.name}: Damage={self.damage} Health={self.health} Accuracy={self.accuracy}]"
