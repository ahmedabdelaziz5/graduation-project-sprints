import sqlite3

def CreateTable(NameTable,rows):
    try:
        db = sqlite3.connect('DateBase.db')
        cr = db.cursor()
        cr.execute(f"CREATE TABLE {NameTable}{rows}")
        db.commit()
        print("Alright")
    except:
        print("Wrong DATA")
    finally:
        db.close()

def insert_id(id):
    try:
        db = sqlite3.connect('DateBase.db')
        cr = db.cursor()
        cr.execute(f"INSERT INTO National_IDs VALUES({id})")
        db.commit()
    finally:
        db.close()

def delete_id(id):
    try:
        db = sqlite3.connect('DateBase.db')
        cr = db.cursor()
        cr.execute(f"DELETE FROM National_IDs WHERE Nid = {id}")
        db.commit()
    finally:
        db.close()

def delete_all_IDs():
    try:
        db = sqlite3.connect('DateBase.db')
        cr = db.cursor()
        cr.execute(f"DELETE FROM National_IDs")
        db.commit()
    finally:
        db.close()


def getIDs():
    db = sqlite3.connect('DateBase.db')
    cr = db.cursor()
    cr.execute(f"SELECT * FROM National_IDs")
    for row in cr.fetchall():
        print(*row)



# CreateTable('National_IDs', '(Nid VARCHAR, PRIMARY KEY(Nid))')
# insert('30206161802915')
# getIDs()