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
genre_id INTEGER NOT NULL,
FOREIGN KEY (author_id) REFERENCES autorid(autorid_Id),
FOREIGN KEY (genre_id) REFERENCES zanrid(genre_Id)
)
"""

insert_autorid = """
INSERT INTO
autorid(autori_nimi, Vanus,sünnipäev)
VALUES ('Jamie Beck', 24, '02-03-2000'),
       ('Iida Turpeinen', 25, '2001-04-15'),
       ('Helena Grauberg', 30, '1996-08-20'),
       ('Ants Rootslane', 28, '1998-11-10')
"""

insert_Zanrid = """
INSERT INTO
zanrid(genre_nimi)
VALUES ('Fantasy'),
       ('Ulme'),
       ('Romantika'),
       ('Detektiiv'),
       ('Luule')
"""
insert_raamatud = """
INSERT INTO raamatud(pealkiri, väljaandmise_kuup, author_id, genre_id)
VALUES ('Tähevihm', '2024-05-01', 1, 1),
       ('Mineviku vari', '2024-04-15', 2, 2),
       ('Jäävangistus', '2024-03-20', 3, 3),
       ('Pariisi saladused', '2024-02-10', 4, 4),
       ('Öise poeesia', '2024-01-05', 1, 5)
"""

filename=path.abspath(__file__)
dbdir=filename.rstrip('Raamatukataloog.py')
dbpath=path.join(dbdir,"data.db")
conn=create_connect(dbpath)
execute_query(conn, TB_Autorid)
execute_query(conn, TB_Zanrid)
execute_query(conn, TB_Raamatud)

execute_query(conn, insert_autorid)
execute_query(conn, insert_Zanrid)
execute_query(conn, insert_raamatud)

autorid1 = execute_read_query(conn, "SELECT * FROM autorid")
print("Kasutajate tabel:")
for TB_Autorid in autorid1:
    print(TB_Autorid)

zanrid1 = execute_read_query(conn, "SELECT * FROM zanrid")
print("zanri tabel:")
for TB_Zanrid in zanrid1:
    print(TB_Zanrid)

raamatud1 = execute_read_query(conn, "SELECT * FROM raamatud")
print("raamatud tabel:")
for TB_Raamatud in raamatud1:
    print(TB_Raamatud)
