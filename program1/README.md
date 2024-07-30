# Program Sewa Hotel - Hotel Sejuk Asri

## Description

Program ini adalah aplikasi manajemen pembayaran untuk Hotel Sejuk Asri. Aplikasi ini memungkinkan petugas hotel untuk menghitung total pembayaran sewa kamar berdasarkan informasi yang diberikan oleh pelanggan. Program ini juga menghitung diskon dan pajak (PPN) serta memberikan rincian pembayaran kepada pelanggan.

### Fitur Utama

- **Input Data:** Petugas dapat memasukkan informasi pelanggan, tanggal check-in, kode kamar, lama sewa, dan uang bayar.
- **Perhitungan Otomatis:** Program menghitung total biaya sewa kamar, diskon, PPN, dan uang kembali.
- **Validasi:** Validasi tanggal check-in dan kode kamar untuk memastikan data yang dimasukkan valid.
- **Laporan Kwitansi:** Menampilkan bukti kwitansi pembayaran yang dapat dicetak atau disimpan.

## Cara Menjalankan

1. **Persiapan:**
   - Pastikan Python sudah terinstall di sistem Anda (Python 3.x disarankan).
   - Pastikan modul `tkinter` sudah terinstall. Modul ini biasanya sudah termasuk dalam distribusi Python standar.

2. **Menjalankan Program:**
   - Download atau clone repository ini ke mesin lokal Anda.
   - Buka terminal atau command prompt.
   - Navigasi ke directory di mana file `main_program.py` berada.
   - Jalankan perintah berikut:

     ```sh
     python main_program.py
     ```

   - Aplikasi GUI akan muncul, dan Anda dapat memasukkan informasi yang diperlukan untuk menghitung pembayaran.

## Struktur Program

- **`main_program.py`**: File utama yang berisi logika program dan antarmuka pengguna menggunakan `tkinter`.
- **`README.md`**: File dokumentasi ini yang menjelaskan cara menggunakan program dan informasi lainnya.

## Kode Kamar dan Harga

| Kode Kamar | Nama Kamar | Harga per Malam |
|------------|------------|-----------------|
| M          | Melati     | Rp. 650,000     |
| S          | Sakura     | Rp. 550,000     |
| L          | Lily       | Rp. 400,000     |
| A          | Anggrek    | Rp. 350,000     |
| K          | Kamboja    | Rp. 200,000     |

## Diskon

- **Lama Sewa lebih dari 5 hari**: Diskon 10%
- **Lama Sewa lebih dari 3 hari**: Diskon 5%
- **Lama Sewa 3 hari atau kurang**: Tidak ada diskon

## PPN

- Diskon akan dihitung terlebih dahulu, kemudian PPN 10% dari jumlah yang harus dibayar setelah diskon akan diterapkan.
