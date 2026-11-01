# 6.10 FAVORITE NUMBERS
# Modifikasi program latihan 6-2.
# Setiap orang sekarang boleh memiliki lebih dari satu angka favorit.
# Simpan angka favorit dalam bentuk list.
# Tampilkan nama setiap orang dan seluruh angka favoritnya.

# Membuat dictionary berisi beberapa angka favorit
favorite_numbers = {
    "budi": [7, 10, 15],
    "yasir": [12, 5],
    "windah": [3, 8, 20],
    "miook": [6, 9],
    "nara": [25, 50]
}

# Menampilkan angka favorit setiap orang
for name, numbers in favorite_numbers.items():
    print(f"\nAngka favorit {name.title()}:")

    for number in numbers:
        print(f"- {number}")