import tkinter as tk
from tkinter import messagebox
import math

class BangunDatarApp:
    def __init__(self, utama):
        self.utama = utama
        self.utama.title("Perhitungan Bangun Datar")
        self.utama.minsize(300, 300)
        self.utama.configure(bg="light sea green")

        # Garis di atas judul
        self.garis_diatas_judul = tk.Canvas(utama, height=2, bd=0, highlightthickness=0, bg="black")
        self.garis_diatas_judul.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(10, 0))

        # Label judul
        self.label_judul = tk.Label(utama, text="Perhitungan Bangun Datar", justify=tk.CENTER, font=("Helvetica", 19, "bold"), bg="light sea green")
        self.label_judul.grid(row=1, column=0, columnspan=2, pady=10)

        # Garis di bawah judul
        self.garis_dibawah_judul = tk.Canvas(utama, height=2, bd=0, highlightthickness=0, bg="black")
        self.garis_dibawah_judul.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(0, 10))

        # Garis di atas pilih bangun datar
        self.garis_atas_pilih = tk.Canvas(utama, height=2, bd=0, highlightthickness=0, bg="black")
        self.garis_atas_pilih.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(10, 0))

        # Label untuk memilih bangun datar
        self.label_pilih = tk.Label(utama, text="Pilih Bangun Datar", justify=tk.LEFT, font=("Helvetica", 14, "bold"), bg="light sea green")
        self.label_pilih.grid(row=4, column=0, columnspan=2, pady=10)

        # Garis di bawah pilih bangun datar
        self.garis_bawah_pilih = tk.Canvas(utama, height=2, bd=0, highlightthickness=0, bg="black")
        self.garis_bawah_pilih.grid(row=5, column=0, columnspan=2, sticky="ew", pady=(0, 10))

        # Tombol pilihan bangun datar
        self.tombol_segiempat = tk.Button(utama, text="Segi Empat", command=lambda: self.show_inputs("Segi Empat"))
        self.tombol_segiempat.grid(row=6, column=0, columnspan=2, pady=5)

        self.tombol_persegipanjang = tk.Button(utama, text="Persegi Panjang", command=lambda: self.show_inputs("Persegi Panjang"))
        self.tombol_persegipanjang.grid(row=7, column=0, columnspan=2, pady=5)

        self.tombol_segitiga = tk.Button(utama, text="Segitiga", command=lambda: self.show_inputs("Segitiga"))
        self.tombol_segitiga.grid(row=8, column=0, columnspan=2, pady=5)

        self.tombol_lingkaran = tk.Button(utama, text="Lingkaran", command=lambda: self.show_inputs("Lingkaran"))
        self.tombol_lingkaran.grid(row=9, column=0, columnspan=2, pady=5)

        # Label dan Entry untuk masukan
        self.input_fields = {}
        self.create_input_fields()

        # Tombol untuk menghitung
        self.calculate_button = tk.Button(utama, text="Hitung", command=self.calculate)
        self.calculate_button.grid(row=13, column=0, columnspan=2, pady=10)

        # Garis di atas output
        self.garis_atas_output = tk.Canvas(utama, height=2, bd=0, highlightthickness=0, bg="black")
        self.garis_atas_output.grid(row=14, column=0, columnspan=2, sticky="ew", pady=(10, 0))

        # Label untuk hasil
        self.result_label = tk.Label(utama, text="", justify=tk.LEFT, font=("Helvetica", 10, "bold"), bg="light sea green")
        self.result_label.grid(row=15, column=0, columnspan=2, pady=10)

        # Garis di bawah output
        self.garis_dibawah_output = tk.Canvas(utama, height=2, bd=0, highlightthickness=0, bg="black")
        self.garis_dibawah_output.grid(row=16, column=0, columnspan=2, sticky="ew", pady=(0, 10))

        # Tombol Clear dan Pause
        self.clear_button = tk.Button(utama, text="Clear", command=self.clear_input)
        self.clear_button.grid(row=17, column=0, pady=10)

        self.pause_button = tk.Button(utama, text="Pause", command=self.pause)
        self.pause_button.grid(row=17, column=1, pady=10)

    def create_input_fields(self):
        self.labels = {}
        labels_text = ["Nilai 1", "Nilai 2", "Nilai 3"]
        for i, text in enumerate(labels_text):
            label = tk.Label(self.utama, text=text, font=("Helvetica", 10, "bold"), bg="light sea green")
            label.grid(row=i+10, column=0, padx=10, pady=5)
            entry = tk.Entry(self.utama)
            entry.grid(row=i+10, column=1, padx=10, pady=5)
            self.labels[text] = label
            self.input_fields[text] = entry

        # Hapus semua input fields di awal
        self.hide_all_inputs()

    def hide_all_inputs(self):
        for label in self.labels.values():
            label.grid_remove()
        for entry in self.input_fields.values():
            entry.grid_remove()

    def show_inputs(self, shape):
        self.hide_all_inputs()
        self.current_shape = shape

        if shape == "Segi Empat" or shape == "Lingkaran":
            self.labels["Nilai 1"].config(text="Sisi" if shape == "Segi Empat" else "Radius")
            self.labels["Nilai 1"].grid()
            self.input_fields["Nilai 1"].grid()
        elif shape == "Persegi Panjang":
            self.labels["Nilai 1"].config(text="Panjang")
            self.labels["Nilai 2"].config(text="Lebar")
            self.labels["Nilai 1"].grid()
            self.labels["Nilai 2"].grid()
            self.input_fields["Nilai 1"].grid()
            self.input_fields["Nilai 2"].grid()
        elif shape == "Segitiga":
            self.labels["Nilai 1"].config(text="Alas")
            self.labels["Nilai 2"].config(text="Tinggi")
            self.labels["Nilai 3"].config(text="Sisi Miring")
            self.labels["Nilai 1"].grid()
            self.labels["Nilai 2"].grid()
            self.labels["Nilai 3"].grid()
            self.input_fields["Nilai 1"].grid()
            self.input_fields["Nilai 2"].grid()
            self.input_fields["Nilai 3"].grid()

    def calculate(self):
        try:
            if self.current_shape == "Segi Empat":
                sisi = float(self.input_fields["Nilai 1"].get())
                luas, keliling = self.calculate_square(sisi)
            elif self.current_shape == "Persegi Panjang":
                panjang = float(self.input_fields["Nilai 1"].get())
                lebar = float(self.input_fields["Nilai 2"].get())
                luas, keliling = self.calculate_rectangle(panjang, lebar)
            elif self.current_shape == "Segitiga":
                alas = float(self.input_fields["Nilai 1"].get())
                tinggi = float(self.input_fields["Nilai 2"].get())
                sisi_miring = float(self.input_fields["Nilai 3"].get())
                luas, keliling = self.calculate_triangle(alas, tinggi, sisi_miring)
            elif self.current_shape == "Lingkaran":
                radius = float(self.input_fields["Nilai 1"].get())
                luas, keliling = self.calculate_circle(radius)

            self.result_label.config(text=f"Luas {self.current_shape}: {luas:.2f}\nKeliling {self.current_shape}: {keliling:.2f}")

        except ValueError:
            messagebox.showerror("Error", "Input tidak valid")

    def calculate_square(self, sisi):
        luas = sisi ** 2
        keliling = 4 * sisi
        return luas, keliling

    def calculate_rectangle(self, panjang, lebar):
        luas = panjang * lebar
        keliling = 2 * (panjang + lebar)
        return luas, keliling

    def calculate_triangle(self, alas, tinggi, sisi_miring):
        luas = 0.5 * alas * tinggi
        keliling = alas + tinggi + sisi_miring
        return luas, keliling

    def calculate_circle(self, radius):
        luas = math.pi * radius ** 2
        keliling = 2 * math.pi * radius
        return luas, keliling
    
    def clear_input(self):
        """Function to clear all input fields and hide results."""
        for entry in self.input_fields.values():
            entry.delete(0, tk.END)
        self.result_label.config(text="")

    def pause(self):
        """Function to simulate pause by showing a message box."""
        messagebox.showinfo("Pause", "Press OK to continue...")

if __name__ == "__main__":
    utama = tk.Tk()
    app = BangunDatarApp(utama)
    
    # Adding buttons for clear and pause functionality
    utama.mainloop()