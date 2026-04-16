from user import User
from data import books, borrowers, borrow_records, find_book_by_isbn, find_borrower_by_id

class Manager(User):
    def __init__(self, user_id, name, phone):
        super().__init__(user_id, name, phone)
    
    def add_book(self, isbn, title, author, total_copies):
        existing = find_book_by_isbn(isbn)
        if existing:
            return False
        new_book = {
            "isbn": isbn,
            "title": title,
            "author": author,
            "available_copies": total_copies,
            "total_copies": total_copies
        }
        books.append(new_book)
        return True
    
    def delete_book(self, isbn):
        for i, book in enumerate(books):
            if book["isbn"] == isbn:
                books.pop(i)
                return True
        return False
    
    def update_book(self, isbn, title=None, author=None, total_copies=None):
        book = find_book_by_isbn(isbn)
        if not book:
            return False
        if title:
            book["title"] = title
        if author:
            book["author"] = author
        if total_copies:
            difference = total_copies - book["total_copies"]
            book["total_copies"] = total_copies
            book["available_copies"] += difference
            if book["available_copies"] < 0:
                book["available_copies"] = 0
        return True
    
    def add_borrower(self, borrower_id, name, phone):
        existing = find_borrower_by_id(borrower_id)
        if existing:
            return False
        new_borrower = {
            "borrower_id": borrower_id,
            "name": name,
            "phone": phone
        }
        borrowers.append(new_borrower)
        return True
    
    def delete_borrower(self, borrower_id):
        for i, borrower in enumerate(borrowers):
            if borrower["borrower_id"] == borrower_id:
                borrowers.pop(i)
                return True
        return False
    
    def modify_borrower(self, borrower_id, name=None, phone=None):
        borrower = find_borrower_by_id(borrower_id)
        if not borrower:
            return False
        if name:
            borrower["name"] = name
        if phone:
            borrower["phone"] = phone
        return True
    
    def view_all_books(self):
        return books
    
    def view_all_borrowers(self):
        return borrowers
    
    def view_all_records(self):
        return borrow_records
    
    def menu(self):
        while True:
            print("\n" + "=" * 50)
            print(f"Welcome Manager: {self.name}")
            print("=" * 50)
            print("1. View All Books")
            print("2. Add Book")
            print("3. Update Book")
            print("4. Delete Book")
            print("5. View All Borrowers")
            print("6. Add Borrower")
            print("7. Modify Borrower")
            print("8. Delete Borrower")
            print("9. View All Borrowing Records")
            print("10. Logout")
            print("=" * 50)
            
            choice = input("Enter your choice (1-10): ")
            
            if choice == "1":
                print("\nAll Books:")
                for book in books:
                    status = "Available" if book["available_copies"] > 0 else "Not Available"
                    print(f"  {book['title']} by {book['author']} (ISBN: {book['isbn']}) - {status} ({book['available_copies']}/{book['total_copies']} copies)")
            
            elif choice == "2":
                isbn = input("Enter ISBN: ")
                title = input("Enter Title: ")
                author = input("Enter Author: ")
                total_copies = int(input("Enter Total Copies: "))
                if self.add_book(isbn, title, author, total_copies):
                    print("Book added successfully!")
                else:
                    print("Book already exists.")
            
            elif choice == "3":
                isbn = input("Enter ISBN of book to update: ")
                title = input("Enter new Title (press Enter to skip): ")
                author = input("Enter new Author (press Enter to skip): ")
                total_copies_input = input("Enter new Total Copies (press Enter to skip): ")
                total_copies = int(total_copies_input) if total_copies_input else None
                if self.update_book(isbn, title if title else None, author if author else None, total_copies):
                    print("Book updated successfully!")
                else:
                    print("Book not found.")
            
            elif choice == "4":
                isbn = input("Enter ISBN of book to delete: ")
                if self.delete_book(isbn):
                    print("Book deleted successfully!")
                else:
                    print("Book not found.")
            
            elif choice == "5":
                print("\nAll Borrowers:")
                for borrower in borrowers:
                    print(f"  ID: {borrower['borrower_id']} | Name: {borrower['name']} | Phone: {borrower['phone']}")
            
            elif choice == "6":
                borrower_id = input("Enter Borrower ID: ")
                name = input("Enter Name: ")
                phone = input("Enter Phone: ")
                if self.add_borrower(borrower_id, name, phone):
                    print("Borrower added successfully!")
                else:
                    print("Borrower already exists.")
            
            elif choice == "7":
                borrower_id = input("Enter Borrower ID to modify: ")
                name = input("Enter new Name (press Enter to skip): ")
                phone = input("Enter new Phone (press Enter to skip): ")
                if self.modify_borrower(borrower_id, name if name else None, phone if phone else None):
                    print("Borrower modified successfully!")
                else:
                    print("Borrower not found.")
            
            elif choice == "8":
                borrower_id = input("Enter Borrower ID to delete: ")
                if self.delete_borrower(borrower_id):
                    print("Borrower deleted successfully!")
                else:
                    print("Borrower not found.")
            
            elif choice == "9":
                print("\nAll Borrowing Records:")
                for record in borrow_records:
                    print(f"  Record ID: {record['record_id']} | Borrower: {record['borrower_id']} | ISBN: {record['isbn']} | Status: {record['status']}")
            
            elif choice == "10":
                print("Logging out...")
                break
            
            else:
                print("Invalid choice. Please try again.")

