# 7.7 PIZZA TOPPINGS
# Buat program yang meminta pengguna memasukkan topping pizza.
#Pengguna bisa memasukkan topping berkali-kali.
# Setiap kali pengguna memasukkan topping, tampilkan pesan bahwa topping tersebut akan ditambahkan.
# Program berhenti ketika pengguna mengetik quit.

# Meminta topping pizza dari pengguna
topping = ""

while topping != "quit":
    topping = input("Masukkan topping pizza (ketik quit untuk selesai): ")

    if topping != "quit":
        print(f"Menambahkan {topping} ke pizza Anda.")

print("Pemesanan pizza selesai!")