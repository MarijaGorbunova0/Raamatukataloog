from cmath import e
from sqlite3 import *
from os import DirEntry, path
from tkinter import *
from tkinter.ttk import Treeview
from turtle import heading
aken = Tk()
aken.geometry("800x600")
aken.title("raamatukataloog")
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
def execute_insert_query(connection, data):
    query = "INSERT INTO autorid(autori_nimi, Vanus,sünnipäev) VALUES(?,?,?,?,?,?)"
    cursor = connection.cursor()
    cursor.execute(query, data)
    connection.commit()

def SPautorid():
    AA = Tk()
    AA.title("autorid")
    
    tree = Treeview(AA, columns=("ID", "nimi", "vanus", "Sünnipäev"))
    tree.column("#1", minwidth=0, width=50)
    tree.heading("#1", text="ID")
    tree.heading("#2", text="nimi")
    tree.column("#2", minwidth=0, width=150)
    tree.heading("#3", text="vanus")
    tree.column("#3", minwidth=0, width=50)
    tree.heading("#4", text="Sünnipäev")
    tree.column("#4", minwidth=0, width=100)
    tree.pack()
    
    autorid_data = execute_read_query(conn, "SELECT * FROM autorid")
    for row in autorid_data:
        tree.insert('', 'end', values=row)
    
    AA.mainloop()

def SPzanrid():
    AA = Tk()
    AA.title("Zanrid")
   
    tree = Treeview(AA, columns=("ID", "nimi"))
    tree.column("#1", minwidth=0, width=50)
    tree.heading("#1", text="ID")
    tree.heading("#2", text="nimi")
    tree.column("#2", minwidth=0, width=150)
    tree.pack()
    
    autorid_data = execute_read_query(conn, "SELECT * FROM zanrid")
    for row in autorid_data:
        tree.insert('', 'end', values=row)
    
    AA.mainloop()

def SPraamatud():
    AA = Tk()
    AA.title("raamatud")
    
    tree = Treeview(AA, columns=("ID", "pealkiri", "kuupaev", "autori_id", "genre_id"), show = 'headings')
    tree.column("#1", minwidth=0, width=50)
    tree.heading("#1", text="ID")
    tree.heading("#2", text="pealkiri")
    tree.column("#2", minwidth=0, width=150)
    tree.heading("#3", text="kuupaev")
    tree.column("#3", minwidth=0, width=50)
    tree.heading("#4", text="autorid_id")
    tree.column("#4", minwidth=0, width=100)
    tree.heading("#5", text="genre_id")
    tree.column("#5", minwidth=0, width=100)

    tree.grid()
    
    autorid_data = execute_read_query(conn, "SELECT * FROM raamatud")
    for row in autorid_data:
        tree.insert('', 'end', values=row)
    lisadaB = Button(AA,
              text = "lisada",
              bg="#a3c9f7",
              fg="#94041f",
              font="Algerian 15",
              height = 2, width= 10
              ) 
    R_pealkiri = Label(AA,
                text = "pealkiri:",
                fg = "#94041f",
                font = "Algerian 20",
                height = 3 )
    INPpealkiri = Entry(AA,
               text = "pealkiri",          
               fg = "#94041f",
               font = "Algerian 20",
               width = 10
               )
    def lisadaR():

        lisage_autori= (
            INPpealkiri("Nimi: "),          
            int(input("Vanus: ")),
            int(input("sunnipaev ")),
             )   
        execute_insert_query(conn, lisage_autori)
        raamatud = execute_read_query(conn, "SELECT * FROM raamatud")
    
    lisadaB.grid(row = 2, column = 3) 
    INPpealkiri.grid(row = 1, column = 9)
    R_pealkiri.grid(row = 1, column = 1)
    AA.mainloop() 

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


f = Frame(aken)
var = IntVar()
autoridB = Button(aken,
              text = "autorid",
              bg="#a3c9f7",
              fg="#94041f",
              font="Algerian 15",
              height = 3, width= 10,
              command = SPautorid
          )

zanriB = Button(aken,
              text = "Zanr",
              bg="#a3c9f7",
              fg="#94041f",
              font="Algerian 15",
              height = 3, width= 10,
              command = SPzanrid
          )
raamatudB = Button(aken,
              text = "raamatud",
              bg="#a3c9f7",
              fg="#94041f",
              font="Algerian 15",
              height = 3, width= 10,
              command = SPraamatud
          )
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

autoridB.grid(row = 1, column = 1)
zanriB.grid(row = 1, column = 2)
raamatudB.grid(row = 1, column = 3)
aken.mainloop()
