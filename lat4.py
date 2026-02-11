class Hero:

    # Constructor -> membuat atribut saat object dibuat
    def __init__(self, nama, hp_awal):
        self.nama = nama
        self.__hp = hp_awal   # private attribute

    # Getter untuk mengambil HP
    def get_hp(self):
        return self.__hp

    # Setter untuk mengubah HP dengan validasi
    def set_hp(self, nilai_baru):

        # HP tidak boleh negatif
        if nilai_baru < 0:
            self.__hp = 0

        # Anti cheat
        elif nilai_baru > 1000:
            print("Cheat terdeteksi!")
            self.__hp = 1000

        else:
            self.__hp = nilai_baru

    # Method menerima serangan
    def diserang(self, damage):
        sisa_hp = self.get_hp() - damage
        self.set_hp(sisa_hp)

        print(f"{self.nama} terkena damage {damage}. Sisa HP: {self.get_hp()}")


# --- Uji coba ---
hero1 = Hero("Layla", 100)

hero1.set_hp(-50)
print(hero1.get_hp())
