# Hola Coder, en esta actividad vas a crear un programa en Python que simule cómo preparar distintas recetas de cocina.
# Para la presente actividad podrás utilizar todo lo aprendido en el módulo de Python. Principalmente deberás utilizar funciones, condicionales y estructuras como listas, tuplas o diccionarios para organizar los ingredientes y pasos de las recetas.
# 🎯 ¿Qué debes hacer?­
# Imagina que estás creando un asistente de cocina virtual. Este asistente debe saber preparar las siguientes tres recetas:
#     1. Ensalada César con pollo
#     2. Wrap de pollo con salsa César
#     3. Sándwich clásico de pollo


lista_preparacion_pollo = ["tiras", "normal"]


def preparar_pollo_a_la_plancha():
    while True:
        try:
            print("\nPreparando pollo...")
            print("Como deseas el pollo\n1.tiras\n2.normal\n")
            como_deseas_pollo = input(
                "como deseas tu pollo elige escribe la presentacion a elegir (tiras o normal): ").lower()
            if como_deseas_pollo in lista_preparacion_pollo:
                if como_deseas_pollo == "tiras":
                    return "pollo en tira"
                elif como_deseas_pollo == "normal":
                    return "pollo a la plancha"
            else:
                print("ERROR! ingresa un valor pedido")
        except:
            print("ERROR! ingresa un valor valido")


lista_pimienta = ["si", "no"]


def preparar_salsa_cesar():
    while True:
        print("\npreparando salsa...")
        deseas_pimienta = input(
            "deseas pimienta en tu salsa (si o no):").lower()
        if deseas_pimienta in lista_pimienta:
            if deseas_pimienta == "si":
                return "agregada"
            elif deseas_pimienta == "no":
                return "no se le agregara"
        else:
            print("ERROR! no espesificaste")


def preparar_ensalada_cesar():
    agregar_pollo = preparar_pollo_a_la_plancha()
    agregar_salsa_cesar = preparar_salsa_cesar()
    ensalada = {
        "lechuga": "30g de lechuga",
        "tomate": "tomate cherry",
        "preparacion pollo": agregar_pollo,
        "salsa_cesar": {"pimienta": agregar_salsa_cesar}
    }
    return ensalada


def preparar_wrap_cesar():
    agregar_pollo = preparar_pollo_a_la_plancha()
    agregar_salsa_cesar = preparar_salsa_cesar()
    wrap_cesar = {
        "tortilla": "tortilla grande",
        "lechuga": "lechuga romana",
        "pollo": agregar_pollo,
        "salsa_cesar": {"pimienta": agregar_salsa_cesar},
        "queso": "queso parmesano"
    }

    return wrap_cesar


def preparar_sandwich_pollo():
    agregar_pollo = preparar_pollo_a_la_plancha()
    sandwich = {
        "pan": "dos torrejas de panes",
        "tomate": "dos torrejas de tomate",
        "lechuga": "20g de lechuga",
        "pollo": agregar_pollo
    }
    return sandwich


while True:
    print("~"*60)
    print(("Bienvenido a el restuarante (AGVfood)\n").center(50))
    print("~"*60)
    print("¨"*60)
    print("🍽️ MENU.".center(50))
    print("¨"*60)
    print("\n1.Ensalada César con pollo\n2.Wrap de pollo con salsa César\n3.Sándwich clásico de pollo\n")

    try:
        receta_Decidir = int(
            input("que receta deseas comer ingresa una opcion numerica: "))
        if receta_Decidir == 1:
            receta_ensalada = preparar_ensalada_cesar()
            print("\nrealizando tu ensalada cesar...\n")
            for receta, valor in receta_ensalada.items():
                if receta == "salsa_cesar":
                    for receta_salsa, valor_salsa in valor.items():
                        print(f"{receta}: {receta_salsa}: {valor_salsa} ")
                else:
                    print(f"{receta}: {valor} ")
            break
        elif receta_Decidir == 2:
            receta_wrap = preparar_wrap_cesar()
            print("\nrealizando tu sandwich...\n")
            for receta, valor in receta_wrap.items():
                if receta == "salsa_cesar":
                    for receta_salsa, valor_salsa in valor.items():
                        print(f"{receta}: {receta_salsa}: {valor_salsa} ")
                else:
                    print(f"{receta}: {valor} ")
            break
        elif receta_Decidir == 3:
            receta_sandwich = preparar_sandwich_pollo()
            print("\nrealizando tu wrap...\n")
            for receta, valor in receta_sandwich.items():
                print(f"{receta}: {valor} ")
            break
        else:
            print("ingresa un valor valido\n")
    except ValueError:
        print("EEROR! ingresa un valor numerico\n")
