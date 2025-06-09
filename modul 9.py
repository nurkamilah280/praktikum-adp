import os
import time
from termcolor import colored

pengguna = input('masukkan nama : ')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_logo():
    logo = r"""
 __  __ _____ _      _       
|  \/  |_   _| |    | |      
| \  / | | | | |    | |      
| |\/| | | | | |    | |      
| |  | |_| |_| |____| |____  
|_|  |_|_____|______|______| 
    """
    print(colored(logo, 'cyan'))

def loading_screen():
    clear_screen()
    tampilkan_logo()
    print(colored("Memulai aplikasi MILL...", "yellow"))

    for i in range(1, 6):
        titik = "." * i
        print(colored(f"Loading{titik}", "green"), end="\r")
        time.sleep(0.5)

    print(colored("Loading selesai!", "green"))
    time.sleep(1)

    # Tambahkan hitungan mundur sebelum masuk ke app
    print(colored("\nMenjalankan aplikasi dalam:", "magenta"))
    for i in range(3, 0, -1):
        print(colored(f"{i}...", "red"))
        time.sleep(1)

def main_app():
    clear_screen()
    print(colored(" Selamat datang di Aplikasi MILL! ", "blue"))
    print(colored(f"Aplikasi siap digunakan. Semangat terus, {pengguna}! 💪", "yellow"))

if __name__ == "__main__":
    loading_screen()
    main_app()
