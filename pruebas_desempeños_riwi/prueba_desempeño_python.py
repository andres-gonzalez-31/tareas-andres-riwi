
save_product_data = []

"""
Function used to order the initial products, which in this case are five
"""
def initial_product():
    # global save_product_data  # Declara que la variable es global
    
    if len(save_product_data) < 5:
        print(f"are missing {5-len(save_product_data)} initial products : ")
        for _ in range(5-len(save_product_data)):
            initial_product()
    else:
        print("enter additional product: ")
        enter_product()


def enter_product():
    """
    Function for entering product data, including name, price, and quantity.
    Handles input errors and ensures that the entered data is valid.
    Saves the data in a dictionary and adds it to a global list.
    """

    while True:
        nombre_base = ''
        name = input("🖊️ enter product name: ").lower()
        producto_existe = any(productos["name"] == name for productos in save_product_data)
        if producto_existe:
            print(f"💢ERROR! The name '{name}' is already registered. Please enter a different name. !\n")
            continue
        if all(' ' != letra for letra in name) and nombre_base != name:
            break
        else:
            print('💢ERROR! The name has spaces or is empty, please correct it.!\n')
            continue

# otra forma de mandar un error en los nombre cuando ingrese un espacio.
        # if not name.strip():  # Verifica si el nombre consiste solo de espacios o está vacío
        #     print('💢 ERROR! El nombre no puede consistir solo de espacios o estar vacío. ¡Inténtalo de nuevo!\n')
        #     continue
        # elif '  ' in name:  # Verifica si hay dos o más espacios consecutivos
        #     print('💢 ERROR! El nombre no debe contener múltiples espacios consecutivos. ¡Inténtalo de nuevo!\n')
        #     continue
        # elif name.startswith(' ') or name.endswith(' '): # Verifica si el nombre comienza o termina con un espacio
        #     print('💢 ERROR! El nombre no debe comenzar ni terminar con un espacio. ¡Inténtalo de nuevo!\n')
        #     continue
        # else:
        #     break
    while True:
        try:
            price = float(input("💲 enter the price of the product: "))
            if price > 0:
                break
            else:
                print("💢 mistake! enter a positive number\n")
                continue
        except ValueError:
            print("💢 mistake! Enter a numeric value\n")
            continue
        
    while True:
        try:
            amount = int(input("🛍️ enter the quantity of product to be carried: "))
            if amount > 0:
                break
            else:
                print("💢mistake! enter a positive number\n")
                continue
        except ValueError:
            print("💢 mistake! Enter a numeric value\n")
            continue
    guardar_datos_diccionario = {"name": name, "price": price, "amount": amount}
    save_product_data.append(guardar_datos_diccionario)
    print("-" * 90)
    print(f"🗳️ Your product {name} with price of {price:,.2f} nd a stock of {amount} was successfully saved.")
    print("-" * 90)

def consult_product():
    """
    Function to search for a product by name.
    Displays the product name, price, and quantity if found.
    """
    query_name = input("Enter the name of the product to consult: ").lower()
    found = False
    for Product in save_product_data:
        if Product["name"] == query_name:
            print("-" * 30)
            print(f"Product: {Product['name'].capitalize()}")
            print(f"price: ${Product['price']:.2f}")
            print(f"Stock Quantity: {Product['amount']}")
            print("-" * 30)
            found = True
            break # Important: Exit the for loop if the product is found


    if not found:
        print("💢 mistake! Product not found.\n")

def update_product_price():
    """
    Function to update the price of an existing product.
    It requests the name of the product to update, verifies that it exists,
    and then requests the new price.
    """
    product_name_update = input("Enter the product name to update the price: ").lower()
    found = False
    for Product in save_product_data:
        if Product["name"] == product_name_update:
            found = True
            while True:
                try:
                    new_price = float(input(f"Enter the new price of the product {product_name_update.capitalize()}: "))
                    if new_price > 0:
                        Product["price"] = new_price # Update the price in the dictionary
                        print(f"Product price{product_name_update.capitalize()} updated to${new_price:,.2f} successfully.")
                        break # Exit the while loop
                    else:
                        print("💢 mistake! enter a positive number\n")
                except ValueError:
                    print("💢 mistake! Enter a valid numeric value\n")
            break # Salir del bucle for
    if not found:
        print("💢 mistake! Product not found.\n")

def delete_product():
    """
    Function to remove a product from the list.
    Requests the name of the product to remove and deletes it if it exists.
    """
    product_name_delete = input("Enter the name of the product to be deleted: ").lower()
    found = False
    for product in save_product_data:
        if product["name"] == product_name_delete:
            save_product_data.remove(product) # Elimina el producto de la lista
            print(f"Product {product_name_delete.capitalize()} successfully removed.")
            found = True
            break # Salir del bucle for
    if not found:
        print("💢 mistake! Product not found.\n")

def calculate_inventory():
    """
    Function to calculate the total inventory value.
    Calculate the total value by multiplying the price by the quantity of each product and adding the results.
    """
    total_value = 0
    for product in save_product_data:
        total_value += product["price"] * product["amount"]
    print(f"The total value of the inventory is: ${total_value:,.2f}\n")

def show_full_inventory():
    """
    Function to display the complete inventory.
    Displays the name, price, and quantity of all products in the list.
    """
    if not save_product_data:
        print("The inventory is empty.\n")
        return  # Salir de la función si el inventario está vacío

    print("-" * 40)
    print("Complete Inventory")
    print("-" * 40)
    for producto in save_product_data:
        print(f"Product: {producto['name'].capitalize()}")
        print(f"Price: ${producto['price']:,.2f}")
        print(f"Stock quantity: {producto['amount']}")
        print("-" * 40)


    """
    Function that displays the main menu and allows the user to interact with the different options of the inventory system.
    """
