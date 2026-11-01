# 6.9 FAVORITE PLACES
# Buat dictionary bernama favorite_places.
# Gunakan tiga nama orang sebagai key.
# Setiap orang memiliki satu sampai tiga tempat favorit.
# Gunakan perulangan untuk menampilkan nama dan seluruh tempat favorit masing-masing.

# Membuat dictionary berisi tempat favorit setiap orang
favorite_places = {
    "yasir": ["Rumah Celine", "Wonogiri", "Bandung"],
    "windah": ["Paris", "Tokyo"],
    "miook": ["Surakarta", "Malang", "Lombok"]
}

# Menampilkan nama dan tempat favorit setiap orang
for name, places in favorite_places.items():
    print(f"\nTempat favorit {name.title()}:")

    for place in places:
        print(f"- {place}")