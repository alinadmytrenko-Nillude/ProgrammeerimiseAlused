# Loome klassi nimega Fruit
class Fruit:

    # Konstruktor, mis saab kaks parameetrit: name ja clr
    def __init__(self, name, clr):
        # Salvestame puuvilja nime objekti atribuuti
        self.name = name

        # Salvestame puuvilja värvi objekti atribuuti
        self.colour = clr
)
    # Meetod, mis kuvab objekti andmed
    def details(self):
        exp_date = datetime.today()
        # Trükib lause, kasutades objekti atribuute
        print("my " + self.name + " is " + self.colour)


# Loome objekti apple klassist Fruit
apple = Fruit("apple", "red")

# Kutsume välja objekti apple meetodi details()
apple.details()
