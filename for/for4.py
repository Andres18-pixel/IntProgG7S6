numero = int(input("Ingrese un numero positivo: "))
if numero < 0:
    print("El numero debe ser positivo. ")
else:
    while numero >= 0:
        print(numero)
        numero -= 1
