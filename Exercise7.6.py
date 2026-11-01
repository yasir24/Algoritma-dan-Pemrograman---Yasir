# 7.6 THREE EXITS
# Buat tiga versi program dari latihan 7-4 atau 7-5. Setiap versi harus menggunakan cara berbeda untuk menghentikan perulangan:
# 1. Menggunakan kondisi pada pernyataan while.
# 2. Menggunakan variabel aktif (active variable).
# 3. Menggunakan pernyataan break.

# coditional test dalam while
# Meminta topping pizza dari pengguna
topping = ""

while topping != "quit":
    topping = input("Masukkan topping (ketik quit untuk selesai): ")

    if topping != "quit":
        print(f"Menambahkan {topping} ke pizza Anda.")

print("Pemesanan selesai!")

# menggunakan variabel aktif
# Menentukan kondisi awal perulangan
active = True

while active:
    topping = input("Masukkan topping (ketik quit untuk selesai): ")

    if topping == "quit":
        active = False
    else:
        print(f"Menambahkan {topping} ke pizza Anda.")

print("Pemesanan selesai!")

# menggunakan pernyataan break
# Memulai perulangan
while True:
    topping = input("Masukkan topping (ketik quit untuk selesai): ")

    if topping == "quit":
        break

    print(f"Menambahkan {topping} ke pizza Anda.")

print("Pemesanan selesai!")