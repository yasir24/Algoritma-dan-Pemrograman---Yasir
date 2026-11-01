# 3.7 SHRINKING GUEST LIST
# Meja makan yang baru ternyata tidak datang tepat waktu. Sekarang kamu hanya bisa mengundang dua 
# orang.
# Ada beberapa hal yang harus dilakukan:
# 1. Beri tahu bahwa kamu hanya bisa mengundang dua orang.
# 2. Gunakan pop() untuk menghapus tamu satu per satu sampai tersisa dua orang.
# 3. Berikan pesan maaf kepada tamu yang dihapus.
# 4. Beri tahu dua tamu yang tersisa bahwa mereka tetap diundang.
# 5. Gunakan del untuk menghapus dua nama terakhir.
# 6. Tampilkan list untuk memastikan sudah kosong.


guest_list = ["Yasir", "Ferry Irwandi", "dr. Tirta",
             "dr. Gia", "Windah", "Budi"]

# Memberi tahu bahwa hanya dua orang yang bisa diundang
print("Maaf, saya hanya bisa mengundang dua orang untuk makan malam.")

# Menghapus tamu satu per satu menggunakan pop()
guest = guest_list.pop()
print(f"Maaf {guest}, saya tidak bisa mengundang Anda untuk makan malam.")

guest = guest_list.pop()
print(f"Maaf {guest}, saya tidak bisa mengundang Anda untuk makan malam.")

guest = guest_list.pop()
print(f"Maaf {guest}, saya tidak bisa mengundang Anda untuk makan malam.")

guest = guest_list.pop()
print(f"Maaf {guest}, saya tidak bisa mengundang Anda untuk makan malam.")

# Memberi tahu dua tamu yang masih diundang
print("\nDua tamu yang masih diundang:")

print(f"Halo {guest_list[0]}, Anda tetap saya undang untuk makan malam.")
print(f"Halo {guest_list[1]}, Anda tetap saya undang untuk makan malam.")

# Menghapus dua nama terakhir menggunakan del
del guest_list[0]
del guest_list[0]

# Memastikan list sudah kosong
print("\nDaftar tamu setelah dihapus:")
print(guest_list)
