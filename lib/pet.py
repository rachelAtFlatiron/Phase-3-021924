import sqlite3 
#creates the connection to a specific file 
#points to the database that we want to use (saved in lib/resources.db)
CONN = sqlite3.connect('resources.db', timeout=10) 
# https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor
# access point to fire off SQL queries
CURSOR = CONN.cursor()
 
class Pet:

    # ✅ 1. Add "__init__" with "name", "species", "breed", "temperament", and "id" (Default: None) Attributes
    #id represents primary key
    #if i create instance WITHOUT adding it to the database
    #my id won't exist, therefore default is none 
    def __init__(self, name, age, species, owner_id=None, id=None):
        self.name = name 
        self.age = age 
        self.id = id 
        self.species = species
        self.owner_id = owner_id 

    # ✅ 2. Create table
    @classmethod 
    def create_table(cls):
        sql = """ 
            CREATE TABLE IF NOT EXISTS pets 
            (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                species TEXT,
                owner_id INTEGER,
                FOREIGN KEY (owner_id) REFERENCES owners(id)
            );
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    # ✅ 3. Drop table
    @classmethod 
    def drop_table(cls):
        sql = """ 
            DROP TABLE IF EXISTS pets;
        """
        CURSOR.execute(sql)
        CONN.commit()
    

    # ✅ 4. Insert instance into DB as a row
    def save(self):
        try:
            sql = """ 
                INSERT INTO pets(name, age, species, owner_id)
                VALUES(?, ?, ?, ?);
            """
            CURSOR.execute(sql, (self.name, self.age, self.species, self.owner_id))
            CONN.commit()
            #get most recently inserted row 
            #update self.id 
            self.id = CURSOR.lastrowid
        except Exception as x:
            print(f'something went wrong {x}')

    # ✅ 5. Initialize instance and insert into database
    @classmethod 
    def create(cls, name, age, species, owner_id):
        pet = cls(name, age, species, owner_id) #here cls represents current class we are working in (i.e. Pet)
        pet.save()
        return pet 

    # ✅ 6. Create instance from DB, thus getting the ID
    @classmethod 
    def create_instance(cls, row):
        pet = cls(
            id=row[0],
            name=row[1],
            age=row[2],
            species=row[3],
            owner_id=row[4]
        )
        return pet 
    
    # ✅ 7. Get all rows
    @classmethod 
    def get_all(cls):
        sql = """ 
            SELECT * FROM pets;
        """
        #[[id, name, age, species], [id, name, age, species], [id, name, age, species], ...]
        rows = CURSOR.execute(sql).fetchall() 
        #turn list into list of instances 
        return [cls.create_instance(row) for row in rows]



    # ✅ 8. Get row by name
    @classmethod 
    def find_by_name(cls, name):
        sql = """ 
            SELECT * FROM pets WHERE name=?;
        """
        row = CURSOR.execute(sql, (name, )).fetchone()
        if not row:
            return None 
        else:
            return cls.create_instance(row)

    # ✅ 9. Get row by id
    @classmethod
    def find_by_id(cls, id):
        sql = """ 
            SELECT * FROM pets WHERE id=?;
        """
        row = CURSOR.execute(sql, (id, )).fetchone() #[1, "Fluffy", 2]
        if not row:
            return None
        else:
            return cls.create_instance(row)

    # ✅ 10. Find row, otherwise create row
    @classmethod 
    def find_or_create_by(cls, name=None, age=None, species=None, owner_id=None):
        try:
            # ✅ 10a. Search for pet
            sql = """  
                SELECT * FROM pets WHERE 
                (name, age, species, owner_id) = (?, ?, ?, ?)
            """
            #✅ 10b. Insert pet if it does not exist
            row = CURSOR.execute(sql, (name, age, species, owner_id))
            if not row: 
                return Pet.create(name, age, species, owner_id)
            return Pet.create_instance(row)
        # ✅ 10c. Return pet if it does exist
        except Exception as x:
            print(f'Something went wrong: {x}')

    # ✅ 11. Update row
        
    @classmethod 
    def delete_by_id(cls, id):
        try:
            sql = """ 
                DELETE FROM pets WHERE id=?;
            """
            CURSOR.execute(sql, (id, ))
            CONN.commit()
        except Exception as x:
            print(f'Something went wrong: {x}')
    

    def delete(self):
        try:
            sql = """ 
                DELETE FROM pets WHERE id=?;
            """
            CURSOR.execute(sql, (self.id, ))
            CONN.commit() 
        except Exception as x:
            print(f'Something went wrong: {x}')
    

    @classmethod 
    def delete_all(cls):
        sql = """ DELETE FROM pets; """

        CURSOR.execute(sql)
        CONN.commit()

    def update(self, name, age, species, owner_id):
        sql = """ 
            UPDATE pets SET name=?, age=?, species=? owner_id=? WHERE id=?;
        """
        CURSOR.execute(sql, (name, age, species, owner_id, self.id))
        CONN.commit()

    #pass in owner instance
    def add_owner(self, owner):
        try:
            sql = """ 
                UPDATE pets SET owner_id=? WHERE id=?;
            """
            CURSOR.execute(sql, (owner.id, self.id))
            CONN.commit()
            self.owner_id = owner.id
        except Exception as e:
            print(f'Something went wrong: {e}')

    def get_owner(self):
        sql = """ SELECT * FROM owners WHERE id=?"""
        row = CURSOR.execute(sql, (self.owner_id, )).fetchone()
        return row

    @property 
    def age(self):
        return self._age 
    @age.getter
    def age(self):
        return self._age 
    @age.setter 
    def age(self, val):
        self._age = val 
        if hasattr(self, 'id') and self.id != None:
            self.update(self.name, self._age, self.species, self.owner_id)



    def __repr__(self):
        return f"<{self.id} Pet {self.name} is a {self.age} yr old {self.species}>"

