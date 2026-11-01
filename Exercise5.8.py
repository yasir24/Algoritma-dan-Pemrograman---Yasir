# 5.8 HELLO ADMIN
# Buat list minimal lima username, termasuk admin.
# Lakukan perulangan menggunakan for.
# Jika username adalah admin, tampilkan sapaan khusus.
# Jika bukan admin, tampilkan sapaan umum.

usernames = ["admin", "jaden", "budi", "sarah", "andi"]

for username in usernames:
    if username == "admin":
        print("Halo admin, apakah kamu ingin melihat laporan status?")
    else:
        print(f"Halo {username}, terima kasih sudah login kembali.")

