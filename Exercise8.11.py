# 8.11 ARCHIVED MESSAGES
# Gunakan program dari latihan 8-10. Namun, ketika memanggil fungsi send_messages(), berikan salinan 
# list menggunakan slicing [:]. Tujuannya agar list asli tetap memiliki seluruh pesan.

messages = [
    "Selamat pagi!",
    "Tetap semangat belajar!",
    "Jangan lupa istirahat.",
    "Teruslah mencoba hal baru."
]

sent_messages = []


def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)

        print(f"Mengirim pesan: {current_message}")

        sent_messages.append(current_message)


send_messages(messages[:], sent_messages)

print("\nDaftar pesan asli:")
print(messages)

print("\nDaftar pesan terkirim:")
print(sent_messages)