# Parent Class
class Hero:

    def __init__(self, nama):
        self.nama = nama

    def serang(self):
        print("Hero menyerang biasa.")


# Child Class Mage
class Mage(Hero):
    def serang(self):
        print(f"{self.nama} (Mage) menembakkan Bola Api!")


# Child Class Archer
class Archer(Hero):
    def serang(self):
        print(f"{self.nama} (Archer) memanah dari jauh!")


# Child Class Fighter
class Fighter(Hero):
    def serang(self):
        print(f"{self.nama} (Fighter) menyerang dengan pedang!")


# Child Class tambahan
class Healer(Hero):
    def serang(self):
        print(f"{self.nama} tidak menyerang, tapi menyembuhkan teman!")


# List berisi berbagai object berbeda
pasukan = [
    Mage("Eudora"),
    Archer("Miya"),
    Fighter("Zilong"),
    Mage("Gord"),
    Healer("Rafaela")
]

print("--- PERANG DIMULAI ---")

# Satu perintah, hasil berbeda (Polymorphism)
for pahlawan in pasukan:
    pahlawan.serang()
