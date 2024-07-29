from service.product_service import ProductService
from entity.product import Product
from prompt.make_table import make_table

def print_table(products:list[Product]):
    table = [[r.get_id(), r.get_name(), "$" + str(r.get_price()), r.get_description()] for r in products]
    pd_table = make_table(table, ["ID", "Name", "Price", "Description"])
    print("\n********\nProducts\n********")
    print(pd_table)

def edit_entry(product_service:ProductService, product_id:int):
    while True:
        products = product_service.get_all_products()
        print("\n*****\nEntry\n*****")
        entry = [[r.get_id(), r.get_name(), "$" + str(r.get_price()), r.get_description()] for r in products if r.get_id() == product_id]
        print(make_table(entry, ["ID", "Name", "Price", "Description"]))
        print("\n[1] Edit Name\n[2] Edit Price\n[3] Edit Description\n[4] Exit")
        option = input("Enter a number: ")
        if option == "1":
            new_name = input("Enter new name: ")
            product_service.change_product_name_by_id(product_id, new_name)
        elif option == "2":
            new_price = float(input("Enter a float: "))
            product_service.change_product_price_by_id(product_id, new_price)
        elif option == "3":
            new_description = input("Enter a description: ")
            product_service.change_product_description_by_id(product_id, new_description)
        elif option == "4":
            break
        else:
            print("Invalid input. Try again.")

def add_entry(product_service:ProductService):
    print("\n************\nAdding Entry\n************")
    name = input("Enter product name: ")
    price = 0.0
    while True:   
        try:
            price = float(input("Enter product price: "))
            break
        except:
            print("Invalid input. Please enter a float.")
    description = input("Enter a product description: ")
    product = product_service.add_product(name, price, description)
    entry = [[product.get_id(), product.get_name(), product.get_price(), product.get_description()]]
    print("\n***********\nEntry Added\n***********")
    print(make_table(entry, ["ID", "Name", "Price", "Description"]))
    input("\nPress Enter to continue")

def edit_products_prompt(product_service:ProductService):
    while True:
        products = product_service.get_all_products()
        print_table(products)
        print("\n[1] Edit Entry\n[2] Add Entry\n[3] Remove Entry\n[4] Exit")
        option = input("Enter a number: ")
        if option == "1":
            ids = [product.get_id() for product in products]
            while True:
                id = input("Enter ID number of product you would like to edit or enter 'x' to exit: ")
                if id == 'x':
                    break
                elif not str(id).isdigit():
                    print("That's not a number try again.")
                elif int(id) not in ids:
                    print("That's not a product ID. Try again.")
                else:
                    edit_entry(product_service, int(id))
                    break
        elif option == "2":
            add_entry(product_service)
        elif option == "3":
            ids = [product.get_id() for product in products]
            while True:
                id = input("Enter ID number of product you would like to remove or enter 'x' to exit: ")
                if id == 'x':
                    break
                elif not str(id).isdigit():
                    print("That's not a number try again.")
                elif int(id) not in ids:
                    print("That's not a product ID. Try again.")
                else:
                    product = next((p for p in products if p.get_id() == int(id)))
                    entry = [[product.get_id(), product.get_name(), product.get_price(), product.get_description()]]
                    product_service.delete_product_by_id(int(id))
                    print("*************\nEntry Removed\n*************")
                    print(make_table(entry, ["ID", "Name", "Price", "Description"]))
                    input("Press Enter to continue")
                    break          
        elif option == "4":
            break
        else:
            print("Invalid input. Try again")