# 5.9 NO USERS
# Tambahkan pengecekan untuk memastikan list username tidak kosong.
# Jika kosong, tampilkan pesan "Kita perlu mencari beberapa pengguna!".
# Jika tidak kosong, jalankan program sapaan seperti latihan 5-8.
# Kosongkan list dan pastikan pesan yang benar muncul

usernames = []

if usernames:
    for username in usernames:
        if username == "admin":
            print("Halo admin, apakah kamu ingin melihat laporan status?")
        else:
            print(f"Halo {username}, terima kasih sudah login kembali.")
else:
    print("Kita perlu mencari beberapa pengguna!")

