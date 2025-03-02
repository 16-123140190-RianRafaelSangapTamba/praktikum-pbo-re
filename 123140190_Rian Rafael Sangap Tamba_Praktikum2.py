# Membuat sebuah dictionary kosong untuk menyimpan nama siswa dan nilai mereka
siswa_dict = {}

# Menanyakan berapa banyak siswa yang ingin dimasukkan
jumlah_siswa = int(input("Masukkan jumlah siswa: "))

# Perulangan untuk meminta data siswa berdasarkan jumlah yang diinputkan
for i in range(1, jumlah_siswa + 1):
    nama = input(f"Masukkan nama siswa ke-{i}: ")
    nilai = int(input(f"Masukkan nilai untuk {nama}: "))
    
    # Menambahkan nama siswa dan nilai mereka ke dalam dictionary
    siswa_dict[nama] = nilai

# Menampilkan isi dictionary setelah semua data dimasukkan
print("\nDictionary yang dibuat:", siswa_dict)
