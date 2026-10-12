# Praktikum Python - Tugas Mandiri 🐍

haloooo, Repository ini berisi skrip Python untuk tugas mandiri. File utama dalam proyek ini adalah "halo.py".

## 📂 Tentang Program
Program "halo.py" adalah antarmuka command-line (CLI) interaktif yang memiliki fitur-fitur berikut:
* Menampilkan teks menggunakan ASCII Art bertuliskan "PEI" dengan jenis *font* "block".
* Mengubah warna latar belakang terminal menjadi putih pada awal eksekusi.
* Meminta pengguna untuk memasukkan tahun lahir mereka dengan teks berwarna Cyan.
* Menghitung estimasi umur pengguna pada tahun 2026 dan menampilkannya dengan teks berwarna Hijau.
* Memiliki sistem penanganan *error* (`try...except ValueError`) yang akan menampilkan pesan peringatan berwarna Merah jika pengguna memasukkan huruf alih-alih angka.
* Mengembalikan pengaturan warna terminal ke pengaturan standar (`Style.RESET_ALL`) di akhir program agar terminal Anda tidak tetap berwarna putih.

## 🛠️ Prasyarat (Dependencies)
Berdasarkan kode di dalam "halo.py", program ini membutuhkan dua library eksternal untuk bisa berjalan. Anda perlu menginstalnya terlebih dahulu:

* **colorama**: Untuk mengatur pewarnaan *foreground*, *background*, dan *style* pada terminal.
* **art**: Untuk menghasilkan *output* ASCII art menggunakan fungsi `tprint`.

Anda dapat menginstal kedua library tersebut dengan menjalankan perintah berikut di terminal/Command Prompt:

```bash
pip install -r requirements.txt

```

TERIMAKASIHHHHH!