Program tersebut adalah aplikasi GUI (Graphical User Interface) untuk mengelola pembayaran di Hotel Sejuk Asri. Aplikasi ini dibuat menggunakan bahasa pemrograman Python dengan library Tkinter untuk membuat antarmuka grafis. Berikut adalah penjelasan dari setiap bagian program tersebut : 

1. Inisialisasi dan Konfigurasi Utama

class HotelSejukAsri:
    def __init__(self, utama):
        self.utama = utama
        self.utama.title("Hotel Sejuk Asri - Pembayaran")
        self.utama.minsize(300, 300)
        self.utama.configure(bg="light sea green")

- HotelSejukAsri adalah kelas utama yang mengatur semua fungsi dalam aplikasi.
- __init__ adalah konstruktor yang diinisialisasi saat objek kelas dibuat. Di sini, jendela utama (window) dikonfigurasi dengan judul, ukuran minimum, dan warna latar belakang.

2. Membuat Garis dan Judul

self.garis_diatas_judul = tk.Canvas(utama, height=2, bd=0, highlightthickness=0, bg="black")
self.garis_diatas_judul.grid(row=0, column=0, columnspan=3, sticky="ew", pady=(10, 0))

self.label_judul = tk.Label(utama, text="Hotel Sejuk Asri", justify=tk.CENTER, font=("Helvetica", 19, "bold"), bg="light sea green")
self.label_judul.grid(row=1, column=0, columnspan=3, pady=10)

self.garis_atas = tk.Canvas(utama, height=2, bd=0, highlightthickness=0, bg="black")
self.garis_atas.grid(row=2, column=0, columnspan=3, sticky="ew", pady=(0, 10))
Canvas digunakan untuk menggambar garis di atas dan di bawah judul.
Label digunakan untuk menampilkan teks judul "Hotel Sejuk Asri" dengan font yang tebal dan besar.
3. Membuat Input Form

def input(self):
    label_label = ["Nama Petugas", "Nama Customer", "Tanggal Check-in (DD-MM-YYYY)", "Kode Kamar", "Lama Sewa (hari)", "Uang Bayar"]
    self.field = {}
    for i, label in enumerate(label_label):
        tk.Label(self.utama, text=label, font=("Helvetica", 10, "bold"), bg="light sea green").grid(row=i+3, column=0, padx=10, pady=5)
        entry = tk.Entry(self.utama)
        entry.grid(row=i+3, column=1, padx=10, pady=5)
        self.field[label] = entry

    self.label_nama_kamar = tk.Label(self.utama, text="", bg="light sea green")
    self.label_nama_kamar.grid(row=6, column=2, padx=10, pady=5)
input adalah metode yang membuat form untuk memasukkan data seperti nama petugas, nama customer, tanggal check-in, kode kamar, lama sewa, dan uang bayar.
self.field adalah dictionary yang menyimpan referensi ke masing-masing Entry (input field) untuk memudahkan pengambilan data nanti.
4. Tombol Hitung Pembayaran dan Garis Pembatas

self.tombol_hitung = tk.Button(utama, text="Hitung Pembayaran", command=self.hitung_pembayaran)
self.tombol_hitung.grid(row=9, column=1, pady=10)

self.garis_bawah = tk.Canvas(utama, height=2, bd=0, highlightthickness=0, bg="black")
self.garis_bawah.grid(row=10, column=0, columnspan=3, sticky="ew", pady=(20, 10))
Button digunakan untuk membuat tombol "Hitung Pembayaran" yang akan memanggil metode hitung_pembayaran saat diklik.
Canvas digunakan untuk menggambar garis pembatas di bawah tombol.
5. Label Kwitansi dan Hasil Pembayaran

self.label_kwitansi = tk.Label(utama, text="Bukti Kwitansi Pembayaran", justify=tk.CENTER, font=("Helvetica", 14, "bold"), bg="light sea green")
self.label_kwitansi.grid(row=11, column=0, columnspan=3, pady=10)
self.label_kwitansi.grid_remove()

self.label_hasil = tk.Label(utama, text="", justify=tk.LEFT, font=("Helvetica", 10, "bold"), bg="light sea green")
self.label_hasil.grid(row=12, column=0, columnspan=3, pady=10)

self.garis_dibawah_hasil = tk.Canvas(utama, height=2, bd=0, highlightthickness=0, bg="black")
self.garis_dibawah_hasil.grid(row=13, column=0, columnspan=3, sticky="ew", pady=(0, 10))
label_kwitansi adalah label yang menampilkan teks "Bukti Kwitansi Pembayaran", tetapi awalnya disembunyikan menggunakan grid_remove.
label_hasil adalah label yang akan menampilkan hasil perhitungan pembayaran.
Canvas digunakan untuk menggambar garis pembatas di bawah hasil.
6. Metode Hitung Pembayaran

