# 6.6 POLLING
# Buat dictionary favorite_languages yang menyimpan nama orang dan bahasa pemrograman favoritnya.
# Buat list people berisi orang-orang yang perlu mengikuti polling.
# Masukkan beberapa nama yang sudah ada dan belum ada dalam dictionary.
# Gunakan perulangan untuk memeriksa apakah seseorang sudah mengikuti polling.
# Jika sudah, tampilkan ucapan terima kasih.
# Jika belum, tampilkan undangan untuk mengikuti polling.

# Membuat dictionary berisi bahasa pemrograman favorit
favorite_languages = {
    "yasir": "python",
    "windah": "c",
    "miook": "rust",
    "pria solo": "python"
}

# Membuat daftar orang yang perlu mengikuti polling
people = ["yasir", "windah", "miook", "pria solo", "budi", "andi", "phil", "dina"]

# Memeriksa siapa yang sudah mengikuti polling
for person in people:
    if person in favorite_languages:
        print(f"Terima kasih {person.title()}, sudah mengikuti polling.")
    else:
        print(f"{person.title()}, silakan ikuti polling bahasa favorit.")