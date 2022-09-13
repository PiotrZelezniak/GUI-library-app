import sqlite3
import datetime

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year text, isbn text, borrow_day text, return_day text, mate_name text, UNIQUE(isbn))")
    cur.execute("INSERT OR IGNORE INTO book VALUES (NULL, 'Title', 'Author', 'Year', 'ISBN', 'Borrow date', 'Return date', 'Mate name')")
    conn.commit()
    conn.close()

def insert(title,author,year, isbn, name):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?,date(julianday('now')),NULL,?)", (title,author,year,isbn,name))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbn="", borrow="", returnday="", name=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ? OR borrow_day = ? OR return_day = ? OR mate_name = ?", (title,author,year,isbn, borrow, returnday, name))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn, borrow, returnday, name):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=?, borrow_day=?, return_day=?, mate_name=? WHERE id=?",(title, author, year, isbn, borrow, returnday, name, id))
    conn.commit()
    conn.close()


connect()
