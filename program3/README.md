# Program Manajemen Barang

## Deskripsi

Program Manajemen Barang adalah aplikasi desktop yang memungkinkan pengguna untuk mengelola data barang, termasuk memasukkan, menampilkan, menghapus, mencari, dan menghitung jumlah pembelian barang. Program ini dibangun menggunakan Python dan Tkinter untuk antarmuka grafis pengguna (GUI).

## Fitur Utama

- **Input Data Barang:** Menambahkan barang baru dengan nama, harga, dan stok.
- **Tampil Data Barang:** Menampilkan daftar semua barang yang telah dimasukkan.
- **Delete Data Barang:** Menghapus barang berdasarkan nama.
- **Cari Data Barang:** Mencari dan menampilkan informasi barang berdasarkan nama.
- **Hitung Jumlah Pembelian:** Menghitung total pembayaran dan memperbarui stok barang berdasarkan jumlah pembelian.

## Cara Menjalankan

1. **Persiapan:**
   - Pastikan Python 3.x sudah terinstal di sistem Anda.
   - Modul `tkinter` harus sudah terinstal (biasanya sudah termasuk dalam distribusi Python standar).

2. **Menjalankan Program:**
   - Download atau clone repository ini ke mesin lokal Anda.
   - Buka terminal atau command prompt.
   - Navigasi ke direktori di mana file `barang.py` berada.
   - Jalankan perintah berikut:

     ```sh
     python barang.py
     ```

   - Aplikasi GUI akan muncul dan Anda dapat mulai menggunakan aplikasi untuk mengelola data barang.

## Struktur Program

- **`barang.py`**: File utama yang berisi logika aplikasi dan antarmuka pengguna menggunakan Tkinter.

## Penjelasan Fitur

### 1. **Antarmuka Pengguna**

- **Header:** Judul aplikasi "Manajemen Barang" dengan garis pemisah di atas dan di bawah.
- **Menu:** Menu utama dengan tombol untuk mengakses berbagai fungsi aplikasi (Input Data Barang, Tampil Data Barang, Delete Data Barang, Cari Data Barang, Hitung Jumlah Pembelian).

### 2. **Fungsi Utama**

#### **Input Data Barang**

- Menampilkan formulir untuk memasukkan nama barang, harga, dan stok.
- Menggunakan validasi untuk memastikan data yang dimasukkan valid.
- Menyimpan data barang ke dalam daftar dan menampilkan pesan konfirmasi.

#### **Tampil Data Barang**

- Menampilkan semua barang yang telah dimasukkan dalam format nama, harga, dan stok.
- Menampilkan pesan jika tidak ada data barang.

#### **Delete Data Barang**

- Meminta nama barang yang akan dihapus menggunakan dialog input.
- Mencari dan menghapus barang dari daftar berdasarkan nama.
- Menampilkan pesan konfirmasi atau kesalahan jika barang tidak ditemukan.

#### **Cari Data Barang**

- Meminta nama barang yang dicari menggunakan dialog input.
- Menampilkan informasi barang berdasarkan nama jika ditemukan.
- Menampilkan pesan jika barang tidak ditemukan.

#### **Hitung Jumlah Pembelian**

- Menampilkan formulir untuk memasukkan nama barang dan jumlah pembelian.
- Menghitung total pembayaran dan memperbarui stok barang.
- Menampilkan pesan dengan total pembayaran dan sisa stok, atau pesan kesalahan jika stok tidak cukup atau barang tidak ditemukan.

## Struktur Kode

- **`Barang Class:`** Kelas untuk menyimpan informasi barang (nama, harga, stok).
- **`BarangApp Class:`** Kelas utama yang mengelola antarmuka pengguna dan logika aplikasi.
  - **`__init__`:** Menyiapkan jendela utama dan menu aplikasi.
  - **`create_header`:** Membuat header aplikasi dengan judul.
  - **`create_menu`:** Membuat menu dengan tombol-tombol untuk akses berbagai fungsi.
  - **`clear_frame`:** Menghapus semua widget dari frame.
  - **`show_input_barang`:** Menampilkan formulir untuk memasukkan data barang.
  - **`simpan_barang`:** Menyimpan data barang ke dalam daftar.
  - **`show_tampil_barang`:** Menampilkan data barang yang tersimpan.
  - **`show_delete_barang`:** Menghapus barang berdasarkan nama.
  - **`show_cari_barang`:** Mencari dan menampilkan barang berdasarkan nama.
  - **`show_hitung_pembelian`:** Menampilkan formulir untuk menghitung total pembelian.
  - **`proses_pembelian`:** Menghitung total pembayaran dan memperbarui stok barang.
