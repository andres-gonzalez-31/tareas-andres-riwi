# Solicita al usuario que ingrese números. Sigue sumándolos hasta que la suma sea mayor a 100. Usa un while.
suma = 0
while suma < 100:
    numero = int(input())
    suma += numero
print(f'la suma es {suma}')


# while True:
#     ingresa_un_numero = int(input("ingresa un valor: "))
#     ingresa_un_numero+= ingresa_un_numero
#     print(f"tu valor va por: {ingresa_un_numero}")
#     if ingresa_un_numero > 100:
#         break
#     else:
#         ingresa_un_numero = int(input("ingresa un valor: "))

