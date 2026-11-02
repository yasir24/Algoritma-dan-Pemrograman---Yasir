# 8.12 SANDWICHES
# Buat fungsi yang menerima sejumlah argumen berupa daftar bahan sandwich yang diinginkan seseorang. 
# Fungsi harus menampilkan ringkasan sandwich yang dipesan. Panggil fungsi sebanyak tiga kali dengan 
# jumlah argumen berbeda.

def make_sandwich(*items):
    print("\nSandwich yang dipesan memiliki bahan:")

    for item in items:
        print(f"- {item}")


make_sandwich("keju", "telur")
make_sandwich("ayam", "selada", "tomat")
make_sandwich("daging", "keju", "saus", "bawang")