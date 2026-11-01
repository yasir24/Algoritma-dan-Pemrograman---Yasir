# 5.11 ORDINAL NUMBERS
# Simpan angka 1 sampai 9 dalam sebuah list.
# Lakukan perulangan menggunakan for.
# Gunakan rangkaian if-elif-else untuk menentukan akhiran angka.
# Angka 1, 2, dan 3 memiliki akhiran khusus (st, nd, rd), sedangkan angka lainnya menggunakan th

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")