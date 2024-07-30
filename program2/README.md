# Program Perhitungan Bangun Datar

## Description

Program ini adalah aplikasi desktop untuk menghitung luas dan keliling berbagai bangun datar seperti segi empat, persegi panjang, segitiga, dan lingkaran. Program ini menggunakan antarmuka grafis pengguna (GUI) yang dibangun dengan Python dan Tkinter. Pengguna dapat memilih jenis bangun datar, memasukkan nilai-nilai yang diperlukan, dan mendapatkan hasil perhitungan.

## Fitur Utama

- **Pemilihan Bangun Datar:** Pengguna dapat memilih antara segi empat, persegi panjang, segitiga, atau lingkaran.
- **Input Dinamis:** Formulir input disesuaikan dengan jenis bangun datar yang dipilih.
- **Perhitungan Luas dan Keliling:** Menghitung luas dan keliling sesuai dengan jenis bangun datar yang dipilih.
- **Validasi Input:** Menangani input yang tidak valid dengan menampilkan pesan kesalahan.
- **Fungsi Clear dan Pause:** Fitur untuk menghapus semua input dan menghentikan sementara aplikasi.

## Cara Menjalankan

1. **Persiapan:**
   - Pastikan Python 3.x sudah terinstal di sistem Anda.
   - Modul `tkinter` harus sudah terinstal (biasanya sudah termasuk dalam distribusi Python standar).

2. **Menjalankan Program:**
   - Download atau clone repository ini ke mesin lokal Anda.
   - Buka terminal atau command prompt.
   - Navigasi ke direktori di mana file `main_program.py` berada.
   - Jalankan perintah berikut:

     ```sh
     python main_program.py
     ```

   - Aplikasi GUI akan muncul dan Anda dapat mulai menggunakan aplikasi untuk menghitung bangun datar.

## Struktur Program

- **`main_program.py`**: File utama yang berisi logika program dan antarmuka pengguna menggunakan `tkinter`.

## Penjelasan Fitur

### 1. **Antarmuka Pengguna**

- **Judul dan Garis:** Aplikasi dimulai dengan judul yang diatur di bagian atas jendela, diikuti dengan garis pemisah.
- **Pilihan Bangun Datar:** Empat tombol (Segi Empat, Persegi Panjang, Segitiga, Lingkaran) memungkinkan pengguna untuk memilih bangun datar yang ingin dihitung.
- **Formulir Input:** Tergantung pada jenis bangun datar yang dipilih, formulir input akan disesuaikan untuk memasukkan nilai yang relevan (misalnya, sisi, panjang, lebar, radius).
- **Tombol Hitung:** Menghitung luas dan keliling berdasarkan input yang diberikan.
- **Hasil:** Menampilkan hasil perhitungan luas dan keliling di bagian bawah jendela.
- **Tombol Clear:** Menghapus semua input dan hasil.
- **Tombol Pause:** Menampilkan pesan peringatan untuk menunggu.

### 2. **Fungsi Perhitungan**

- **Segi Empat:** Menghitung luas dan keliling segi empat berdasarkan sisi yang diberikan.
- **Persegi Panjang:** Menghitung luas dan keliling persegi panjang berdasarkan panjang dan lebar.
- **Segitiga:** Menghitung luas dan keliling segitiga berdasarkan alas, tinggi, dan sisi miring.
- **Lingkaran:** Menghitung luas dan keliling lingkaran berdasarkan radius.

### 3. **Validasi Input**

Jika input tidak valid (misalnya, tidak dapat dikonversi menjadi angka), program akan menampilkan pesan kesalahan menggunakan `messagebox`.

## Fungsi Tambahan

- **`clear_input()`:** Menghapus semua nilai dari formulir input dan hasil yang ditampilkan.
- **`pause()`:** Menampilkan pesan informasi untuk menghentikan sementara aplikasi.
