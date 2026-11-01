# 6.4 GLOSSARY 2
# Gunakan kembali dictionary glossary dari latihan 6-3.
# Ganti beberapa perintah print() menjadi satu perulangan for.
# Tambahkan lima istilah Python baru beserta pengertiannya.
# Pastikan semua istilah baru otomatis muncul ketika program dijalankan.

# Membuat dictionary berisi istilah pemrograman
glossary = {
    "variable": "Tempat untuk menyimpan suatu nilai.",
    "list": "Tipe data untuk menyimpan kumpulan elemen.",
    "loop": "Struktur untuk mengulang suatu perintah.",
    "if_statement": "Struktur untuk menjalankan kode berdasarkan kondisi.",
    "dictionary": "Tipe data yang menyimpan pasangan key dan value.",
    "string": "Tipe data untuk menyimpan kumpulan karakter.",
    "integer": "Tipe data untuk menyimpan bilangan bulat.",
    "float": "Tipe data untuk menyimpan bilangan desimal.",
    "boolean": "Tipe data yang memiliki nilai True atau False.",
    "function": "Blok kode yang dibuat untuk menjalankan tugas tertentu."
}

# Menampilkan seluruh istilah dan pengertiannya
for word, meaning in glossary.items():
    print(f"{word.upper()}:")
    print(f"    {meaning}\n")