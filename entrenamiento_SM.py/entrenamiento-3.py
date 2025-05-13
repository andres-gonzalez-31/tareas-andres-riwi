guardar_producto ={}


def pedir_valor(mensaje):
    try:
        valor_producto = int(input(mensaje))
        if valor_producto < 0:
            print("ERROR! ingresa un valor mayor a 0\n")
        else:
            return mensaje
    except:
        print("ERROR! ingresa un valor numerico\n")
def pedir_cantidad(mensaje):
    try:
        valor_producto = int(input(mensaje))
        if valor_producto < 0:
            print("ERROR! ingresa un valor mayor a 0\n")
        else:
            return mensaje
    except:
        print("ERROR! ingresa un valor numerico\n")

def añadir_producto():
    nombre_producto = input("ingresa nombre del producto: ")
    valor_producto = pedir_valor("ingresa el valor del producto: ")
    cantidad_producto = pedir_cantidad("ingresa las cantidades del producto a llevar: ")
guardar_producto(nombre_producto)
guardar_producto(valor_producto)
guardar_producto(cantidad_producto)