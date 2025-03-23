import sqlite3

conn = sqlite3.connect('bird.db')
cursor = conn.cursor()
print('DB Init')


cursor.execute("""
CREATE TABLE IF NOT EXISTS mainspecies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mainspecies TEXT NOT NULL UNIQUE
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS subspecies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subspecies TEXT NOT NULL UNIQUE,
    mspecies_id INTEGER,
    FOREIGN KEY(mspecies_id) REFERENCES mainspecies(id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Bird (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL UNIQUE,
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
cursor.execute("""INSERT INTO mainspecies (mainspecies) VALUES('Parrot');""")
cursor.execute("""INSERT INTO mainspecies (mainspecies) VALUES('Songbirds');""")
cursor.execute("""INSERT INTO mainspecies (mainspecies) VALUES('Waterfowl');""")


conn.commit()
conn.close()

