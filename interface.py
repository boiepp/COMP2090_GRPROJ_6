from data import find_borrower_by_id
from borrower import Borrower
from manager import Manager

def main_menu():
    while True:
        print("\n" + "=" * 50)
        print("LIBRARY MANAGEMENT SYSTEM")
        print("=" * 50)
        print("1. Borrower Login")
        print("2. Manager Login")
        print("3. Exit")
        print("=" * 50)
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            borrower_login()
        elif choice == "2":
            manager_login()
        elif choice == "3":
            print("Thank you for using Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def borrower_login():
    borrower_id = input("Enter your Borrower ID (e.g., B001): ")
    borrower_data = find_borrower_by_id(borrower_id)
    
    if borrower_data:
        borrower = Borrower(borrower_data["borrower_id"], borrower_data["name"], borrower_data["phone"])
        borrower.menu()
    else:
        print("Invalid Borrower ID. Please try again.")

def manager_login():
    manager_id = input("Enter Manager ID (default: M001): ")
    manager_password = input("Enter Password (default: admin123): ")
    
    if manager_id == "M001" and manager_password == "admin123":
        manager = Manager("M001", "Head Librarian", "69998888")
        manager.menu()
    else:
        print("Invalid Manager ID or Password.")

def borrower_menu(borrower):
    borrower.menu()

def manager_menu(manager):
    manager.menu()

def manager_menu(manager):
    manager.menu()
