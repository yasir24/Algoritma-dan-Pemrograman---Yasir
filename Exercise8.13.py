# 8.13 USER PROFILE
# Buat fungsi build_profile() yang menerima nama depan, nama belakang, dan sejumlah pasangan 
# key-value tambahan. Gunakan fungsi tersebut untuk membuat profil diri dengan tiga informasi 
# tambahan.

def build_profile(first, last, **user_info):
    profile = {
        "first_name": first,
        "last_name": last
    }

    for key, value in user_info.items():
        profile[key] = value

    return profile


my_profile = build_profile(
    "Muhammad",
    "Yasir",
    umur=19,
    jurusan="Teknik Industri",
    universitas="Universitas Sebelas Maret"
)

print(my_profile)