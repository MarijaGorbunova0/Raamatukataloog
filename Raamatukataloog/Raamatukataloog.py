from sqlite3 import *
from os import path
def create_connect(path:str):
    connection = None
    try:
        connection = connect(path)
        print("Ühendus loodud")
    except Error as e:
        print(f"Tekkis viga: {e}")
    return connection 

def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Tabel on loodud või andmed on sisestatu")      
    except Error as e:
        print(f"Tekkis viga: {e}")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
    except Error as e:
        print(f"Tekkis viga: {e}")
    return result

TB_Autorid = """
CREATE TABLE IF NOT EXISTS autorid(
autorid_Id INTEGER PRIMARY KEY AUTOINCREMENT,
autori_nimi TEXT NOT NULL,
Vanus INTEGER NOT NULL,
sünnipäev DATE NOT NULL
)
"""
TB_Zanrid = """
CREATE TABLE IF NOT EXISTS zanrid(
genre_Id INTEGER PRIMARY KEY AUTOINCREMENT,
genre_nimi TEXT NOT NULL
)
"""
TB_Raamatud = """
CREATE TABLE IF NOT EXISTS raamatud(
raamatu_Id INTEGER PRIMARY KEY AUTOINCREMENT,
pealkiri TEXT NOT NULL,
väljaandmise_kuup DATE NOT NULL,
author_id INTEGER NOT NULL,
FOREIGN KEY (author_id) REFERENCES autorid(autorid_Id),
genre_id INTEGER NOT NULL,
FOREIGN KEY (genre_id) REFERENCES zanrid(genre_Id)
)
"""

#insert_autorid = """
#INSERT INTO
#autorid(autori_nimi, Vanus,sünnipäev )
#VALUES ("")
#"""

filename=path.abspath(__file__)
dbdir=filename.rstrip('Raamatukataloog.py')
dbpath=path.join(dbdir,"data.db")
conn=create_connect(dbpath)
execute_query(conn, TB_Autorid)
execute_query(conn, TB_Zanrid)
execute_query(conn, TB_Raamatud)