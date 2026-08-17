import csv

inventory = []

def add_product():
    print("\===== ADD PRODUCT =====")

    name = input("Product name: ")

    try:
        price = float(input("Product price: ₱ "))
        quantity = int(input("Product quantity: "))
    except ValueError:
        print("Invalid price or quantity.")
        return

    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    inventory.append(product)

    print("Product added successfully!")

def view_products():
    print("\===== INVENTORY =====")

    if not inventory:
        print("Inventory is empty.")
        return

    for number, product in enumerate(inventory, start=1):
        print(f"{number}. {product['name']} | ₱ {product['price']:.2f} | Quantity: {product['quantity']}")

def search_product():
    print("\===== SEARCH PRODUCT =====")

    search_name = input("Enter product name: ").lower()

    found = False

    for product in inventory:
        if search_name in product['name'].lower():
            print(f"{product['name']} | ₱ {product['price']:.2f} | Quantity: {product['quantity']}")
            found = True

    if not found:
        print("Product not found.")    

def update_stock():
    print("\===== UPDATE STOCK =====")

    name = input("Enter product name: ").lower()

    for product in inventory:
        if product["name"].lower() == name:
            try:
                new_quantity = int(input("Enter new quantity: "))
            except ValueError:
                print("Invalid quantity.")
                return

            product["quantity"] = new_quantity 
            print("Stock updated successfully!")
            return
    
    print("Product not found.")  

def delete_product():
    print("\===== DELETE PRODUCT =====")

    name = input("Enter product name: ").lower()

    for product in inventory:
        if product["name"].lower() == name:
            inventory.remove(product)
            print("Product deleted successfully!")
            return

    print("Product not found.")

def save_inventory():
    with open("inventory.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Product", "Price", "Quantity"])
        for product in inventory:
            writer.writerow([product["name"], product["price"], product["quantity"]])
        print("Inventory saved to inventory.csv.")

def show_inventory_value():
    total_value = sum(product["price"] * product["quantity"] for product in inventory)
    print(f"Total Inventory Value: ₱ {total_value:.2f}")

def main():
    while True:
        print("=============================")
        print("INVENTORY MANAGEMENT SYSTEM")
        print("=============================")

        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Stock")
        print("5. Delete Product")
        print("6. Show Inventory Value")
        print("7. Save Inventory")
        print("8. Exit")

        choice = input("Choose an option: ")
        
        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "3":
            search_product()
        elif choice == "4":
            update_stock()
        elif choice == "5":
            delete_product()
        elif choice == "6":
            show_inventory_value()
        elif choice == "7":
            save_inventory()
        elif choice == "8":
            print("Thank you for using Inventory Management System!")
            break
        else:
            print("Invalid choice. Please choose 1-8")

if __name__ == "__main__":
    main()  
               