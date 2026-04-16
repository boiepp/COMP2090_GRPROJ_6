books = [
    {"isbn": "9780141182803", "title": "1984", "author": "George Orwell", "available_copies": 3, "total_copies": 3},
    {"isbn": "9780061120084", "title": "To Kill a Mockingbird", "author": "Harper Lee", "available_copies": 2, "total_copies": 2},
    {"isbn": "9780451524935", "title": "Animal Farm", "author": "George Orwell", "available_copies": 4, "total_copies": 4},
    {"isbn": "9780743273565", "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "available_copies": 1, "total_copies": 1},
    {"isbn": "9780131103627", "title": "The C Programming Language", "author": "Brian Kernighan", "available_copies": 0, "total_copies": 2}
]

borrowers = [
    {"borrower_id": "B001", "name": "Ngai Pik Yi", "phone": "61234567"},
    {"borrower_id": "B002", "name": "Lam Wing Hei Sophie", "phone": "62345678"},
    {"borrower_id": "B003", "name": "Poon Po Yee", "phone": "63456789"}
]

borrow_records = [
    {"record_id": "R001", "borrower_id": "B001", "isbn": "9780131103627", "borrow_date": "2026-03-01", "due_date": "2026-03-15", "status": "borrowed"},
    {"record_id": "R002", "borrower_id": "B002", "isbn": "9780141182803", "borrow_date": "2026-03-05", "due_date": "2026-03-19", "status": "borrowed"},
    {"record_id": "R003", "borrower_id": "B001", "isbn": "9780451524935", "borrow_date": "2026-02-20", "due_date": "2026-03-06", "status": "returned"}
]

def find_book_by_isbn(isbn):
    for book in books:
        if book["isbn"] == isbn:
            return book
    return None

def find_borrower_by_id(borrower_id):
    for borrower in borrowers:
        if borrower["borrower_id"] == borrower_id:
            return borrower
    return None

def get_borrow_records(borrower_id):
    records = []
    for record in borrow_records:
        if record["borrower_id"] == borrower_id:
            records.append(record)
    return records

def add_borrow_record(record):
    borrow_records.append(record)

def update_borrow_record(record_id, status):
    for record in borrow_records:
        if record["record_id"] == record_id:
            record["status"] = status
            return True
    return False

def get_all_books():
    return books

def get_all_borrowers():
    return borrowers

def get_all_borrow_records():
    return borrow_records


def get_all_borrow_records():
    return borrow_records
