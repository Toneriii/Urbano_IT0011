class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def display(self):
        print(f"ID: {self.item_id}, Name: {self.name}, Description: {self.description}, Price: {self.price}")

items = []

def add_item():
    try:
        item_id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        description = input("Enter Description: ")
        price = float(input("Enter Price: "))
        items.append(Item(item_id, name, description, price))
        print("Item added successfully!")
    except ValueError:
        print("Invalid input! Please enter the correct values.")

def view_items():
    if not items:
        print("No items available.")
    else:
        for item in items:
            item.display()

def update_item():
    try:
        item_id = int(input("Enter the ID of the item to update: "))
        for item in items:
            if item.item_id == item_id:
                item.name = input("Enter new name: ")
                item.description = input("Enter new description: ")
                item.price = float(input("Enter new price: "))
                print("Item updated successfully!")
                return
        print("Item not found.")
    except ValueError:
        print("Invalid input!")

def delete_item():
    try:
        item_id = int(input("Enter the ID of the item to delete: "))
        for item in items:
            if item.item_id == item_id:
                items.remove(item)
                print("Item deleted successfully!")
                return
        print("Item not found.")
    except ValueError:
        print("Invalid input!")

while True:
    print("\nItem Management System")
    print("[1] Add Item")
    print("[2] View Items")
    print("[3] Update Item")
    print("[4] Delete Item")
    print("[5] Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_item()
    elif choice == "2":
        view_items()
    elif choice == "3":
        update_item()
    elif choice == "4":
        delete_item()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please enter a valid option.")
