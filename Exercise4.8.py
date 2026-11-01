# 4.8 CUBES
# Pangkat tiga dari sebuah angka disebut cube.
# Contohnya, pangkat tiga dari 2 ditulis 2**3 dalam Python.
# Buat list berisi hasil pangkat tiga dari bilangan bulat 1 sampai 10.
#Gunakan for loop untuk menampilkan setiap hasilnya.

# Membuat list kosong
cubes = []

# Menghitung pangkat tiga dari angka 1 sampai 10
for number in range(1, 11):
    cube = number ** 3
    cubes.append(cube)

# Menampilkan hasil pangkat tiga
for cube in cubes:
    print(cube)