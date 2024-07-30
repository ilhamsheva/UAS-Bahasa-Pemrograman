import tkinter as tk
from tkinter import messagebox, simpledialog

class Barang:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

class BarangApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Manajemen Barang")
        self.root.geometry("300x400")  # Menambah ukuran jendela untuk tombol yang lebih banyak
        self.barang_list = []
        
        # Frame utama untuk aplikasi dengan latar belakang hijau telur asin
        self.main_frame = tk.Frame(self.root, bg="#7FA1C3")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Membuat header aplikasi
        self.create_header("Manajemen Barang")

        # Frame untuk menu dengan latar belakang hijau telur asin
        self.menu_frame = tk.Frame(self.main_frame, bg="#7FA1C3")
        self.menu_frame.pack(pady=10)

        # Menampilkan menu utama
        self.create_menu()

    def create_header(self, title):
        # Garis di atas judul dengan warna hitam
        self.garis_diatas_judul = tk.Canvas(self.main_frame, height=2, bd=0, highlightthickness=0, bg="black")
        self.garis_diatas_judul.pack(fill=tk.X, pady=(10, 0))

        # Label judul dengan warna teks hitam
        self.label_judul = tk.Label(self.main_frame, text=title, justify=tk.CENTER, font=("Helvetica", 19, "bold"), bg="#7FA1C3", fg="black")
        self.label_judul.pack(pady=10)

        # Garis di bawah judul dengan warna hitam
        self.garis_dibawah_judul = tk.Canvas(self.main_frame, height=2, bd=0, highlightthickness=0, bg="black")
        self.garis_dibawah_judul.pack(fill=tk.X, pady=(0, 10))

    def create_menu(self):
        # Menghapus widget-widget sebelumnya dari menu frame
        self.clear_frame(self.menu_frame)

        # Membuat tombol-tombol untuk berbagai menu dengan warna latar belakang hijau telur asin
        tk.Button(self.menu_frame, text="Input Data Barang", command=self.show_input_barang, bg="#7FA1C3").pack(pady=10, fill=tk.X)
        tk.Button(self.menu_frame, text="Tampil Data Barang", command=self.show_tampil_barang, bg="#7FA1C3").pack(pady=10, fill=tk.X)
        tk.Button(self.menu_frame, text="Delete Data Barang", command=self.show_delete_barang, bg="#7FA1C3").pack(pady=10, fill=tk.X)
        tk.Button(self.menu_frame, text="Cari Data Barang", command=self.show_cari_barang, bg="#7FA1C3").pack(pady=10, fill=tk.X)
        tk.Button(self.menu_frame, text="Hitung Jumlah Pembelian", command=self.show_hitung_pembelian, bg="#7FA1C3").pack(pady=10, fill=tk.X)

    def clear_frame(self, frame):
        # Menghapus semua widget di dalam frame
        for widget in frame.winfo_children():
            widget.destroy()

    def show_input_barang(self):
        # Mengubah tampilan untuk input data barang
        self.clear_frame(self.menu_frame)

        # Variabel untuk menyimpan input pengguna
        self.nama_barang_var = tk.StringVar()
        self.harga_barang_var = tk.DoubleVar()
        self.stok_barang_var = tk.IntVar()

        # Input nama barang
        tk.Label(self.menu_frame, text="Nama Barang", bg="#7FA1C3").pack(pady=5)
        tk.Entry(self.menu_frame, textvariable=self.nama_barang_var).pack(pady=5)
        
        # Input harga barang
        tk.Label(self.menu_frame, text="Harga Barang", bg="#7FA1C3").pack(pady=5)
        tk.Entry(self.menu_frame, textvariable=self.harga_barang_var).pack(pady=5)
        
        # Input stok barang
        tk.Label(self.menu_frame, text="Stok Barang", bg="#7FA1C3").pack(pady=5)
        tk.Entry(self.menu_frame, textvariable=self.stok_barang_var).pack(pady=5)
        
        # Tombol simpan dan kembali
        tk.Button(self.menu_frame, text="Simpan", command=self.simpan_barang, bg="#7FA1C3").pack(pady=10)

    def simpan_barang(self):
        # Mengambil data dari input pengguna
        nama = self.nama_barang_var.get()
        harga = self.harga_barang_var.get()
        stok = self.stok_barang_var.get()
        
        # Validasi data
        if not nama or harga <= 0 or stok < 0:
            messagebox.showerror("Error", "Data tidak valid")
            return
        
        # Format harga dengan dua desimal
        harga = round(harga, 2)
        
        # Menyimpan data barang ke dalam list
        self.barang_list.append(Barang(nama, harga, stok))
        messagebox.showinfo("Info", "Data barang berhasil disimpan")
        self.create_menu()

    def show_tampil_barang(self):
        # Mengubah tampilan untuk menampilkan data barang
        self.clear_frame(self.menu_frame)
        
        if not self.barang_list:
            tk.Label(self.menu_frame, text="Tidak ada data barang", bg="#7FA1C3").pack(pady=10)
        else:
            for barang in self.barang_list:
                # Format harga dengan dua desimal
                formatted_harga = f"{barang.harga:.2f}"
                tk.Label(self.menu_frame, text=f"Nama: {barang.nama}, Harga: {formatted_harga}, Stok: {barang.stok}", bg="#7FA1C3").pack(pady=5)
        
        # Tombol kembali
        tk.Button(self.menu_frame, text="Kembali", command=self.create_menu, bg="#7FA1C3").pack(pady=10)

    def show_delete_barang(self):
        # Mengubah tampilan untuk menghapus data barang
        self.clear_frame(self.menu_frame)
        
        # Input nama barang yang ingin dihapus
        nama = simpledialog.askstring("Input", "Masukkan Nama Barang yang ingin dihapus")
        if not nama:
            return
        
        # Mencari dan menghapus barang
        for barang in self.barang_list:
            if barang.nama == nama:
                self.barang_list.remove(barang)
                messagebox.showinfo("Info", "Barang berhasil dihapus")
                self.create_menu()
                return
        
        messagebox.showerror("Error", "Barang tidak ditemukan")

    def show_cari_barang(self):
        # Mengubah tampilan untuk mencari data barang
        self.clear_frame(self.menu_frame)

        # Input nama barang yang dicari
        nama = simpledialog.askstring("Input", "Masukkan Nama Barang yang dicari")
        if not nama:
            return
        
        # Mencari dan menampilkan barang
        for barang in self.barang_list:
            if barang.nama == nama:
                # Format harga dengan dua desimal
                formatted_harga = f"{barang.harga:.2f}"
                tk.Label(self.menu_frame, text=f"Nama: {barang.nama}, Harga: {formatted_harga}, Stok: {barang.stok}", bg="#7FA1C3").pack(pady=5)
                break
        else:
            tk.Label(self.menu_frame, text="Barang tidak ditemukan", bg="#7FA1C3").pack(pady=5)
        
        # Tombol kembali
        tk.Button(self.menu_frame, text="Kembali", command=self.create_menu, bg="#7FA1C3").pack(pady=10)

    def show_hitung_pembelian(self):
        # Mengubah tampilan untuk menghitung jumlah pembelian
        self.clear_frame(self.menu_frame)
        
        # Variabel untuk menyimpan input pengguna
        self.nama_barang_var = tk.StringVar()
        self.jumlah_beli_var = tk.IntVar()

        # Input nama barang
        tk.Label(self.menu_frame, text="Nama Barang", bg="#7FA1C3").pack(pady=5)
        tk.Entry(self.menu_frame, textvariable=self.nama_barang_var).pack(pady=5)
        
        # Input jumlah pembelian
        tk.Label(self.menu_frame, text="Jumlah Pembelian", bg="#7FA1C3").pack(pady=5)
        tk.Entry(self.menu_frame, textvariable=self.jumlah_beli_var).pack(pady=5)
        
        # Tombol hitung dan kembali
        tk.Button(self.menu_frame, text="Hitung", command=self.proses_pembelian, bg="#7FA1C3").pack(pady=10)
        tk.Button(self.menu_frame, text="Kembali", command=self.create_menu, bg="#7FA1C3").pack(pady=10)

    def proses_pembelian(self):
        # Mengambil data dari input pengguna
        nama_barang = self.nama_barang_var.get()
        jumlah_beli = self.jumlah_beli_var.get()

        # Validasi data
        if not nama_barang or jumlah_beli <= 0:
            messagebox.showerror("Error", "Data tidak valid")
            return

        # Mencari barang dan menghitung total pembayaran
        for barang in self.barang_list:
            if barang.nama == nama_barang:
                if barang.stok < jumlah_beli:
                    messagebox.showerror("Error", "Stok tidak cukup")
                    return
                
                total_bayar = barang.harga * jumlah_beli
                # Format total bayar dengan dua desimal
                formatted_total_bayar = f"{total_bayar:.2f}"
                formatted_stok = f"{barang.stok - jumlah_beli}"
                barang.stok -= jumlah_beli
                messagebox.showinfo("Info", f"Total Bayar: {formatted_total_bayar}\nSisa Stok: {formatted_stok}")
                self.create_menu()
                return
        
        messagebox.showerror("Error", "Barang tidak ditemukan")

if __name__ == "__main__":
    root = tk.Tk()
    app = BarangApp(root)
    root.mainloop()