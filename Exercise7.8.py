# 7.8 DELI
# Buat daftar pesanan sandwich bernama sandwich_orders dan daftar kosong finished_sandwiches. 
# Proses setiap pesanan, tampilkan pesan bahwa sandwich sudah dibuat, lalu pindahkan pesanan 
# tersebut ke daftar sandwich yang selesai dibuat. Terakhir, tampilkan semua sandwich yang sudah 
# selesai.

sandwich_orders = [
    "tuna",
    "chicken",
    "beef",
    "egg",
    "cheese"
]

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)

    print(f"Saya sudah membuat sandwich {current_sandwich}.")

    finished_sandwiches.append(current_sandwich)

print("\nDaftar sandwich yang sudah selesai dibuat:")

for sandwich in finished_sandwiches:
    print(f"- {sandwich}")