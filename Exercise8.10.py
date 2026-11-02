# 8.10 SENDING MESSAGES
# Kembangkan latihan 8-9 dengan membuat fungsi send_messages(). Fungsi harus menampilkan setiap 
# pesan dan memindahkannya ke list baru bernama sent_messages. Setelah fungsi dipanggil, tampilkan 
# kedua list.

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


send_messages(messages, sent_messages)

print("\nDaftar pesan awal:")
print(messages)

print("\nDaftar pesan terkirim:")
print(sent_messages)