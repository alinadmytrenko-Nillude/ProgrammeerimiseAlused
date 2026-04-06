# Baasklass inimeste andmete hoidmiseks (vanemklass / parent class)
class User:
    # Konstruktor – käivitatakse objekti loomisel automaatselt
    def __init__(self, name, age, gender):
        self.name = name       # salvestame nime atribuudiks
        self.age = age         # salvestame vanuse
        self.gender = gender   # salvestame soo

    # Meetod, mis kuvab kasutaja isikuandmed
    def show_details(self):
        print("Isikuandmed:")
        print(f"Nimi:    {self.name}")
        print(f"Vanus:   {self.age}")
        print(f"Sugu:    {self.gender}")


# Pangakonto klass – pärineb User klassist (child class / tuletatud klass)
class Bank(User):
    # Konstruktor – kutsume kõigepealt vanema (User) konstruktorit
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)   # kasutame super() et vanema __init__ tööle panna
        self.balance = 0                      # iga uue konto algjääk on 0

    # Meetod raha lisamiseks kontole
    def deposit(self, amount):
        self.balance += amount                # liidame summa kontojäägile
        print(f"Lisati {amount} €. Uus jääk: {self.balance} €")

    # Meetod raha väljavõtmiseks (kontrollib, kas piisavalt raha)
    def withdraw(self, amount):
        if amount > self.balance:             # kui soovitakse rohkem kui kontol on
            print("Viga: Kontol pole piisavalt raha!")
        else:
            self.balance -= amount            # vähendame jääki
            print(f"Välja võetud {amount} €. Järele jäi: {self.balance} €")

    # Meetod kontojäägi ja isikuandmete kuvamiseks
    def view_balance(self):
        self.show_details()                   # kutsume vanema klassi meetodit
        print(f"Konto jääk: {self.balance} €")
        print("-" * 30)


# === TESTIMINE / PEAOSA ===

# Loome pangakliendi (pangakonto objekt)
kliend1 = Bank("Jaanus", 28, "mees")

# Teeme paar tehingut
kliend1.deposit(500)       # lisame 500 €
kliend1.deposit(1200)      # lisame veel 1200 €
kliend1.withdraw(300)      # võtame 300 €
kliend1.withdraw(2000)     # proovime võtta rohkem kui on → peaks andma veateate
kliend1.view_balance()     # kuvame lõpptulemuse

# Teine klient – et näidata, et objektid on sõltumatud
kliend2 = Bank("Liisa", 19, "naine")
kliend2.deposit(100)
kliend2.view_balance()