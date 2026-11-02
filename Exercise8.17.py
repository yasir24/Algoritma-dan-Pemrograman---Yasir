# 8.17 STYLING FUNCTIONS
# Pilih tiga program yang sudah dibuat pada bab ini, kemudian rapikan kode agar mengikuti 
# pedoman penulisan Python (PEP 8).

# perbaikan latihan 8.3
def make_shirt(size, message):
    print(
        f"Ukuran kaos: {size}. "
        f"Tulisan pada kaos: {message}."
    )


make_shirt("L", "Tetap Semangat")
make_shirt(size="M", message="Belajar Python")

# perbaikan latihan 8.7
def make_album(artist, title, num_songs=None):
    album = {
        "artist": artist,
        "title": title
    }

    if num_songs is not None:
        album["num_songs"] = num_songs

    return album


album1 = make_album("Lany", "you!")
album2 = make_album("Hindia", "Cincin")
album3 = make_album("Perunggu", "Pikiran yang Matang", 10)

print(album1)
print(album2)
print(album3)

# perbaikan latihan 8.12
def make_sandwich(*items):
    print("\nSandwich yang dipesan memiliki bahan:")

    for item in items:
        print(f"- {item}")


make_sandwich("keju", "telur")
make_sandwich("ayam", "selada", "tomat")
make_sandwich("daging", "keju", "saus", "bawang")

