import sqlite3

conn = sqlite3.connect('bird.db')
cursor = conn.cursor()
print('DB Init')


cursor.execute("""
CREATE TABLE IF NOT EXISTS mainspecies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mainspecies TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS subspecies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subspecies TEXT NOT NULL,
    mspecies_id INTEGER,
    FOREIGN KEY(mspecies_id) REFERENCES mainspecies(id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Bird (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL,
    species_id INTEGER,
    mspecies_id INTEGER,
    Image_URL VARCHAR(300) DEFAULT NULL,
    description VARCHAR(3000) DEFAULT NULL,
    life_expectancy TEXT CHECK(life_expectancy IN ('short', 'medium', 'long')) DEFAULT NULL,
    status TEXT CHECK (status IN ('hunter', 'prey')) DEFAULT NULL,
    keywords VARCHAR(100) DEFAULT NULL,
    FOREIGN KEY(species_id) REFERENCES subspecies(id),
    FOREIGN KEY(mspecies_id) REFERENCES mainspecies(id)
);
""")

# Insert data here
cursor.execute("""
INSERT INTO mainspecies (mainspecies)
SELECT 'Parrot'
WHERE NOT EXISTS (SELECT 1 FROM mainspecies WHERE mainspecies = 'Parrot');
""")

cursor.execute("""
INSERT INTO subspecies (subspecies, mspecies_id)
SELECT 'Budgie', mainspecies.id
FROM mainspecies
WHERE mainspecies.mainspecies = 'Parrot'
AND NOT EXISTS (SELECT 1 FROM subspecies WHERE subspecies = 'Budgie');
""")

cursor.execute("""
INSERT INTO Bird (name, species_id, Image_URL, description, life_expectancy, status, keywords)
SELECT 'Budgie', subspecies.id, 'https://tse2.mm.bing.net/th?id=OIP.7YjtFYyysnJlt81K5ghAJQHaEK&pid=Api', 'A small, colorful parrot native to Australia.', 'medium', 'prey', 'small, colorful, Australia'
FROM subspecies
JOIN mainspecies ON subspecies.mspecies_id = mainspecies.id
WHERE subspecies.subspecies = 'Budgie'
AND mainspecies.mainspecies = 'Parrot';
""")
