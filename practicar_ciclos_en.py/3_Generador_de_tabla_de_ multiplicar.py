# Pide al usuario un número y muestra su tabla de multiplicar del 1 al 10 utilizando for y range().
numero_a_multiplicar = int(input("ingres un tu numero a multiplicar: "))

if numero_a_multiplicar > 0:
    for i in range(1, 11):
        resultado = numero_a_multiplicar * i 
        print(f"multiplicar {numero_a_multiplicar} * {i} : {resultado}")
