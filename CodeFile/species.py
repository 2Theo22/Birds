import sqlite3

from connection import db_conn

def search_species(search_query): 
    if search_query is None: 
        return False, None
    try: 
        conn = db_conn()
        cursor = conn.cursor()
        query = """
                SELECT Bird.name, mainspecies.mainspecies, subspecies.subspecies, Bird.Image_URL, Bird.description, Bird.life_expectancy, Bird.status, Bird.keywords
                FROM Bird
                JOIN subspecies ON Bird.species_id = subspecies.id
                JOIN mainspecies ON Bird.mspecies_id = mainspecies.id
                WHERE Bird.species = ?;
                """
        search = '%' + search_query + '%'
        cursor.execute(query, (search,))
        results = cursor.fetchall()
        conn.close()
        return True, results
    except Exception as e:
        return False, str(e)