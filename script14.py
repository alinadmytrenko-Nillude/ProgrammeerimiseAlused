class A:    # Määrame baasklassi A
    field1 = 1  # A-klassi atribuut: ühine kõigile eksemplaridele, väärtus 1

    def make_str(self):     # Meetod make_str klassis A
        print(self.field1)   # Prindib väärtuse field1 (st 1)


class B(A):     # Klass B pärineb klassist A
    field2 = 2      # Uus klassi B atribuut: väärtus 2

    def make_str(self):       # Ümberdefineerime (override) meetodi make_str klassist A
        print(self.field1, self.field2)   # Prindib välja field1 (A-st) ja field2 (B-st) → 1 2


class C(A):     # Klass C pärineb samuti klassist A.
    field3 = 3      # Uus klassi C atribuut: väärtus 3

    def make_str(self):     # Ümberdefineerime meetodi make_str
        print(self.field1, self.field3)     # Prindib välja field1 (A-st) ja field3 (C-st) → 1 3

# Loome ühe objekti igast klassist
a = A()     # Klass A eksemplar
b = B()     # Klass B eksemplar (A pärija)
c = C()     # Klass C eksemplar (A pärija)

for i in (a, b, c):     # Tsükkel kõigi kolme objekti kohta
    i.make_str()        # Kutsume meetodit make_str() iga objekti jaoks
# Polümorfismi abil kutsutakse esile õige versioon meetodist.