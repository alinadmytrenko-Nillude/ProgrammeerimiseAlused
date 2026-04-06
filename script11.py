class Pet:                                          # Baasklass — üldine lemmikloom
    def __init__(self, name, age):                  # Konstruktor: nimi ja vanus
        self.name = name                            # Salvestame nime
        self.age = age                              # Salvestame vanuse

    def show(self):                                 # Meetod info kuvamiseks
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):                                # Baasmeetod "rääkimiseks"
        print("I don't know what I say")            # Lemmikloom ei tea, mida öelda


class Cat(Pet):                                     # Klass Cat pärib klassist Pet
    def __init__(self, name, age, color):           # Lisame uue parameetri — värv
        super().__init__(name, age)                 # Kutsume välja vanema klassi konstruktorit
        self.color = color                          # Salvestame kassi värvi

    def speak(self):                                # Ümberdefineerime meetodi speak kassile
        print("Meow")                               # Kass müügab

    def show(self):                                 # Ümberdefineerime show, et lisada värv
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")


class Dog(Pet):                                     # Klass Dog pärib klassist Pet
    def speak(self):                                # Ümberdefineerime ainult meetodi speak
        print("Bark")                               # Koer haugub

    # Meetodit show ei pea ümber defineerima — kasutatakse Pet klassist päritud versiooni


# Näited kasutamisest
print("=== Näited koodi tööst ===")

p = Pet("Tim", 19)                                  # Tavapärane lemmikloom (mitte kass ega koer)
p.show()                                            # → I am Tim and I am 19 years old
p.speak()                                           # → I don't know what I say

print()

c = Cat("Bill", 34, "Brown")                        # Kass koos karva värviga
c.show()                                            # → I am Bill and I am 34 years old and I am Brown
c.speak()                                           # → Meow

print()

d = Dog("Jill", 25)                                 # Koer
d.show()                                            # → I am Jill and I am 25 years old (kasutab Pet klassi meetodit)
d.speak()                                           # → Bark