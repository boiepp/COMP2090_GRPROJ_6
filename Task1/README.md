# Task 1 - Library Management System

## Group Members [ GRP_6 ]
- NGAI Pik Yi (14261837)
- LAM Wing Hei Sophie (14265664)
- POON Po Yee (13884023)

## Description
A Python-based library management system using OOP concepts including encapsulation, inheritance, abstraction, and polymorphism.

## How to Run
1. Ensure Python 3.x is installed
2. Run the main program:
   python main.py
3. No external packages required git clone

https://github.com/boiepp/COMP2090_GRP6.git

## Default Login Credentials
### Borrower Login
- B001 (Ngai Pik Yi)
- B002 (Lam Wing Hei Sophie)
- B003 (Poon Po Yee)

### Manager Login
- ID: M001
- Password: admin123

## Books Available in the System

| ISBN | Title | Author | Available Copies |
|------|-------|--------|------------------|
| 9780141182803 | 1984 | George Orwell | 3 |
| 9780061120084 | To Kill a Mockingbird | Harper Lee | 2 |
| 9780451524935 | Animal Farm | George Orwell | 4 |
| 9780743273565 | The Great Gatsby | F. Scott Fitzgerald | 1 |
| 9780131103627 | The C Programming Language | Brian Kernighan | 0 (Out of stock) |

## Current Borrowing Records

| Borrower ID | Borrower Name | ISBN | Book Title | Borrow Date | Due Date | Status |
|-------------|---------------|------|------------|-------------|----------|--------|
| B001 | Ngai Pik Yi | 9780131103627 | The C Programming Language | 2026-03-01 | 2026-03-15 | borrowed |
| B002 | Lam Wing Hei Sophie | 9780141182803 | 1984 | 2026-03-05 | 2026-03-19 | borrowed |
| B001 | Ngai Pik Yi | 9780451524935 | Animal Farm | 2026-02-20 | 2026-03-06 | returned |

### Currently Borrowed (Not Returned Yet)

| Borrower | Book Title | Due Date |
|----------|------------|----------|
| Ngai Pik Yi (B001) | The C Programming Language | 2026-03-15 |
| Lam Wing Hei Sophie (B002) | 1984 | 2026-03-19 |

## Features
### Borrowers can:
- Search books by title or author
- Borrow available books
- Return borrowed books
- Renew books (extend due date by 14 days)
- View personal borrowing records

### Managers can:
- View all books
- Add new books
- Update book information
- Delete books
- View all borrowers
- Add new borrowers
- Modify borrower information
- Delete borrowers
- View all borrowing records

## Modules
- main.py - Entry point
- data.py - Sample data and database functions
- bookfunction.py - Book class with borrow/return logic
- user.py - Parent User class
- borrower.py - Borrower class with all borrower functions
- manager.py - Manager class with all management functions
- interface.py - Menu display and login interface

## Video Introduction



