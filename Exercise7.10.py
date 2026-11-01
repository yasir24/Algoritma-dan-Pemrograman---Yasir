# 7.10 DREAM VACATION
# Buat program polling yang menanyakan tempat impian yang ingin dikunjungi pengguna. Simpan 
# setiap jawaban ke dalam sebuah dictionary, kemudian tampilkan seluruh hasil polling.

responses = {}

polling_active = True

while polling_active:
    name = input("\nSiapa nama Anda? ")
    destination = input(
        "Jika bisa mengunjungi satu tempat di dunia, "
        "ke mana Anda ingin pergi? "
    )

    responses[name] = destination

    repeat = input(
        "\nApakah ada orang lain yang ingin mengikuti polling? (ya/tidak) "
    )

    if repeat.lower() == "tidak":
        polling_active = False

print("\n===== HASIL POLLING =====")

for name, destination in responses.items():
    print(f"{name} ingin mengunjungi {destination}.")