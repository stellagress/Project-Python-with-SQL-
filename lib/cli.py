from db.models import Salon
from simple_term_menu import TerminalMenu
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from prettycli import red



engine = create_engine('sqlite:///db/data.db')
Session = sessionmaker(bind=engine)
session = Session()




def start():
    print("     _       _           _            _")
    print("    / \\   __| |_ __ ___ (_)_ __      / \\   ___ ___ ___  ___ ___")
    print("   / _ \\ / _` | '_ ` _ \\| | '_ \\    / _ \\ / __/ __/ _ \\/ __/ __|")
    print("  / ___ \\ (_| | | | | | | | | | |  / ___ \\ (_| (_|  __/\\__ \\__ \\")
    print(" /_/   \\_\\__,_|_| |_| |_|_|_| |_| /_/   \\_\\___\\___\\___||___/___/")

    # for _ in range(3):
    print("\n")

    print("-----------------MARILYN'S NAIL SALON - RESTRICTED PORTAL-----------------")

    print("\n")

    options = ["1. View Current Inventory", "2. Update Inventory", "3. SOS order", "4. Exit"]
    terminal_menu = TerminalMenu(options)
    menu_entry = terminal_menu.show()
    
    if menu_entry == 0:
        view_current_inventory()
    elif menu_entry == 1:
        update_inventory()
        


def view_current_inventory():
    inventory_items = session.query(Salon).all()
    for item in inventory_items:
        print(f"Product: {item.product}, Price: {item.price}, Quantity: {item.quantity}")




def update_inventory():
    update_inventory_input_1 = input("Would you like to add or delete inventory? ")
    
    if update_inventory_input_1 == "add":
        products = session.query(Salon.product).all()
        print("\n".join([f"{product[0]}" for product in products]))
        product_name = input("Enter the name of the product to add: ")
        salon = session.query(Salon).filter_by(product=product_name).first()

        if salon:
            print(f"Current quantity for {product_name}: {salon.quantity}")
            update_inventory_input_add_3 = int(input(f"How many units would you like to add? "))
            salon.quantity += update_inventory_input_add_3
            session.commit()
            print(f"Updated quantity for {product_name}: {salon.quantity}")
        else:
            print(f"Product {product_name} not found in inventory.")

    elif update_inventory_input_1 == "delete":
        product_name = input("Enter the name of the product to delete: ")
        salon = session.query(Salon).filter_by(product=product_name).first()

        if salon:
            print(f"Current quantity for {product_name}: {salon.quantity}")
            update_inventory_input_add_3 = int(input(f"How many units would you like to delete? "))
            salon.quantity -= update_inventory_input_add_3
            session.commit()
            print(f"Updated quantity for {product_name}: {salon.quantity}")
        else:
            print(f"Product {product_name} not found in inventory.")
    else:
        print(red("invalid selection"))


# def update_inventory():
#     update_inventory_input_1 = input("Would you like to add or delete inventory? ")
#     if update_inventory_input_1 == "add":
#         print(session.query(Salon.product).all())
#         update_inventory_input_add_1 = input("Is the inventory to add in the list above? y/n ")
#         if update_inventory_input_add_1 == "y":
#             update_inventory_input_add_2 = input("Which item would you like to add inventory? ")
#             update_inventory_input_add_3 = input(f"You selected: {update_inventory_input_add_2}. How many units would you like to add? ")
#             print("bla")


        


#     elif update_inventory_input_1 == "delete":
#         print(Salon.quantity[update_inventory_input_add_2])







if __name__ == "__main__":
    
    start()
  












# from simple_term_menu import TerminalMenu
# from models import Salon, Nail_Polish
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker


# def start():
#     print("     _       _           _            _")
#     print("    / \\   __| |_ __ ___ (_)_ __      / \\   ___ ___ ___  ___ ___")
#     print("   / _ \\ / _` | '_ ` _ \\| | '_ \\    / _ \\ / __/ __/ _ \\/ __/ __|")
#     print("  / ___ \\ (_| | | | | | | | | | |  / ___ \\ (_| (_|  __/\\__ \\__ \\")
#     print(" /_/   \\_\\__,_|_| |_| |_|_|_| |_| /_/   \\_\\___\\___\\___||___/___/")

#     # for _ in range(3):
#     print("\n")

#     print("-----------------MARILYN'S NAIL SALON RESTRICTED PORTAL-----------------")

#     print("\n")

#     options = ["1. View Current Inventory", "2. Update Inventory", "3. SOS order", "4. Exit"]
#     terminal_menu = TerminalMenu(options)
#     menu_entry = terminal_menu.show()
#     # print(f"Confirm selection: {options[menu_entry]}")

# start()





    # print("1. View Current Inventory")
    # print("2. Update Inventory")
    # print("3. SOS order")
    # print("4. Exit")
    # user_input = input("Please make a selection (1-3): ")

 




