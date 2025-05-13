while True:
    try:
        notas_a_ingresar = int(input("cuantas notas deseas ingresar: "))
        if notas_a_ingresar > 0:
            break
        else:
            print("ERROR! ingresa un numero positivo\n")
    except:
        print("ERROR! ingresa nueva mente tu opcion\n") 

if notas_a_ingresar > 0:
    for i in range(notas_a_ingresar):
        while True:
            try:
                valor_de_nota = float(input(f"ingresa tu {i+1} nota: "))
                if  valor_de_nota >= 0  and valor_de_nota <=100:
                    break
                else:
                    print("ERROR!ingresa tu nota nueva mente")
            except:
                print("ERROR! ingresa un valor numerico valido")
promedio_de_nota = valor_de_nota + valor_de_nota / valor_de_nota

print(f"tu promdio de notas es de: {promedio_de_nota:.2f}")
