# Gunakan variabel untuk menyimpan nama seseorang dengan tambahan whitespace 
# (karakter kosong) di awal dan akhir. Gunakan \t dan \n, 
# kemudian tampilkan nama asli dan hasil dari tiga method stripping.
nama = "\t Muhammad Yasir \n"
print(f"Nama asli: '{nama}'")
print(f"Nama setelah lstrip(): '{nama.lstrip()}'")
print(f"Nama setelah rstrip(): '{nama.rstrip()}'")
print(f"Nama setelah strip(): '{nama.strip()}'")