# 8.6 CIT NAMES
# Buat fungsi city_country() yang menerima nama kota dan negara, kemudian mengembalikan string 
# dengan format "Kota, Negara". Panggil fungsi minimal tiga kali dan tampilkan hasilnya.

def city_country(city, country):
    return f"{city}, {country}"


result1 = city_country("Surakarta", "Indonesia")
result2 = city_country("Ngawi barat", "Rongawi Kingdom")
result3 = city_country("Ngawi Selatan", "Rongawi Kingdom")

print(result1)
print(result2)
print(result3)