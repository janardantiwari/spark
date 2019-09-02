import sqlite3

def connect():
    c=sqlite3.connect("book_manager.db")
    cur=c.cursor()
    cur.execute("CREATE TABLE IF NOT  EXISTS library(id INTEGER PRIMARY KEY , title TEXT,author text,year integer,isbn integer)")
    c.commit()
    c.close()

def insert(title,author,year,isbn):
    c=sqlite3.connect("book_manager.db")
    cur=c.cursor()
    cur.execute("INSERT INTO library  VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    c.commit()
    c.close()
    
    

def view():
    c=sqlite3.connect("book_manager.db")
    cur=c.cursor()
    cur.execute("SELECT * FROM library")
   
    r=cur.fetchall()
    c.close()
    return r

def search(title="",author="",year="",isbn=""):
    c=sqlite3.connect("book_manager.db")
    cur=c.cursor()
    cur.execute("SELECT * FROM library WHERE title=? or author=? or year=? or isbn=?",(title,author,year,isbn))
    
    r=cur.fetchall()
    c.close()
    return r
    
def delete(id):
    conn=sqlite3.connect("book_manager.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM library WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn=sqlite3.connect("book_manager.db")
    cur=conn.cursor()
    cur.execute("UPDATE library SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()


connect()
#insert("trees","Ruskin Bond",1976,123440)
#print(view())