def menu():
    print("¨"*50)
    print(("𝕖𝕟𝕥𝕖𝕣 𝕪𝕠𝕦𝕣 𝕥𝕠𝕡 𝕗𝕚𝕧𝕖 𝕡𝕣𝕠𝕕𝕦𝕔𝕥𝕤.").center(50))
    print("¨"*50)
    while len(save_product_data)< 5:
        enter_product()
    """
    loop that is used to ask the user for the initial products to enter their inventory
    """
    while True:
        try:
            print("¨"*50)
            print(("𝕎𝔼𝕃ℂ𝕆𝕄𝔼 𝕋𝕆 𝕋ℍ𝔼 𝕀ℕ𝕍𝔼ℕ𝕋𝕆ℝ𝕐 𝕄𝔼ℕ𝕌").center(50))
            print("¨"*50)
            print("select 1. 📩 add product."
                  "\nselect 2. 🖨️ consult product."
                  "\nselect 3. 🗃️ update product price"
                  "\nselect 4. 🗑️ remove product"
                  "\nselect 5. 📳 calculate total inventory value"
                  "\nselect 6. 📝 show full inventory"
                  "\nselect 7. 🚪 go out")
            select_an_option = int(input("selecciona una opcion del menu: "))
            if select_an_option < 0:
                print("💢 mistake! enter a positive number\n")
                continue
        except ValueError:
            print("💢 mistake! Enter a numeric value\n")
        while True:
            if select_an_option == 1:
                print("-"*50)
                print("𝕎𝕖𝕝𝕔𝕠𝕞𝕖, 𝕖𝕟𝕥𝕖𝕣 𝕪𝕠𝕦𝕣 𝕡𝕣𝕠𝕕𝕦𝕔𝕥 𝕚𝕟𝕗𝕠𝕣𝕞𝕒𝕥𝕚𝕠𝕟..")
                print("-"*50)
                enter_product()
                print("🎉 INFORMACION INGRESADA CORRECTAMENTE.\n")
            elif select_an_option == 2:
                print("-"*70)
                print("𝕎𝕖𝕝𝕔𝕠𝕞𝕖, 𝕕𝕠 𝕪𝕠𝕦 𝕨𝕒𝕟𝕥 𝕥𝕠 𝕔𝕠𝕟𝕤𝕦𝕝𝕥 𝕚𝕟𝕗𝕠𝕣𝕞𝕒𝕥𝕚𝕠𝕟 𝕒𝕓𝕠𝕦𝕥 𝕒 𝕡𝕣𝕠𝕕𝕦𝕔𝕥?.")
                print("-"*70)
                consult_product()
            elif select_an_option == 3:
                print("-"*70)
                print("𝕎𝕖𝕝𝕔𝕠𝕞𝕖, 𝕕𝕠 𝕪𝕠𝕦 𝕨𝕒𝕟𝕥 𝕥𝕠 𝕦𝕡𝕕𝕒𝕥𝕖 𝕥𝕙𝕖 𝕡𝕣𝕚𝕔𝕖 𝕠𝕗 𝕒 𝕡𝕣𝕠𝕕𝕦𝕔𝕥?.")
                print("-"*70)
                update_product_price()
            elif select_an_option == 4:
                print("-" * 50)
                print(" 𝕎𝕖𝕝𝕔𝕠𝕞𝕖 𝕥𝕠 𝕥𝕙𝕖 𝕕𝕖𝕝𝕖𝕥𝕖 𝕡𝕣𝕠𝕕𝕦𝕔𝕥 𝕤𝕖𝕔𝕥𝕚𝕠𝕟. ".center(50, "-"))
                print("-" * 50)
                delete_product()
            elif select_an_option == 5:
                print("-" * 50)
                print(" 𝕎𝕖𝕝𝕔𝕠𝕞𝕖 𝕥𝕠 𝕥𝕙𝕖 𝕚𝕟𝕧𝕖𝕟𝕥𝕠𝕣𝕪 𝕔𝕒𝕝𝕔𝕦𝕝𝕒𝕥𝕚𝕠𝕟 𝕤𝕖𝕔𝕥𝕚𝕠𝕟 ".center(50, "-"))
                print("-" * 50)
                calculate_inventory()
            elif select_an_option == 6:
                print("-" * 50)
                print(" 𝕎𝕖𝕝𝕔𝕠𝕞𝕖 𝕥𝕠 𝕥𝕙𝕖 𝕚𝕟𝕧𝕖𝕟𝕥𝕠𝕣𝕪 𝕕𝕚𝕤𝕡𝕝𝕒𝕪 𝕤𝕖𝕔𝕥𝕚𝕠𝕟 ".center(50, "-"))
                print("-" * 50)
                show_full_inventory()
            elif select_an_option == 7:
                print("-" * 50)
                print(" ¡𝕋𝕙𝕒𝕟𝕜 𝕪𝕠𝕦 𝕗𝕠𝕣 𝕦𝕤𝕚𝕟𝕘 𝕠𝕦𝕣 𝕚𝕟𝕧𝕖𝕟𝕥𝕠𝕣𝕪 𝕤𝕪𝕤𝕥𝕖𝕞! ".center(50, "-"))
                print("-" * 50)
                exit()
            break
      

menu()
