# 8.8 USER ALBUMS
# Gunakan fungsi make_album() dari latihan 8-7. Buat while loop agar pengguna bisa memasukkan 
# nama artis dan judul album. Program harus memiliki perintah untuk berhenti (quit).

def make_album(artist, title):
    album = {
        "artist": artist,
        "title": title
    }

    return album


while True:
    print("\nMasukkan informasi album:")
    print("(Ketik 'quit' untuk berhenti)")

    artist = input("Nama artis: ")

    if artist.lower() == "quit":
        break

    title = input("Judul album: ")

    if title.lower() == "quit":
        break

    album = make_album(artist, title)

    print(album)