# 3.6 MORE GUESTS
# Kamu menemukan meja makan yang lebih besar sehingga bisa mengundang tiga orang tambahan.
# Ada empat hal yang harus dilakukan:
# 1. Beri tahu semua orang bahwa kamu menemukan meja yang lebih besar.
# 2. Gunakan insert() untuk menambahkan satu tamu di awal list.
# 3. Gunakan insert() untuk menambahkan satu tamu di tengah list.
# 4. Gunakan append() untuk menambahkan satu tamu di akhir list.
# 5. Tampilkan kembali seluruh undangan.


guest_list = ["Yasir", "Azhar", "Pria Solo"]

# Memberi tahu tamu bahwa meja lebih besar sudah tersedia
print("Kabar baik! Saya menemukan meja makan yang lebih besar.")

# Menambahkan tamu di awal list
guest_list.insert(0, "Prabowo")

# Menambahkan tamu di tengah list
guest_list.insert(2, "Teddy")

# Menambahkan tamu di akhir list
guest_list.append("Windah")

# Menampilkan seluruh undangan
print("\nDaftar undangan terbaru:")

print(f"Halo {guest_list[0]}, saya ingin mengundang Anda untuk makan malam.")
print(f"Halo {guest_list[1]}, saya ingin mengundang Anda untuk makan malam.")
print(f"Halo {guest_list[2]}, saya ingin mengundang Anda untuk makan malam.")
print(f"Halo {guest_list[3]}, saya ingin mengundang Anda untuk makan malam.")
print(f"Halo {guest_list[4]}, saya ingin mengundang Anda untuk makan malam.")
print(f"Halo {guest_list[5]}, saya ingin mengundang Anda untuk makan malam.")
