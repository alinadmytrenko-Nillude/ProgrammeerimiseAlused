class Isik:
    def __init__(self, eesnimi, perekonnanimi, kvalifikatsioon=1):
        self.eesnimi = eesnimi
        self.perekonnanimi = perekonnanimi
        self.kvalifikatsioon = kvalifikatsioon

    def get_info(self):
        return f"{self.eesnimi} {self.perekonnanimi}, kvalifikatsioon: {self.kvalifikatsioon}"

    def __del__(self):
        print(f"Hüvasti, härra {self.eesnimi} {self.perekonnanimi}")


# Loome 3 töötajat
t1 = Isik("Jaan", "Tamm", 5)
t2 = Isik("Mari", "Kask", 3)
t3 = Isik("Peeter", "Mänd")

tootajad = [t1, t2, t3]

# Vaatame kõiki
print("Töötajad:")
for t in tootajad:
    print(t.get_info())

# Leiame nõrgima
norgim = min(tootajad, key=lambda x: x.kvalifikatsioon)
print(f"\nNõrgim: {norgim.get_info()}")
print("Vallandame...\n")

# Vallandame
tootajad.remove(norgim)
del norgim

# Näitame ülejäänud
print("\nÜlejäänud:")
for t in tootajad:
    print(t.get_info())

input("\nVajuta Enter...")