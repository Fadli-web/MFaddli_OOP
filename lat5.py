from abc import ABC, abstractmethod

# Abstract Class (Blueprint)
class GameUnit(ABC):

    # Method wajib dimiliki semua turunan
    @abstractmethod
    def serang(self, target):
        pass

    @abstractmethod
    def info(self):
        pass


# Class Hero wajib mengisi semua method abstract
class Hero(GameUnit):

    def __init__(self, nama):
        self.nama = nama

    def serang(self, target):
        print(f"Hero {self.nama} menebas {target}!")

    def info(self):
        print(f"Saya adalah Hero: {self.nama}")


class Monster(GameUnit):

    def __init__(self, jenis):
        self.jenis = jenis

    def serang(self, target):
        print(f"Monster {self.jenis} menggigit {target}!")

    def info(self):
        print(f"Saya adalah Monster: {self.jenis}")


h = Hero("Alucard")
m = Monster("Serigala")

h.info()
m.info()
