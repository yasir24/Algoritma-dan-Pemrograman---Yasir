# 6.5 RIVERS
# Buat dictionary berisi tiga sungai besar dan negara tempat sungai tersebut mengalir.
# Gunakan perulangan untuk:
# 1. Menampilkan kalimat tentang setiap sungai dan negaranya.
# 2. Menampilkan seluruh nama sungai.
# 3. Menampilkan seluruh nama negara.

# Membuat dictionary berisi sungai dan negara
rivers = {
    "nil": "mesir",
    "amazon": "brasil",
    "gangga": "india"
}

# Menampilkan informasi sungai dan negara
print("INFORMASI SUNGAI")

for river, country in rivers.items():
    print(f"Sungai {river.title()} mengalir melalui {country.title()}.")

# Menampilkan seluruh nama sungai
print("\nDAFTAR SUNGAI")

for river in rivers.keys():
    print(river.title())

# Menampilkan seluruh nama negara
print("\nDAFTAR NEGARA")

for country in rivers.values():
    print(country.title())