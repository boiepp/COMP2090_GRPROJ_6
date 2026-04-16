class Book:
    def __init__(self, isbn, title, author, available_copies, total_copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.available_copies = available_copies
        self.total_copies = total_copies
    
    def borrow(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False
    
    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        return False
    
    def is_available(self):
        return self.available_copies > 0
    
    def get_info(self):
        return {
            "isbn": self.isbn,
            "title": self.title,
            "author": self.author,
            "available_copies": self.available_copies,
            "total_copies": self.total_copies
        }