def hitung_pembayaran(self):
    try:
        # Mendapatkan masukan
        nama_petugas = self.field["Nama Petugas"].get()
        nama_customer = self.field["Nama Customer"].get()
        tanggal_checkin = self.field["Tanggal Check-in (DD-MM-YYYY)"].get()
        kode_kamar = self.field["Kode Kamar"].get().upper()
        lama_sewa = int(self.field["Lama Sewa (hari)"].get())
        uang_bayar = int(self.field["Uang Bayar"].get())

        # Validasi tanggal
        datetime.strptime(tanggal_checkin, '%d-%m-%Y')

        # Harga dan nama kamar
        data_kamar = {
            'M': ("Melati", 650000),
            'S': ("Sakura", 550000),
            'L': ("Lily", 400000),
            'A': ("Anggrek", 350000),
            'K': ("Kamboja", 200000)
        }

        if kode_kamar not in data_kamar:
            raise ValueError("Kode Kamar tidak valid")

        nama_kamar, harga_sewa = data_kamar[kode_kamar]

        # Menghitung total pembayaran
        jumlah_bayar = harga_sewa * lama_sewa

        # Menghitung diskon
        if lama_sewa > 5:
            diskon = 0.10
        elif lama_sewa > 3:
            diskon = 0.05
        else:
            diskon = 0.0

        ppn = diskon * jumlah_bayar
        total_bayar = jumlah_bayar - ppn
        uang_kembali = uang_bayar - total_bayar

        if uang_kembali < 0:
            raise ValueError("Uang yang dibayarkan tidak cukup untuk membayar total biaya")

        # Menampilkan hasil
        teks_hasil = (f"Nama Petugas : {nama_petugas}\n"
                      f"Nama Customer : {nama_customer}\n"
                      f"Tanggal Check-in : {tanggal_checkin}\n"
                      f"Nama Kamar : {nama_kamar}\n"
                      f"Harga Sewa per Malam : Rp. {harga_sewa:,.2f}\n"
                      f"Lama Sewa : {lama_sewa} hari\n"
                      f"Jumlah Bayar : Rp. {jumlah_bayar:,.2f}\n"
                      f"Diskon : {diskon * 100}%\n"
                      f"PPN : Rp. {ppn:,.2f}\n"
                      f"Total Bayar : Rp. {total_bayar:,.2f}\n"
                      f"Uang Bayar : Rp. {uang_bayar:,.2f}\n"
                      f"Uang Kembali : Rp. {uang_kembali:,.2f}")
        self.label_hasil.config(text=teks_hasil)

        # Menampilkan label kwitansi
        self.label_kwitansi.grid()

    except Exception as e:
        messagebox.showerror("Error", str(e))
Metode hitung_pembayaran mengambil data dari input field, memvalidasi tanggal, dan menghitung total pembayaran serta diskon berdasarkan lama sewa.
Data kamar disimpan dalam dictionary data_kamar dengan kode kamar sebagai kunci dan nama serta harga sewa sebagai nilai.
Hasil perhitungan ditampilkan dalam label_hasil.
Jika terjadi kesalahan (seperti input tidak valid), akan ditampilkan pesan error menggunakan messagebox.
7. Tombol Clear dan Pause

def clear_input(self):
    """Function to clear all input fields and hide results."""
    for entry in self.field.values():
        entry.delete(0, tk.END)
    self.label_hasil.config(text="")
    self.label_kwitansi.grid_remove()

def pause(self):
    """Function to simulate pause by showing a message box."""
    messagebox.showinfo("Pause", "Press OK to continue...")
    
clear_input adalah metode untuk membersihkan semua input field dan menyembunyikan hasil serta label kwitansi.
pause adalah metode yang menampilkan pesan info untuk mensimulasikan jeda.

8. Menambahkan Tombol Clear dan Pause

if __name__ == "__main__":
    utama = tk.Tk()
    app = HotelSejukAsri(utama)

    # Adding buttons for clear and pause functionality
    tombol_clear = tk.Button(utama, text="Clear", command=app.clear_input)
    tombol_clear.grid(row=14, column=0, pady=10)

    tombol_pause = tk.Button(utama, text="Pause", command=app.pause)
    tombol_pause.grid(row=14, column=1, pady=10)

    utama.mainloop()
    
Tombol "Clear" dan "Pause" ditambahkan di bagian akhir program, masing-masing memanggil metode clear_input dan pause saat diklik.
