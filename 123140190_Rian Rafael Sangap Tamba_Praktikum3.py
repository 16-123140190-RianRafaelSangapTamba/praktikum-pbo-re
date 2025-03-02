# Membuka file "me.txt" dalam mode tulis ('w'). 
# Jika file sudah ada, file akan ditimpa (overwrite). Jika belum ada, file akan dibuat.
file = open("me.txt", "w")

# Menulis baris pertama ke dalam file. 
# "\n" digunakan untuk membuat baris baru setelah teks ini ditulis.
file.write("Masukkan Nama: Rian .\n")

# Menulis baris kedua ke dalam file dengan format yang sama. 
# "\n" juga digunakan untuk memulai baris baru setelahnya.
file.write("Masukkan Nim: 123140190.\n")

# Menulis baris ketiga ke dalam file.
# "\n" di akhir memastikan bahwa teks berikutnya akan dimulai pada baris baru jika ada.
file.write("Masukkan Resolusi di Tahun ini: Jadi Presiden.\n")

# Menutup file setelah selesai menulis.
# Penting untuk menutup file agar perubahan disimpan dengan benar.
file.close()

# Menampilkan pesan di console. Ini hanya contoh tampilan terminal dan tidak ada hubungannya dengan file.
# Menggunakan f-string (walaupun tidak ada variabel yang dimasukkan dalam string).
print(f"rian@tamba MINGW64 /C/Riiiiian/py")