from random import randint

p1 = input("Kulob Hayang? ")

if p1 not in ["kulob", "hayang"]:
    print("kulob or hayang ra oy")
else:
    c2 = "kulob" if randint(0, 1) == 0 else "hayang"
    c3 = "kulob" if randint(0, 1) == 0 else "hayang"

    print(f"Computer 2 = {c2}")
    print(f"Computer 3 = {c3}")

    if p1 == c2 == c3:
        print("Tabla!")
    elif p1 != c2 and p1 != c3:
        print("Player ang daog!")
    elif c2 != p1 and c2 != c3:
        print("CPU 2 ang daog!")
    elif c3 != p1 and c3 != c2:
        print("CPU 3 ang daog!")
    else:
        print("Walay daog")
