def buat_piramida(height):
    # Iterasi untuk setiap baris
    for i in range(1, height + 1):
        # Mencetak spasi agar segitiga terlihat rata di tengah
        spasi = ' ' * (height - i)
        # Mencetak bintang untuk membentuk segitiga
        bintang = '*' * (2 * i - 1)
        # Gabungkan spasi dan bintang, kemudian print hasilnya
        print(spasi + bintang)
# Minta input tinggi piramida dari pengguna
height = int(input("Input Tinggi 5: "))
buat_piramida(height)