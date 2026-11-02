# 8.3 T-SHIRT
# Buat fungsi make_shirt() yang menerima dua parameter, yaitu ukuran baju dan tulisan pada baju. 
# Panggil fungsi menggunakan positional arguments dan keyword arguments.

def make_shirt(size, message):
    print(
        f"Ukuran kaos: {size}. "
        f"Tulisan pada kaos: {message}."
    )


# Menggunakan positional arguments
make_shirt("L", "Tetap Semangat")

# Menggunakan keyword arguments
make_shirt(size="M", message="Belajar Python")