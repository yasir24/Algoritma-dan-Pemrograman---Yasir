# 8.4 LARGE SHIRTS
# Modifikasi fungsi make_shirt() agar ukuran default-nya L dan tulisan default-nya I love Python. 
# Buat kaos ukuran besar dan sedang dengan tulisan default, serta kaos dengan ukuran bebas dan 
# tulisan berbeda.

def make_shirt(size="L", message="I love Python"):
    print(
        f"Ukuran kaos: {size}. "
        f"Tulisan pada kaos: {message}."
    )


# Kaos ukuran besar dengan tulisan default
make_shirt()

# Kaos ukuran sedang dengan tulisan default
make_shirt(size="M")

# Kaos ukuran bebas dengan tulisan berbeda
make_shirt("S", "Teknik Industri")