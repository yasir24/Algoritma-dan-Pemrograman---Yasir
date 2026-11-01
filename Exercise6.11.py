# 6.11 CITIES
# Buat dictionary bernama cities.
# Gunakan tiga nama kota sebagai key.
# Setiap kota memiliki dictionary sendiri yang berisi:
# - country: negara tempat kota berada.
# - population: perkiraan jumlah penduduk.
# - fact: fakta menarik tentang kota tersebut.
# Tampilkan nama kota dan seluruh informasinya.

# Membuat dictionary berisi informasi tiga kota
cities = {
    "surakarta": {
        "country": "Indonesia",
        "population": 522364,
        "fact": "Dikenal sebagai Kota Batik."
    },

    "yogyakarta": {
        "country": "Indonesia",
        "population": 373589,
        "fact": "Memiliki kawasan wisata Malioboro."
    },

    "semarang": {
        "country": "Indonesia",
        "population": 1653524,
        "fact": "Memiliki bangunan bersejarah Lawang Sewu."
    }
}

# Menampilkan informasi setiap kota
for city, information in cities.items():
    print(f"\nNama kota: {city.title()}")
    print(f"Negara: {information['country']}")
    print(f"Populasi: {information['population']:,} jiwa")
    print(f"Fakta: {information['fact']}")