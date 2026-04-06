class Person:
    number_of_people = 0    # Klassi muutuja – ühine kõigile objektidele
    GRAVITY = -9.8          # Konstant (klassimuutuja), mida tavaliselt ei muudeta

    def __init__(self, name):           # Konstruktor – kutsutakse iga uue objekti loomisel
        self.name = name                # Isiku nimi (eksemplari muutuja)
        Person.add_person()             # Iga kord, kui luuakse uus inimene, suurendame loendurit
        # VÕI: self.add_person() – töötab samuti, sest @classmethod

    @classmethod
    def number_of_people_(cls):         # Klassimeetod – tagastab praeguse inimeste arvu
        return cls.number_of_people     # Kasutame cls, sest meetod töötab klassiga, mitte eksemplariga

    @classmethod
    def add_person(cls):                # Klassimeetod – suurendab inimeste arvu ühe võrra
        cls.number_of_people += 1       # Muudame klassimuutujat


# Näited kasutamisest
p1 = Person("tim")          # Luuakse esimene inimene → loendur muutub 1-ks
p2 = Person("jill")         # Teine inimene → loendur muutub 2-ks

print(Person.number_of_people_())   # Väljastab: 2