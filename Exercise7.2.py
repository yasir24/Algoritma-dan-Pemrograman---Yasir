# 7.2 RESTAURANT SEATING
# Tanyakan kepada pengguna berapa jumlah orang dalam kelompok makan malamnya.
# Jika jumlahnya lebih dari 8 orang, tampilkan pesan bahwa mereka harus menunggu meja.
# Jika jumlahnya 8 orang atau kurang, tampilkan pesan bahwa meja sudah tersedia

# Menanyakan jumlah orang dalam kelompok
group_size = int(input("Ada berapa orang dalam kelompok makan malam Anda? "))

# Memeriksa jumlah orang
if group_size > 8:
    print("Maaf, Anda harus menunggu meja tersedia.")
else:
    print("Meja Anda sudah siap!")