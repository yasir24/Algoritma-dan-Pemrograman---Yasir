# 5.10 CHECKING USERNAMES
# Buat list current_users berisi minimal lima username.
# Buat list new_users berisi lima username.
# Pastikan satu atau dua username baru sudah digunakan.
# Periksa apakah username baru tersedia.
# Perbandingan harus tidak membedakan huruf kapital dan kecil (case insensitive).

current_users = ["admin", "yasir", "budi", "windah", "miook"]

new_users = ["Jokowi", "Pria Solo", "Dina", "Budi", "Rafi"]

# Membuat salinan username dalam huruf kecil
current_users_lower = []

for username in current_users:
    current_users_lower.append(username.lower())

# Memeriksa username baru
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Username {new_user} sudah digunakan. Silakan pilih username lain.")
    else:
        print(f"Username {new_user} tersedia.")