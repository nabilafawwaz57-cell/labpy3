from random import random

n = int(input("Masukkan nilai N: "))

i = 0

while i < n:
    a = random()
    if a < 0.5:
        i += 1
        print(f"data ke: {i} => {a}")
print("Selesai")
