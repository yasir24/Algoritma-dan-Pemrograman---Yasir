# 8.9 MESSAGES
# Buat list berisi beberapa pesan singkat. Berikan list tersebut kepada fungsi show_messages() 
# untuk ditampilkan satu per satu.

messages = [
    "Selamat pagi!",
    "Tetap semangat belajar!",
    "Jangan lupa istirahat.",
    "Teruslah mencoba hal baru."
]


def show_messages(messages):
    for message in messages:
        print(message)


show_messages(messages)