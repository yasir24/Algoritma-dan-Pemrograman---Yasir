# 3.5 CHANGING GUEST LIST
# Salah satu tamu ternyata tidak bisa menghadiri makan malam. Kamu harus mengganti tamu tersebut 
# dengan orang lain.

# Ada tiga hal yang harus dilakukan:
# 1. Tampilkan nama tamu yang tidak bisa hadir.
# 2. Ganti nama tamu tersebut dengan orang baru.
# 3. Tampilkan kembali seluruh pesan undangan.


guest_list = ["Yasir", "Azhar", "Jokowi"]

# Menampilkan tamu yang tidak bisa hadir
print(f"{guest_list[1]} tidak bisa menghadiri makan malam.")

# Mengganti tamu yang tidak bisa hadir
guest_list[1] = "Prabowo"

# Mengirimkan undangan baru
print("\nUndangan makan malam terbaru:")

print(f"Halo {guest_list[0]}, saya ingin mengundang Anda untuk makan malam.")
print(f"Halo {guest_list[1]}, saya ingin mengundang Anda untuk makan malam.")
print(f"Halo {guest_list[2]}, saya ingin mengundang Anda untuk makan malam.")
