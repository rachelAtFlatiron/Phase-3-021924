# Stretch Goal: Build Out Corresponding Owner Class Methods

# Owner Attributes: 
# name: string 
# phone: string 
# email: string 
# address: string

import sqlite3
from pet import Pet

CONN = sqlite3.connect('resources.db')
CURSOR = CONN.cursor()

class Owner:
    
    def __init__(self, name, email, id="None"):
        self.name = name 
        self.email = email 
        self.id = id

    # ✅ 12. Create table
    @classmethod 
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS owners(
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    

    # ✅ 13. Drop table
    @classmethod 
    def drop_table(cls):
        sql = "DROP TABLE owners; "
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod 
    def create_instance(cls, row):
        owner = cls(
            id=row[0],
            name=row[1],
            email = row[2]
        )
        return owner 
    
    # ✅ 14. Insert row
    def save(self):
        try: 
            sql = """ 
                INSERT INTO owners (name, email)
                VALUES(?, ?);
            """
            # ✅ 14a. Update instance with new row's id
            CURSOR.execute(sql, (self.name, self.email))
            CONN.commit()
            self.id = CURSOR.lastrowid
        except Exception as x:
            print(f'Something went wrong: {x}')

    # ✅ 15. Get all rows
    @classmethod 
    def get_all(cls):
        sql = """ SELECT * FROM owners; """
        rows = CURSOR.execute(sql)
        return [Owner.create_instance(owner) for owner in rows]

    # ✅ 15a. Create helper method to turn a row into an owner instance

    # ✅ 16. Get row by id

    # ✅ 17. Delete row by id
    @classmethod 
    def delete_all(cls):
        sql = """DELETE FROM owners;"""
        CURSOR.execute(sql)
        CONN.commit()

    # ✅ 18. Update row by id
    
    def get_pets(self):
        sql = """ 
            SELECT * FROM pets WHERE owner_id=?;
        """
        rows = CURSOR.execute(sql, (self.id, )).fetchall()
        return [Pet.create_instance(pet) for pet in rows]
        

    def __repr__(self):
        return f'<Owner id={self.id} name={self.name} />'