from user import User
from data import find_book_by_isbn, get_borrow_records, add_borrow_record, update_borrow_record, books
from bookfunction import Book
from datetime import datetime, timedelta

class Borrower(User):
    def __init__(self, user_id, name, phone):
        super().__init__(user_id, name, phone)
        self.borrowed_books = []
        self.load_borrowed_books()
    
    def load_borrowed_books(self):
        records = get_borrow_records(self.user_id)
        for record in records:
            if record["status"] == "borrowed":
                self.borrowed_books.append(record["isbn"])
    
    def borrow_available(self, isbn):
        book_data = find_book_by_isbn(isbn)
        if book_data:
            book = Book(book_data["isbn"], book_data["title"], book_data["author"], 
                       book_data["available_copies"], book_data["total_copies"])
            if book.borrow():
                book_data["available_copies"] = book.available_copies
                record_id = f"R{len(get_borrow_records(self.user_id)) + 100}"
                borrow_date = datetime.now().strftime("%Y-%m-%d")
                due_date = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")
                new_record = {
                    "record_id": record_id,
                    "borrower_id": self.user_id,
                    "isbn": isbn,
                    "borrow_date": borrow_date,
                    "due_date": due_date,
                    "status": "borrowed"
                }
                add_borrow_record(new_record)
                self.borrowed_books.append(isbn)
                return True
        return False
    
    def return_available(self, isbn):
        if isbn not in self.borrowed_books:
            return False
        book_data = find_book_by_isbn(isbn)
        if book_data:
            book = Book(book_data["isbn"], book_data["title"], book_data["author"],
                       book_data["available_copies"], book_data["total_copies"])
            if book.return_book():
                book_data["available_copies"] = book.available_copies
                self.borrowed_books.remove(isbn)
                records = get_borrow_records(self.user_id)
                for record in records:
                    if record["isbn"] == isbn and record["status"] == "borrowed":
                        update_borrow_record(record["record_id"], "returned")
                        return True
        return False
    
    def renew_available(self, isbn):
        if isbn not in self.borrowed_books:
            return False
        records = get_borrow_records(self.user_id)
        for record in records:
            if record["isbn"] == isbn and record["status"] == "borrowed":
                new_due_date = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")
                record["due_date"] = new_due_date
                return True
        return False
    
    def search_books(self, keyword):
        results = []
        for book in books:
            if keyword.lower() in book["title"].lower() or keyword.lower() in book["author"].lower():
                results.append(book)
        return results
    
    def show_my_record(self):
        return get_borrow_records(self.user_id)
    
    def get_borrowed_books(self):
        return self.borrowed_books
    
    def menu(self):
        while True:
            print("\n" + "=" * 50)
            print(f"Welcome Borrower: {self.name}")
            print("=" * 50)
            print("1. Search Books")
            print("2. Borrow Book")
            print("3. Return Book")
            print("4. Renew Book")
            print("5. Show My Borrowing Records")
            print("6. Logout")
            print("=" * 50)
            
            choice = input("Enter your choice (1-6): ")
            
            if choice == "1":
                keyword = input("Enter title or author to search: ")
                results = self.search_books(keyword)
                if results:
                    print("\nSearch Results:")
                    for book in results:
                        status = "Available" if book["available_copies"] > 0 else "Not Available"
                        print(f"  {book['title']} by {book['author']} (ISBN: {book['isbn']}) - {status} ({book['available_copies']}/{book['total_copies']} copies)")
                else:
                    print("No books found.")
            
            elif choice == "2":
                isbn = input("Enter ISBN of book to borrow: ")
                if self.borrow_available(isbn):
                    print("Book borrowed successfully!")
                else:
                    print("Failed to borrow book. It may be unavailable or you already borrowed it.")
            
            elif choice == "3":
                isbn = input("Enter ISBN of book to return: ")
                if self.return_available(isbn):
                    print("Book returned successfully!")
                else:
                    print("Failed to return book. You may not have borrowed it.")
            
            elif choice == "4":
                isbn = input("Enter ISBN of book to renew: ")
                if self.renew_available(isbn):
                    print("Book renewed successfully! Due date extended by 14 days.")
                else:
                    print("Failed to renew book. You may not have borrowed it.")
            
            elif choice == "5":
                records = self.show_my_record()
                if records:
                    print("\nYour Borrowing Records:")
                    for record in records:
                        print(f"  ISBN: {record['isbn']} | Borrowed: {record['borrow_date']} | Due: {record['due_date']} | Status: {record['status']}")
                else:
                    print("No borrowing records found.")
            
            elif choice == "6":
                print("Logging out...")
                break
            
            else:
                print("Invalid choice. Please try again.")

