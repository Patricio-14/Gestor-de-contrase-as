import random
a = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
b = ""
c = int(input("¿Cuantos caracteres quieres que tenga la contraseña?"))

for i in range(c):
    b += random.choice(a)
print(b)
