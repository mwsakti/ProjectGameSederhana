import random

print("Permainan Batu Gunting Kertas")
print("Pilihan:")
print("1. Batu")
print("2. Gunting")
print("3. Kertas")

def permainan():
    saya = int(input("Masukkan pilihanmu: "))
    komputer = random.choice(["batu", "gunting", "kertas"])
    
    if saya == 1:
        print("Saya: Batu")
        print("Komputer:", komputer)
        if komputer == "batu":
            print("\tSeri")
        elif komputer == "gunting":
            print("\tKamu Menang")
        elif komputer == "kertas":
            print("\tKamu Kalah")
    
    elif saya == 2:
        print("Saya: Gunting")
        print("Komputer:", komputer)
        if komputer == "batu":
            print("\tKamu Kalah")
        elif komputer == "gunting":
            print("\tSeri")
        elif komputer == "kertas":
            print("\tKamu Menang")
    
    elif saya == 3:
        print("Saya: Kertas")
        print("Komputer:", komputer)
        if komputer == "batu":
            print("\tKamu Menang")
        elif komputer == "gunting":
            print("\tKamu Kalah")
        elif komputer == "kertas":
            print("\tSeri")
    
    else:
        print("Pilihanmu salah")

permainan()
