

# def calculadora (operacion, numero_uno,numero_dos):
    
#     resultdo_operacion= 0
#     if operacion == "suma":
#       resultdo_operacion =  numero_uno + numero_dos
#     elif operacion == "resta":
#       resultdo_operacion =  numero_uno - numero_dos
#     elif operacion == "multiplicar":
#       resultdo_operacion =  numero_uno * numero_dos
#     elif operacion == "dividir":
#         if numero_dos != 0:
#           resultdo_operacion =  numero_uno / numero_dos
#     else:
#         print("operacion invalida")
#     return resultdo_operacion

# numero_uno = int(input("ingresa primer numero : "))
# numero_dos = int(input("ingresa segundo numero:"))
# operacion = input("ingresa la operacion que deseas realizar: ").lower()

# resultado = calculadora(operacion,numero_uno,numero_dos)
# print(f"tu resultado es : {resultado}")


def calculadora (operacion, numero_uno,numero_dos):
    
    resultado_operacion= 0
    operacion_ejecutada = True
    mensaje = "operacion exitosa"
    if operacion == "suma":
      resultado_operacion =  numero_uno + numero_dos
    elif operacion == "resta":
      resultado_operacion =  numero_uno - numero_dos
    elif operacion == "multiplicar":
      resultado_operacion =  numero_uno * numero_dos
    elif operacion == "dividir":
        if numero_dos != 0:
          resultado_operacion =  numero_uno / numero_dos
    else:
        operacion_ejecutada = False
        mensaje = "opcion invalida"  
    return {
        "mensaje":mensaje,
        "resultado_operacion":resultado_operacion,
        "operacion_ejecutada": operacion_ejecutada,
        "operacion": operacion
    }

numero_uno = int(input("ingresa primer numero : "))
numero_dos = int(input("ingresa segundo numero:"))
operacion = input("ingresa la operacion que deseas realizar: ").lower()

resultado = calculadora(operacion,numero_uno,numero_dos)

if resultado["operacion_ejecutada"]:
    print(f"el resultado es de: {resultado['resultado_operacion']} con operacion {resultado['operacion_ejecutada']}")
else:
    print(resultado["mensaje"])
    
print(f" ejecutó la operación {resultado['operacion']}")