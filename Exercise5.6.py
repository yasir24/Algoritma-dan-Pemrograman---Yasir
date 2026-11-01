# 5.6 STAGES OF LIFE
# Buat rangkaian if-elif-else untuk menentukan tahapan kehidupan seseorang berdasarkan usia.
# Ketentuan:
# 1. Usia kurang dari 2 tahun: bayi (baby).
# 2. Usia minimal 2 tahun tetapi kurang dari 4 tahun: balita (toddler).
# 3. Usia minimal 4 tahun tetapi kurang dari 13 tahun: anak-anak (kid).
# 4. Usia minimal 13 tahun tetapi kurang dari 20 tahun: remaja (teenager).
# 5. Usia minimal 20 tahun tetapi kurang dari 65 tahun: dewasa (adult).
# 6. Usia 65 tahun atau lebih: lansia (elder).

age = 19

if age < 2:
    print("Kamu masih bayi.")
elif age < 4:
    print("Kamu masih balita.")
elif age < 13:
    print("Kamu masih anak-anak.")
elif age < 20:
    print("Kamu masih remaja.")
elif age < 65:
    print("Kamu sudah dewasa.")
else:
    print("Kamu sudah lanjut usia.")

