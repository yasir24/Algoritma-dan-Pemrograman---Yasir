# 8.7 ALBUM
# Buat fungsi make_album() yang menerima nama artis dan judul album, kemudian mengembalikan 
# dictionary berisi informasi tersebut. Tambahkan parameter opsional num_songs dengan nilai 
# default None. Jika jumlah lagu diberikan, masukkan ke dictionary.

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
album3 = make_album("Perunggu", "Pikiran yang matang")
album4 = make_album("Olivia Rodrigo", "u + me = <3", 10)

print(album1)
print(album2)
print(album3)
print(album4)