# 6.3 GLOSSARY
# Buat dictionary bernama glossary.
# Pilih lima istilah pemrograman yang sudah dipelajari pada bab sebelumnya.
# Gunakan istilah sebagai key dan pengertiannya sebagai value.
# Tampilkan setiap istilah beserta pengertiannya.
# Gunakan \n untuk memberikan baris kosong di antara setiap istilah.

# Membuat dictionary berisi istilah pemrograman
glossary = {
    "variable": "Tempat untuk menyimpan suatu nilai.",
    "list": "Tipe data untuk menyimpan kumpulan elemen.",
    "loop": "Struktur untuk mengulang suatu perintah.",
    "if_statement": "Struktur untuk menjalankan kode berdasarkan kondisi.",
    "dictionary": "Tipe data yang menyimpan pasangan key dan value."
}

# Menampilkan istilah dan pengertiannya
print("KAMUS ISTILAH PEMROGRAMAN\n")

for word, meaning in glossary.items():
    print(f"{word.upper()}:")
    print(f"    {meaning}\n")