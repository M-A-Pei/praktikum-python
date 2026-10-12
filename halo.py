try:
    tahunLahir = int(input("Masukkan Tahun lahir Anda: "))
    umur = 2026 - tahunLahir
    print(f"Halo, umur Anda di tahun 2026 adalah {umur} tahun.")
except ValueError:
    print("Peringatan: Input tidak valid! Harap masukkan angka saja.")