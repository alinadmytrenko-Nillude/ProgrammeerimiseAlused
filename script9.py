class Dog:
    def __init__(self, name, age): # Konstruktor – kutsutakse välja objekti loomisel
        self.name = name  # Salvestame koera nime eksemplari atribuudina
        self.age = age # kaitstud atribuut

    def get_name(self): # Meetod nime lugemiseks (getter)
        return self.name # Tagastame koera nime

    def get_age(self): # Meetod vanuse lugemiseks (getter)
        return self.age # Tagastame koera vanuse

    def set_age(self, age): # Meetod vanuse muutmiseks (setter)
        self.age = age # Uuendame koera vanust uue väärtusega

dog1_name = ["Tim", "Bill"]
dog1_age = [32, 14]