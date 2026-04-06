# Loome klassi nimega Fruit
class Fruit:

    # Konstruktor, mis käivitatakse automaatselt objekti loomisel
    def __init__(self):
        # Objekti atribuut name (puuvilja nimi), vaikimisi "apple"
        self.name = "apple"

        # Objekti atribuut colour (puuvilja värv), vaikimisi "red"
        self.colour = "red"


# Loome objekti my_fruit klassist Fruit
my_fruit = Fruit()

# Muudame objekti my_fruit värvi
# Algne väärtus oli "red", nüüd on "green"
my_fruit.colour = "green"

# Muudame objekti my_fruit nime
# Algne väärtus oli "apple", nüüd on "kiwi"
my_fruit.name = "kiwi"

# Trükime objekti my_fruit värvi
print(my_fruit.colour)

# Trükime objekti my_fruit nime
print(my_fruit.name)
