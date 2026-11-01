# 7.9 NO PASTRAMI
# Gunakan daftar sandwich_orders dari latihan sebelumnya. Pastikan terdapat minimal tiga pesanan 
# pastrami. Tampilkan pesan bahwa pastrami habis, kemudian hapus seluruh pesanan pastrami 
# menggunakan while. Pastikan tidak ada pastrami yang masuk ke finished_sandwiches.

sandwich_orders = [
    "tuna",
    "pastrami",
    "chicken",
    "pastrami",
    "beef",
    "pastrami",
    "cheese"
]

finished_sandwiches = []

print("Maaf, deli kehabisan pastrami!")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)

    print(f"Saya sudah membuat sandwich {current_sandwich}.")

    finished_sandwiches.append(current_sandwich)

print("\nDaftar sandwich yang sudah selesai dibuat:")

for sandwich in finished_sandwiches:
    print(f"- {sandwich}")