# Loome klassi nimega Fruit
class Fruit:

    # Konstruktor, mis võtab vastu PARAMEETRID: name ja clr
    def __init__(self, name, clr):
        # Salvestame parameetri name objekti atribuuti name
        self.name = name

        # Salvestame parameetri clr objekti atribuuti colour
        self.colour = clr


# Loome objekti nimega apple
# "apple" ja "red" on ARGUMENDID,
# mis antakse konstruktorile __init__
apple = Fruit("apple", "red")
banana = Fruit("banana", "yellow")