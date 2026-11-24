# Desain Program (Milestone 1)

Kumpulkan bersama `docs/flowchart.pdf` **sebelum** menulis kode di `app/core/`.

## 1. Struktur data

| Tahap | Bentuk data | Contoh | Alasan memilih bentuk ini |
| --- | --- | --- | --- |
| Hasil baca Excel |  |  |  |
| Setelah dibersihkan |  |  |  |
| Hasil perhitungan utama |  |  |  |
| Data yang disimpan di `keadaan` (ui.py) |  |  |  |

## 2. Algoritma pengurutan

Jelaskan langkah odd-even transposition sort: putaran genap membandingkan pasangan (0,1), (2,3), ...; putaran ganjil pasangan (1,2), (3,4), ...; berhenti jika dua putaran berturut-turut tanpa pertukaran dengan contoh 5 data, termasuk dua data bernilai sama, dan tunjukkan mengapa hasilnya stabil.

## 3. Pseudocode fungsi inti

Tulis pseudocode atau flowchart untuk minimal: `urutkan`, `cari_biner`, `uraikan_bom`, `hitung_mrp_item`, `jalankan_mrp`.

## 4. Rancangan menu

Gambarkan alur menu utama (perulangan, pilihan, validasi input, keluar).

## 5. Penanganan kesalahan

| Kesalahan | Di fungsi mana dideteksi | Tanggapan program |
| FileNotFoundError | Pembacaan file | except FileNotFoundError untuk menampilkan pesan bahwa file tidak ditemukan dan meminta pengguna memeriksa kembali lokasi file |
| ZeroDivisionError | Hitung_mrp_item | except ZeroDivisionError untuk menampilkan pesan bahwa pembagian dengan nol tidak diperbolehkan |
| TypeError | pembersihan data dan perhitungan MRP | except TypeError untuk menampilkan pesan bahwa terdapat ketidaksesuaian tipe data yang perlu diperiksa |
| ValueError | validasi input pada menu utama | except ValueError untuk menampilkan pesan bahwa input harus sesuai dengan format yang diminta dan meminta pengguna mengulanginya |
| KeyboardInterrupt | menu utama ui.py | except KeyboardInterrupt untuk menampilkan pesan bahwa program dihentikan oleh pengguna |
| PermissionError | pembacaan file | except PermissionError untuk menampilkan pesan bahwa file tidak dapat diakses karena masalah izin |
| IndexError | urutkan dan cari_biner | except IndexError untuk menampilkan pesan bahwa posisi data yang diakses tidak tersedia |