import colorama
from colorama import Fore, Back, Style

from art import tprint

colorama.init()
print(Back.WHITE, end="")

tprint("PEI", font="block")


try:
    tahunLahir = int(input(Fore.CYAN + "Masukkan Tahun lahir Anda: "))
    umur = 2026 - tahunLahir
    print(Fore.GREEN + f"Halo, umur Anda di tahun 2026 adalah {umur} tahun.")
except ValueError:
    print(Fore.RED + "Peringatan: Input tidak valid! Harap masukkan angka saja.")

print(Style.RESET_ALL, end="")