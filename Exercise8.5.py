# 8.5 CITIES
# Buat fungsi describe_city() yang menerima nama kota dan negara. Parameter negara harus memiliki 
# nilai default. Panggil fungsi untuk tiga kota berbeda, minimal satu kota berada di luar negara 
# default.

def describe_city(city, country="Indonesia"):
    print(f"{city} berada di {country}.")


describe_city("Surakarta")
describe_city("Bandung")
describe_city("Tokyo", "Jepang")