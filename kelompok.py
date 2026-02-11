from abc import ABC, abstractmethod

# 1. ABSTRACTION
class BarangElektronik(ABC):
    def __init__(self, nama, stok, harga_dasar):
        self.nama = nama
        # 2. ENCAPSULATION (Private Attributes)
        self.__stok = 0
        self.__harga_dasar = harga_dasar
        self.set_stok(stok) # Menggunakan setter untuk validasi awal

    # GETTER untuk Stok
    def get_stok(self):
        return self.__stok

    # SETTER untuk Stok dengan Validasi
    def set_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
        else:
            self.__stok = jumlah
            print(f"Berhasil menambahkan stok {self.nama}: {jumlah} unit.")

    def get_harga_dasar(self):
        return self.__harga_dasar

    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass

# 3. INHERITANCE & POLYMORPHISM
class Laptop(BarangElektronik):
    def __init__(self, nama, stok, harga_dasar, processor):
        super().__init__(nama, stok, harga_dasar)
        self.processor = processor

    def tampilkan_detail(self):
        return f"[LAPTOP] {self.nama} | Proc: {self.processor}"

    def hitung_harga_total(self, jumlah):
        pajak = 0.10 * self.get_harga_dasar()
        total = (self.get_harga_dasar() + pajak) * jumlah
        return total, pajak

class Smartphone(BarangElektronik):
    def __init__(self, nama, stok, harga_dasar, kamera):
        super().__init__(nama, stok, harga_dasar)
        self.kamera = kamera

    def tampilkan_detail(self):
        return f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}"

    def hitung_harga_total(self, jumlah):
        pajak = 0.05 * self.get_harga_dasar()
        total = (self.get_harga_dasar() + pajak) * jumlah
        return total, pajak

# 4. FITUR TRANSAKSI (POLYMORPHISM)
def proses_transaksi(daftar_belanja):
    print("\n--- STRUK TRANSAKSI ---")
    grand_total = 0
    for i, item in enumerate(daftar_belanja, 1):
        produk = item['objek']
        qty = item['jumlah']
        
        detail = produk.tampilkan_detail()
        total_item, pajak_item = produk.hitung_harga_total(qty)
        
        print(f"{i}. {detail}")
        print(f"   Harga Dasar: Rp {produk.get_harga_dasar():,} | Pajak: Rp {pajak_item:,}")
        print(f"   Beli: {qty} unit | Subtotal: Rp {total_item:,}")
        grand_total += total_item
    
    print("-" * 40)
    print(f"TOTAL TAGIHAN: Rp {grand_total:,}")
    print("-" * 40)

# --- ALUR PROGRAM (User Story) ---
print("--- SETUP DATA ---")
laptop1 = Laptop("ROG Zephyrus", 10, 20000000, "Ryzen 9")
hp1 = Smartphone("iPhone 13", 20, 15000000, "12MP")

# Mencoba isi stok negatif (Akan ditolak oleh Setter)
hp1.set_stok(-5) 

# Simulasi Belanja
keranjang = [
    {'objek': laptop1, 'jumlah': 2},
    {'objek': hp1, 'jumlah': 1}
]

proses_transaksi(keranjang)