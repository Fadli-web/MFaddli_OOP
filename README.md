<img width="628" height="133" alt="image" src="https://github.com/user-attachments/assets/11c92ca2-cbd7-4b95-9590-459a5ca0c1e1" /># 📘 Praktikum OOP Python – Battle System & Konsep OOP

 Latihan 1 – Membuat Class Hero
Pada latihan ini dibuat class `Hero` yang memiliki atribut:
* name
* hp
* attack_power
Object dibuat dari class tersebut dan menampilkan informasi hero menggunakan method `info()`.

# Hasil Output:
<img width="628" height="133" alt="image" src="https://github.com/user-attachments/assets/b197dbfb-f76b-4a56-a458-96ea3df32e4e" />
Hero: Layla | HP: 100 | Power: 15
Hero: Zilong | HP: 120 | Power: 20

#### Analisis:
Class berfungsi sebagai blueprint. Object yang dibuat dari class memiliki data masing-masing walaupun berasal dari class yang sama.

---

###  Latihan 2 – Interaksi Antar Objek
Ditambahkan method:

* `serang()`
* `diserang()`

Hero dapat menyerang hero lain dan mengurangi HP lawan.

#### Hasil Output:
<img width="539" height="214" alt="image" src="https://github.com/user-attachments/assets/84b306c0-00e9-494f-8772-641793627974" />
```
--- Pertarungan Dimulai ---
Layla menyerang Zilong!
Zilong terkena damage 15. Sisa HP: 105
Zilong menyerang Layla!
Layla terkena damage 20. Sisa HP: 80
```

#### Analisis:
Parameter method menerima object, bukan string, sehingga object dapat mengakses atribut dan method milik object lain.

---

###  Latihan 3 – Inheritance
Class `Mage` dibuat sebagai turunan dari class `Hero`.
Mage memiliki atribut tambahan yaitu `mana` dan skill khusus `fireball`.

#### Hasil Output:
<img width="585" height="217" alt="image" src="https://github.com/user-attachments/assets/89c7cbe1-b455-49a5-9ad6-217b4b8110cb" />

```
Eudora [Mage] | HP: 80 | Mana: 100
Eudora menyerang Balmond!
Balmond terkena damage 30. Sisa HP: 170
Eudora menggunakan Fireball ke Balmond!
Balmond terkena damage 60. Sisa HP: 110
```

#### Analisis:
Inheritance memungkinkan class anak menggunakan fitur dari class induk tanpa menulis ulang kode.

---

###  Latihan 4 – Encapsulation
Atribut HP diubah menjadi private (`__hp`) agar tidak bisa diubah langsung dari luar class.
Digunakan method:

* `get_hp()` (getter)
* `set_hp()` (setter)

#### Hasil Output:
<img width="816" height="163" alt="image" src="https://github.com/user-attachments/assets/257a911c-b137-4d91-963c-dde8b6cd6b88" />

```
0
```

#### Analisis:
Setter digunakan untuk validasi data agar HP tidak negatif atau terlalu besar. Hal ini menjaga integritas data program.

###  Latihan 5 – Abstraction & Interface
Menggunakan modul `abc` untuk membuat abstract class `GameUnit`.
Class turunan wajib memiliki method:

* `serang()`
* `info()`

#### Hasil Output:
<img width="646" height="218" alt="image" src="https://github.com/user-attachments/assets/f51180e0-1cd5-4086-8988-a33d0aecc0a4" />

```
Saya adalah Hero: Alucard
Saya adalah Monster: Serigala
```

#### Analisis:
Abstract class berfungsi sebagai kontrak agar semua class turunan memiliki struktur method yang sama.

---

### Latihan 6 – Polymorphism
Beberapa class hero memiliki method `serang()` yang sama tetapi menghasilkan output berbeda.

#### Hasil Output:
<img width="732" height="258" alt="image" src="https://github.com/user-attachments/assets/73807162-8968-4c00-81d6-74e07c334408" />

```
--- PERANG DIMULAI ---
Eudora (Mage) menembakkan Bola Api!
Miya (Archer) memanah dari jauh!
Zilong (Fighter) menyerang dengan pedang!
Gord (Mage) menembakkan Bola Api!
Rafaela tidak menyerang, tapi menyembuhkan teman!
```

#### Analisis:
Polymorphism memungkinkan satu method digunakan pada berbagai object dengan perilaku berbeda tanpa mengubah kode utama.


#### TechMaster
Implementasi Konsep (Masterclass)
✅ Bagian 1 – Abstraction (Kerangka Dasar)
Dibuat Abstract Class BarangElektronik menggunakan modul abc. Class ini berfungsi sebagai kontrak utama yang tidak dapat diinstansiasi langsung.
Method Wajib: tampilkan_detail() dan hitung_harga_total().

✅ Bagian 2 – Encapsulation (Keamanan Data)
Atribut sensitif didefinisikan sebagai Private Attribute untuk mencegah manipulasi data dari luar class.
Atribut: __stok dan __harga_dasar.

Validasi: Method set_stok atau tambah_stok memastikan jumlah stok tidak boleh negatif.

✅ Bagian 3 – Inheritance (Pewarisan)
Dibuat dua class turunan yang mewarisi atribut dari BarangElektronik dengan spesifikasi unik:
Class Laptop: Memiliki atribut processor dan pajak pembelian 10%.

Class Smartphone: Memiliki atribut kamera dan pajak pembelian 5%.

✅ Bagian 4 – Polymorphism (Fleksibilitas)
Implementasi method overriding pada hitung_harga_total dan fungsi proses_transaksi yang mampu menerima list berisi campuran objek Laptop dan Smartphone secara otomatis.

### Hasil Output dari TechMaster
  <img width="764" height="419" alt="image" src="https://github.com/user-attachments/assets/39edbcd3-16cc-4613-8da9-864f19500461" />
--- SETUP DATA ---
Berhasil menambahkan stok ROG Zephyrus: 10 unit. 
Gagal update stok iPhone 13! Stok tidak boleh negatif (-5). [cite: 279]
Berhasil menambahkan stok iPhone 13: 20 unit. [cite: 279]

--- STRUK TRANSAKSI ---
1. [LAPTOP] ROG Zephyrus | Proc: Ryzen 9 [cite: 280]
   Harga Dasar: Rp 20.000.000 | Pajak(10%): Rp 2.000.000 [cite: 281]
   Beli: 2 unit | Subtotal: Rp 44.000.000 [cite: 281]

2. [SMARTPHONE] iPhone 13 | Cam: 12MP [cite: 282]
   Harga Dasar: Rp 15.000.000 | Pajak(5%): Rp 750.000 [cite: 282]
   Beli: 1 unit | Subtotal: Rp 15.750.000 
----------------------------------------
TOTAL TAGIHAN: Rp 59.750.000 
----------------------------------------



##  Kesimpulan Praktikum

Dari praktikum ini dapat disimpulkan bahwa OOP membantu program menjadi:

* Lebih terstruktur
* Mudah dikembangkan
* Aman dari perubahan data sembarangan
* Mudah menambah fitur baru tanpa mengubah kode lama

Konsep OOP sangat cocok digunakan dalam pengembangan game, aplikasi, maupun sistem backend karena modular dan fleksibel.

---

## 📸 Dokumentasi (Opsional)

Tambahkan screenshot hasil output program atau tampilan kode dari VS Code pada bagian ini jika diperlukan.
