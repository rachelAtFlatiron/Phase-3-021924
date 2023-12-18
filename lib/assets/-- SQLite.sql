-- SQLite
-- ✅ 1. Select specific columns
SELECT id, name, address FROM owners;
-- all columns, use * 
SELECT * FROM owners;

-- ✅ 2. Create new database structure
CREATE TABLE pets(
    id INTEGER PRIMARY KEY,
    name TEXT,
    owner_id INTEGER,
    birthdate INTEGER,
    breed TEXT,
    favorite_treats TEXT,
    last_fed_at DATETIME, -- includes hour and minute
    last_walked_at DATETIME,
        FOREIGN KEY(owner_id) REFERENCES owners(id)
);

-- ✅ 2a. Remove owners table

-- ✅ 2b. Create owners table

-- ✅ 2c. Create pets table

-- ✅ 3. Modify pets table

-- ✅ 3a. Add image_url to pets
ALTER TABLE pets 
ADD COLUMN image_url TEXT;

-- ✅ 3b. Rename column
ALTER TABLE pets 
RENAME COLUMN birthdate TO age;

-- ✅ 4. Create new instances

-- ✅ 4a. Use chatGPT to create random owners

-- ✅ 4b. Use chat GPT to create sample data for pets

-- Sample data for cats
INSERT INTO pets (name, age, owner_id, breed, favorite_treats, last_fed_at, last_walked_at, image_url)
VALUES ('Whiskers', 5, 1, 'Siamese', 'Tuna', '2023-08-30 09:00:00', NULL, 'https://example.com/whiskers.jpg');

INSERT INTO pets (name, age, owner_id, breed, favorite_treats, last_fed_at, last_walked_at, image_url)
VALUES ('Fluffy', 3, 2, 'Persian', 'Salmon', '2023-08-29 18:30:00', NULL, 'https://example.com/fluffy.jpg');

-- Sample data for dogs
INSERT INTO pets (name, age, owner_id, breed, favorite_treats, last_fed_at, last_walked_at, image_url)
VALUES ('Buddy', 2, 3, 'Golden Retriever', 'Biscuits', '2023-08-30 07:45:00', '2023-08-30 16:00:00', 'https://example.com/buddy.jpg');

INSERT INTO pets (name, age, owner_id, breed, favorite_treats, last_fed_at, last_walked_at, image_url)
VALUES ('Max', 4, 4, 'German Shepherd', 'Peanut Butter', '2023-08-29 19:15:00', '2023-08-29 20:30:00', 'https://example.com/max.jpg');

-- Adding two more cats
INSERT INTO pets (name, age, owner_id, breed, favorite_treats, last_fed_at, last_walked_at, image_url)
VALUES ('Smokey', 2, 4, 'Russian Blue', 'Catnip', '2023-08-30 10:15:00', NULL, 'https://example.com/smokey.jpg');

INSERT INTO pets (name, age, owner_id, breed, favorite_treats, last_fed_at, last_walked_at, image_url)
VALUES ('Luna', 1, 3, 'Scottish Fold', 'Tuna', '2023-08-29 20:45:00', NULL, 'https://example.com/luna.jpg');

-- Adding two birds
INSERT INTO pets (name, age, owner_id, breed, favorite_treats, last_fed_at, last_walked_at, image_url)
VALUES ('Rio', 1, 1, 'Parrot', 'Sunflower Seeds', '2023-08-30 08:30:00', NULL, 'https://example.com/rio.jpg');

INSERT INTO pets (name, age, owner_id, breed, favorite_treats, last_fed_at, last_walked_at, image_url)
VALUES ('Sunny', 3, 2, 'Canary', 'Millet', '2023-08-29 16:00:00', NULL, 'https://example.com/sunny.jpg');



-- ✅ 5. Read data

-- ✅ 5a. Get all columns from pets
SELECT * FROM pets;

-- ✅ 5b. Select pet by name
SELECT * FROM pets WHERE name = 'Luna';
-- ✅ 5c. Select pets by favorite treats
SELECT name, owner_id FROM pets WHERE favorite_treats = 'Tuna';
-- ✅ 5d. Select pets by age 
SELECT name, age, owner_id, favorite_treats FROM pets WHERE age < 3;
SELECT name, age, owner_id FROM pets WHERE age < 3 AND owner_id = 3;

-- ✅ 6. Update data
-- ✅ 6a. Update pet's age by name
UPDATE pets 
SET age = 12 
WHERE name = 'Luna';

-- ✅ 6b. Update multiple pets' favorite_treats
UPDATE pets 
SET favorite_treats = "Water";

UPDATE pets 
SET owner_id = 1
WHERE id = 8;

-- ✅ 7. Delete data
DELETE FROM pets WHERE age > 8;

-- ✅ 8. Join data 
-- ✅ 8a. One to many
-- pet_name, owner_name 
SELECT pets.name, owners.name as 'owner'
FROM pets JOIN owners
ON pets.owner_id = owners.id;

-- ✅ 8b. Many to many: create staff table 

-- ✅ 8c. Many to many: create appointments table

-- ✅ 9. Seed data

-- ✅ 9a. Create two staff members using ChatGPT

-- ✅ 9b. Create six appointments using ChatGPT

-- ✅ 10. Join tables

-- ✅ 10a. Basic join

-- ✅ 10b. Basic join with specific values

-- ✅ 10c. Inner join

-- ✅ 10d. Outer join