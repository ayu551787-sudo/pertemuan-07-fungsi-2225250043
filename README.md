# Pertemuan 07 Fungsi Python

Nama: Ayu Syarifatu Zahra
NIM: 2225250043
Kelas: 3B  

## Tujuan
Menggunakan fungsi, parameter, return value, dan scope untuk membuat program modular.

## Cara Menjalankan
python praktik/utilitas_matematika.py

## Struktur Fungsi
1. **`luas_persegi_panjang(p, l)`**
   - **Tujuan:** Menghitung luas persegi panjang berdasarkan panjang dan lebar.
   - **Parameter:** 
     - `p`: Panjang persegi panjang (tipe data angka).
     - `l`: Lebar persegi panjang (tipe data angka).
   - **Return Value:** Mengembalikan hasil perkalian `p * l`.

2. **`jumlah_n(n)`**
   - **Tujuan:** Menghitung jumlah total deret angka dari 1 sampai $n$.
   - **Parameter:** 
     - `n`: Batas angka akhir deret (integer).
   - **Return Value:** Mengembalikan total penjumlahan angka (`total`).

3. **`statistik(data)`**
   - **Tujuan:** Menghitung nilai minimum, maksimum, dan rata-rata dari sekumpulan data list.
   - **Parameter:** 
     - `data`: Sebuah list yang berisi kumpulan angka (integer/float).
   - **Return Value:** Mengembalikan tiga nilai sekaligus yaitu `minimum`, `maksimum`, dan `rata`.

## Hasil Pengujian

| No | Nama Fungsi / Modul | Input / Parameter | Hasil yang Diharapkan | Hasil Aktual | Status |
|----|---------------------|-------------------|-----------------------|--------------|--------|
| 1 | Fungsi `luas_persegi_panjang` | `p = 5`, `l = 3` | `15` | `15` | Berhasil |
| 2 | Fungsi `jumlah_n` | `n = 5` | `15` | `15` | Berhasil |
| 3 | Fungsi `statistik` | `[70, 80, 65, 90, 75]` | Min: 65, Maks: 90, Rata-rata: 75.0 | Min: 65, Maks: 90, Rata-rata: 75.0 | Berhasil |

## Refleksi
1. **Penggunaan Parameter & Return Value:** Mampu mengirim data ke dalam fungsi dan mengambil kembali hasilnya untuk digunakan di bagian program utama.
2. **Modularitas Kode:** Penggunaan file terpisah seperti `utilitas_matematika.py` membuat kode sumber menjadi jauh lebih bersih, terstruktur, mudah dibaca, serta dapat digunakan kembali (*reusable*).
3. **Ketelitian Sintaks:** Belajar memahami pentingnya membedakan penggunaan kurung siku `[]` untuk mengakses elemen list dan kurung biasa `()` untuk pemanggilan fungsi, serta mengatasi berbagai *error* konfigurasi terminal saat menjalankan program Python.