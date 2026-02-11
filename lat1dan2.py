# Membuat class Hero sebagai blueprint / cetakan object
class Hero:

    # Constructor -> otomatis dijalankan saat object dibuat
    def __init__(self, name, hp, attack_power):
        self.name = name              # atribut nama hero
        self.hp = hp                  # atribut health point (nyawa)
        self.attack_power = attack_power  # atribut kekuatan serangan

    # Method untuk menampilkan informasi hero
    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")


# Membuat object dari class Hero (instansiasi)
hero1 = Hero("Layla", 100, 15)
hero2 = Hero("Zilong", 120, 20)

# Memanggil method info()
hero1.info()
hero2.info()

# Mengubah nilai atribut secara langsung (karena masih public)
hero1.hp = 500
print(hero1.hp)  # Output: 500

class Hero:

    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    # Method menyerang object lain
    def serang(self, lawan):
        # self adalah hero yang menyerang
        # lawan adalah object hero lain
        print(f"{self.name} menyerang {lawan.name}!")

        # memanggil method milik object lawan
        lawan.diserang(self.attack_power)

    # Method menerima serangan
    def diserang(self, damage):
        # HP dikurangi damage
        self.hp -= damage
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self.hp}")


hero1 = Hero("Layla", 100, 15)
hero2 = Hero("Zilong", 120, 20)

print("\n--- Pertarungan Dimulai ---")

# Object saling berinteraksi
hero1.serang(hero2)
hero2.serang(hero1)
