# Loome klassi Person (inimese mall)
class Person:

    # Konstruktor, mis käivitatakse objekti loomisel
    def __init__(self, name, age):
        self.name = name    # salvestame inimese nime
        self.age = age      # salvestame inimese vanuse

    # Meetod, mis prindib inimese info
    def info(self):
        print("Nimi:", self.name)   # väljastame nime
        print("Vanus:", self.age)   # väljastame vanuse

    # Meetod, mis kontrollib, kas inimene on täiskasvanu
    def is_adult(self):
        if self.age >= 18:          # kui vanus on 18 või rohkem
            return True             # tagastame True
        else:
            return False            # muidu tagastame False


# Loome objekti p1 klassist Person
p1 = Person("Alex", 20)  # nimi Alex, vanus 20

# Loome objekti p2 klassist Person
p2 = Person("Bob", 15)   # nimi Bob, vanus 15

# Kutsume välja meetodi info objekti p1 jaoks
p1.info()

# Kontrollime, kas p1 on täiskasvanu
print(p1.is_adult())    # True

# Kutsume välja meetodi info objekti p2 jaoks
p2.info()

# Kontrollime, kas p2 on täiskasvanu
print(p2.is_adult())    # False