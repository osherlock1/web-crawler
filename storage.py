import sqlite3

def initiate_db(path):
    connection = sqlite3.connect(path)
    cursor = connection.cursor()

    create_database = """CREATE TABLE IF NOT EXISTS pages(
                        id INTEGER PRIMARY KEY,
                        url TEXT UNIQUE,
                        status_code INTEGER,
                        depth INTEGER,
                        fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        )"""



    cursor.execute(create_database)
    connection.commit()
    cursor.execute("""CREATE TABLE IF NOT EXISTS links (
                   source_id INTEGER,
                   target_id INTEGER,
                   UNIQUE(source_id, target_id)
                   )""")
    connection.commit()