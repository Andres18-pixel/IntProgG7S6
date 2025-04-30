numero = int(input("Ingrese un número positivo: "))
if numero < 0:
    print("El numero debe ser positivo. ")
else:
    for contador in range(0, numero + 1):
        if contador % 2 == 0:
            print(contador)